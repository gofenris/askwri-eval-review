"""Ingest annot-*.json review files into evalset review_status (spec §2.4).

Usage:
  uv run scripts/ingest_review_status.py --evalset evalsets/evalset_answer_02.json \
      --annot review-output/ [--dry-run]

Rules (spec §2.4, exact):
- a passage labeled `no` (any reviewer) is dropped from expected_passages and
  its supports_key_fact is flagged in the case note;
- a canonical answer (or, on negative cases, the negative-case validity)
  labeled `no` blocks approval; the case stays `draft` and the reviewer's
  note is quoted in a marker;
- all passages yes and answer yes (>=1 yes on every item, no `no` anywhere,
  nothing unlabeled, no reviewer conflicts) sets expert_approved; on negative
  cases (no expected_external_ids AND no key_facts) the negative-case
  validity takes the answer's role;
- conflicting reviewers (yes AND no on the same item) leave draft and list both;
- `skip` and absent labels are neutral: silent (no marker, no drop, no
  conflict), but a skipped item is not a "yes", so it blocks approval;
- `rejected` is never written by this script (manual maintainer edit);
- drops are IRREVERSIBLE through this script: a passage removed from
  expected_passages stays removed, and its no-vote keeps blocking approval on
  every re-run. Restoring a dropped passage is a manual evalset edit;
- review markers are note lines starting `[review ` — content-deduplicated
  (an identical marker line is never appended twice) and dated from the
  annot labels' own `timestamp` field, so the same annot set always produces
  byte-identical output. ALWAYS pass the whole annot directory: re-ingesting
  a partial subset can miss no-votes recorded in files you leave out, and a
  previously-dropped passage's blocking no-vote goes unseen. Top-level
  `updated` is refreshed to the run date; `version` is never touched.

Annot files are named `annot-{evalset-stem}-<query>-by-<reviewer>.json` where
{evalset-stem} is the evalset JSON file's name without extension (e.g.
`evalset_answer_02`). A top-level `query_id` not matching any case id raises;
a label outside {yes,no,skip} raises — both errors name the annot file. The
optional `_annot_file` key (set by the CLI) is metadata used only in those
error messages and is ignored by the review logic.

Pure core: ingest(evalset: dict, annots: list[dict]) -> (dict, list[str]);
the CLI wrapper does the file I/O. Nothing here calls a model or service.
"""

from __future__ import annotations

import argparse
import copy
import json
import sys
from datetime import date
from pathlib import Path
from typing import Any

VALID_LABELS = {"yes", "no", "skip"}


def _label_date(entry: dict[str, Any] | None) -> str:
    """Date part of a label's own timestamp (never the run date)."""
    if not entry:
        return ""
    return str(entry.get("timestamp") or "")[:10]


def _where(annot: dict) -> str:
    """File name for error messages (the CLI sets `_annot_file`)."""
    return annot.get("_annot_file") or (
        f"query_id {annot.get('query_id')!r} (reviewer {annot.get('reviewer')!r})"
    )


def _case_is_negative(case: dict) -> bool:
    """Negative case: no expected docs AND no key facts."""
    rt = case.get("retrieval_ground_truth") or {}
    st = case.get("synthesis_ground_truth") or {}
    return not (rt.get("expected_external_ids") or []) and not (st.get("key_facts") or [])


def ingest(evalset: dict, annots: list[dict]) -> tuple[dict, list[str]]:
    """Apply annot review labels to an evalset (pure; no file I/O).

    Returns (new_evalset, report_lines). Cases with annots get
    review_status "expert_approved" or "draft"; cases without annots are
    completely untouched; "rejected" is never written. Passage drops are
    irreversible through this script (restoring one is a manual evalset
    edit). The input dict is not mutated.

    Each annot may carry an optional `_annot_file` key (set by the CLI);
    it is metadata for error messages only.
    """
    new_es = copy.deepcopy(evalset)
    cases = {
        c.get("id"): c
        for c in new_es.get("test_cases", [])
        if isinstance(c, dict) and c.get("id")
    }
    report: list[str] = []

    # Validate everything before touching anything.
    for annot in annots:
        qid = annot.get("query_id")
        if qid not in cases:
            raise ValueError(f"{_where(annot)}: unknown query_id {qid!r}")
        for p in annot.get("reviewed_passages") or []:
            if p.get("label") not in VALID_LABELS:
                raise ValueError(
                    f"{_where(annot)}: invalid label {p.get('label')!r} on "
                    f"passage {p.get('chunk_id')!r} (expected yes|no|skip)"
                )
        for item in ("synthesis_review", "negative_case_review"):
            entry = annot.get(item)
            if entry is not None and entry.get("label") not in VALID_LABELS:
                raise ValueError(
                    f"{_where(annot)}: invalid label {entry.get('label')!r} "
                    f"on {item} (expected yes|no|skip)"
                )

    grouped: dict[str, list[dict]] = {}
    for annot in annots:
        grouped.setdefault(annot["query_id"], []).append(annot)

    today = date.today().isoformat()
    approved_total = 0
    draft_total = 0
    for qid, group in grouped.items():
        case = cases[qid]
        old_status = case.get("review_status")  # absent = draft
        original_lines = (case.get("note") or "").split("\n")
        existing = set(original_lines)
        new_markers: list[str] = []

        # Per-item labels over the full annot group, in event order.
        passage_labels: dict[str, list[dict]] = {}
        answer_labels: list[dict] = []
        validity_labels: list[dict] = []
        for annot in group:
            reviewer = annot.get("reviewer")
            for p in annot.get("reviewed_passages") or []:
                passage_labels.setdefault(p["chunk_id"], []).append(
                    {
                        "reviewer": reviewer,
                        "label": p.get("label"),
                        "ts": _label_date(p),
                        "notes": p.get("notes") or "",
                    }
                )
            sr = annot.get("synthesis_review")
            if sr is not None:
                answer_labels.append(
                    {
                        "reviewer": reviewer,
                        "label": sr.get("label"),
                        "ts": _label_date(sr),
                        "notes": sr.get("notes") or "",
                    }
                )
            vr = annot.get("negative_case_review")
            if vr is not None:
                validity_labels.append(
                    {
                        "reviewer": reviewer,
                        "label": vr.get("label"),
                        "ts": _label_date(vr),
                        "notes": vr.get("notes") or "",
                    }
                )

        def append_marker(line: str) -> None:
            if line not in existing:
                new_markers.append(line)
                existing.add(line)

        # --- passage drops + conflict markers (event order) ----------------
        expected = list(
            (case.get("retrieval_ground_truth") or {}).get("expected_passages") or []
        )
        for cid, events in passage_labels.items():
            no_events = [e for e in events if e["label"] == "no"]
            has_no = bool(no_events)
            conflict = has_no and any(e["label"] == "yes" for e in events)
            if has_no:
                no_reviewers = ",".join(e["reviewer"] for e in no_events)
                passage = next(
                    (p for p in expected if p.get("chunk_id") == cid), None
                )
                if passage is not None:
                    # Drop. Irreversible through this script: the passage
                    # leaves expected_passages for good (manual edit to undo).
                    case_gt = case.setdefault("retrieval_ground_truth", {})
                    case_gt["expected_passages"] = [
                        p for p in expected if p.get("chunk_id") != cid
                    ]
                    expected = case_gt["expected_passages"]
                    fact = passage.get("supports_key_fact") or ""
                    append_marker(
                        f"[review {no_events[0]['ts']} r={no_reviewers}] "
                        f"passage {cid} dropped (labeled no); "
                        f"fact needs re-sourcing: {fact}"
                    )
                    report.append(f"case {qid}: dropped passage {cid} (labeled no)")
                elif not any(
                    ln.startswith("[review ")
                    and f"passage {cid}" in ln
                    and "dropped" in ln
                    for ln in original_lines
                ):
                    # Already dropped (earlier run or manual edit): the drop
                    # marker exists; emit the reduced form only if none does.
                    append_marker(
                        f"[review {no_events[0]['ts']} r={no_reviewers}] "
                        f"passage {cid} labeled no (already dropped; fact unknown)"
                    )
            if conflict:
                pairs = ", ".join(f"{e['reviewer']}={e['label']}" for e in events)
                append_marker(
                    f"[review {no_events[0]['ts']}] conflicting labels on "
                    f"passage {cid}: {pairs} — left draft"
                )
                report.append(
                    f"case {qid}: conflicting labels on passage {cid}: "
                    f"{pairs} — left draft"
                )

        # --- answer / validity items ----------------------------------------
        is_negative = _case_is_negative(case)
        for labels, item_name, marker_noun in (
            (answer_labels, "canonical answer", "canonical answer labeled no"),
            (
                validity_labels,
                "negative-case validity",
                "negative-case validity labeled no",
            ),
        ):
            no_events = [e for e in labels if e["label"] == "no"]
            yes_events = [e for e in labels if e["label"] == "yes"]
            has_no = bool(no_events)
            conflict = has_no and bool(yes_events)
            if has_no:
                no_reviewers = ",".join(e["reviewer"] for e in no_events)
                notes = "; ".join(e["notes"] for e in no_events if e["notes"])
                line = (
                    f"[review {no_events[0]['ts']} r={no_reviewers}] {marker_noun}"
                )
                if notes:
                    line += f": {notes}"
                append_marker(line)
            if conflict:
                pairs = ", ".join(f"{e['reviewer']}={e['label']}" for e in labels)
                append_marker(
                    f"[review {no_events[0]['ts']}] conflicting labels on "
                    f"{item_name}: {pairs} — left draft"
                )
                report.append(
                    f"case {qid}: conflicting labels on {item_name}: "
                    f"{pairs} — left draft"
                )

        # --- approval state machine ------------------------------------------
        remaining = [p.get("chunk_id") for p in expected]
        if remaining:
            passage_ok = all(
                any(e["label"] == "yes" for e in passage_labels.get(cid, []))
                for cid in remaining
            )
        else:
            # negative case: no passages to approve
            passage_ok = True
        gate = validity_labels if is_negative else answer_labels
        gate_ok = bool(gate) and not any(e["label"] == "no" for e in gate) and any(
            e["label"] == "yes" for e in gate
        )
        any_has_no = any(
            e["label"] == "no"
            for events in list(passage_labels.values()) + [answer_labels, validity_labels]
            for e in events
        )
        has_conflict = any(
            any(e["label"] == "no" for e in events)
            and any(e["label"] == "yes" for e in events)
            for events in list(passage_labels.values()) + [answer_labels, validity_labels]
        )
        approved = (
            not any_has_no
            and not has_conflict
            and passage_ok
            and gate_ok
        )
        new_status = "expert_approved" if approved else "draft"
        if approved:
            approved_total += 1
        else:
            draft_total += 1
        case["review_status"] = new_status
        report.append(f"case {qid}: review_status {old_status or 'absent'} -> {new_status}")

        if new_markers:
            note = case.get("note") or ""
            if note:
                case["note"] = note.rstrip("\n") + "\n" + "\n".join(new_markers)
            else:
                case["note"] = "\n".join(new_markers)

    report.append(
        f"{approved_total} expert_approved, {draft_total} draft, "
        f"{len(new_es.get('test_cases', [])) - len(grouped)} untouched"
    )
    new_es["updated"] = today  # run date; version is never touched
    return new_es, report


def main() -> None:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("--evalset", type=Path, required=True, help="Evalset JSON path (written in place unless --dry-run)")
    parser.add_argument(
        "--annot",
        type=Path,
        nargs="+",
        required=True,
        help="Annot dir (searched for annot-<evalset-stem>-*.json) or explicit annot JSON files; ALWAYS pass the whole directory",
    )
    parser.add_argument("--dry-run", action="store_true", help="Report only; do not write the evalset")
    args = parser.parse_args()

    evalset_path = args.evalset
    evalset = json.loads(evalset_path.read_text(encoding="utf-8"))
    stem = evalset_path.stem

    annot_files: list[Path] = []
    for p in args.annot:
        if p.is_dir():
            annot_files.extend(sorted(p.rglob(f"annot-{stem}-*.json")))
        elif p.is_file():
            annot_files.append(p)
        else:
            print(f"warning: no such file or directory: {p}", file=sys.stderr)
    # de-duplicate, preserving order
    annot_files = list(dict.fromkeys(annot_files))

    if not annot_files:
        print(f"no annot files found for evalset {stem!r} under: {', '.join(str(a) for a in args.annot)}")
        print("evalset left untouched")
        return

    annots = []
    for f in annot_files:
        annot = json.loads(f.read_text(encoding="utf-8"))
        annot["_annot_file"] = f.name
        annots.append(annot)

    new_evalset, report = ingest(evalset, annots)
    for line in report:
        print(line)

    if args.dry_run:
        print("dry run: evalset not written")
        return

    evalset_path.write_text(
        json.dumps(new_evalset, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"wrote {evalset_path}")


if __name__ == "__main__":
    main()
