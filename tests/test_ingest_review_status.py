"""Tests for scripts/ingest_review_status.py (spec §2.4, PR 3 Task 4).

Synthetic evalsets + annot files in tmp_path only — never the real
evalsets/evalset_answer_02.json. No live model/service calls.
"""

from __future__ import annotations

import copy
import json
import subprocess
import sys
from datetime import date
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from scripts.ingest_review_status import ingest  # noqa: E402

SCRIPT = REPO_ROOT / "scripts" / "ingest_review_status.py"
EVALSET_NAME = "evalset_test_evalset"


def _annot(qid, reviewer, passages=(), answer=None, validity=None):
    """Annot payload per the review-evalset-answer.py contract.

    passages: iterable of (chunk_id, label) or (chunk_id, label, notes).
    """
    return {
        "query_id": qid,
        "question": f"q {qid}",
        "reviewer": reviewer,
        "reviewed_passages": [
            {
                "chunk_id": c,
                "doc_id": "d",
                "label": lab,
                "notes": notes,
                "timestamp": "2026-09-04",
            }
            for c, lab, *rest in passages
            for notes in [rest[0] if rest else ""]
        ],
        "synthesis_review": answer
        and {"label": answer, "notes": "", "timestamp": "2026-09-04"},
        "negative_case_review": validity
        and {"label": validity, "notes": "", "timestamp": "2026-09-04"},
    }


def _evalset():
    """2 positive cases (2 passages each) + 1 negative case."""
    return {
        "name": EVALSET_NAME,
        "version": "3",
        "created": "2026-09-01",
        "updated": "2026-09-01",
        "description": "synthetic",
        "test_cases": [
            {
                "id": "q1_alpha",
                "question": "Q1?",
                "retrieval_ground_truth": {
                    "expected_external_ids": ["doc_a"],
                    "expected_passages": [
                        {
                            "doc_id": "doc_a",
                            "chunk_id": "a_chunk_1",
                            "text_snippet": "s1",
                            "supports_key_fact": "fact one text",
                        },
                        {
                            "doc_id": "doc_a",
                            "chunk_id": "a_chunk_2",
                            "text_snippet": "s2",
                            "supports_key_fact": "fact two text",
                        },
                    ],
                },
                "synthesis_ground_truth": {
                    "canonical_answer": "A1",
                    "key_facts": ["fact one text", "fact two text"],
                },
            },
            {
                "id": "q2_beta",
                "question": "Q2?",
                "retrieval_ground_truth": {
                    "expected_external_ids": ["doc_b"],
                    "expected_passages": [
                        {
                            "doc_id": "doc_b",
                            "chunk_id": "b_chunk_1",
                            "text_snippet": "t1",
                            "supports_key_fact": "fact three text",
                        },
                        {
                            "doc_id": "doc_b",
                            "chunk_id": "b_chunk_2",
                            "text_snippet": "t2",
                            "supports_key_fact": "fact four text",
                        },
                    ],
                },
                "synthesis_ground_truth": {
                    "canonical_answer": "A2",
                    "key_facts": ["fact three text", "fact four text"],
                },
            },
            {
                "id": "q3_negative",
                "question": "Q3?",
                "retrieval_ground_truth": {"expected_external_ids": []},
                "synthesis_ground_truth": {"key_facts": []},
            },
        ],
        "twins": [],
    }


def _markers(case):
    """The case's [review ...] marker lines."""
    note = case.get("note") or ""
    return [ln for ln in note.split("\n") if ln.startswith("[review ")]


def _write_annot(dir_path: Path, annot: dict, filename: str | None = None) -> Path:
    name = (
        filename
        or f"annot-{EVALSET_NAME}-{annot['query_id']}-by-{annot['reviewer']}.json"
    )
    p = dir_path / name
    p.write_text(json.dumps(annot, ensure_ascii=False, indent=2), encoding="utf-8")
    return p


# --- 1. all-yes single reviewer -> expert_approved ---------------------------


def test_all_yes_single_reviewer_approves():
    es = _evalset()
    annots = [
        _annot("q1_alpha", "fenris", [("a_chunk_1", "yes"), ("a_chunk_2", "yes")], answer="yes")
    ]
    new_es, report = ingest(es, annots)
    case = new_es["test_cases"][0]
    assert case["review_status"] == "expert_approved"
    assert _markers(case) == []
    assert case["retrieval_ground_truth"]["expected_passages"] == (
        es["test_cases"][0]["retrieval_ground_truth"]["expected_passages"]
    )
    assert any("q1_alpha" in ln for ln in report)


# --- 2. one passage no -> dropped + fact flagged -----------------------------


def test_passage_no_drops_and_flags_fact():
    es = _evalset()
    annots = [
        _annot("q1_alpha", "fenris", [("a_chunk_1", "no"), ("a_chunk_2", "yes")], answer="yes")
    ]
    new_es, _ = ingest(es, annots)
    case = new_es["test_cases"][0]
    ids = [p["chunk_id"] for p in case["retrieval_ground_truth"]["expected_passages"]]
    assert "a_chunk_1" not in ids
    assert "a_chunk_2" in ids
    assert case["review_status"] == "draft"
    markers = _markers(case)
    assert len(markers) == 1
    assert markers[0].startswith("[review ")
    assert "a_chunk_1" in markers[0]
    assert "fact one text" in markers[0]


# --- 3. canonical answer no -> draft + marker quoting the note ---------------


def test_answer_no_blocks_with_note():
    es = _evalset()
    annots = [
        _annot("q1_alpha", "fenris", [("a_chunk_1", "yes"), ("a_chunk_2", "yes")], answer="no")
    ]
    annots[0]["synthesis_review"]["notes"] = "answer misses the 54% figure"
    new_es, _ = ingest(es, annots)
    case = new_es["test_cases"][0]
    assert case["review_status"] == "draft"
    markers = _markers(case)
    assert len(markers) == 1
    assert "canonical answer labeled no" in markers[0]
    assert "answer misses the 54% figure" in markers[0]


# --- 4. conflicting reviewers -> draft, both listed --------------------------


def test_conflicting_reviewers_leave_draft():
    es = _evalset()
    annots = [
        _annot("q1_alpha", "fenris", [("a_chunk_1", "yes"), ("a_chunk_2", "yes")], answer="yes"),
        _annot("q1_alpha", "mlabel", [("a_chunk_1", "no"), ("a_chunk_2", "yes")], answer="yes"),
    ]
    new_es, report = ingest(es, annots)
    case = new_es["test_cases"][0]
    assert case["review_status"] == "draft"
    markers = _markers(case)
    # drop marker (from mlabel's no) + conflict marker naming both reviewers
    drop = [m for m in markers if "a_chunk_1" in m and "dropped" in m]
    conflict = [m for m in markers if "conflicting labels on passage a_chunk_1" in m]
    assert len(drop) == 1 and "r=mlabel" in drop[0]
    assert len(conflict) == 1
    assert "fenris=yes" in conflict[0] and "mlabel=no" in conflict[0]
    # the CLI report carries the same conflict detail (case id + labels)
    conflict_report = [ln for ln in report if "conflicting labels on passage a_chunk_1" in ln]
    assert len(conflict_report) == 1
    assert conflict_report[0].startswith("case q1_alpha:")
    assert "fenris=yes" in conflict_report[0] and "mlabel=no" in conflict_report[0]


# --- 4b. answer/validity conflict -> draft, conflict in the report ------------


def test_answer_conflict_reported_in_report_lines():
    es = _evalset()
    annots = [
        _annot("q1_alpha", "fenris", [("a_chunk_1", "yes"), ("a_chunk_2", "yes")], answer="no"),
        _annot("q1_alpha", "mlabel", [("a_chunk_1", "yes"), ("a_chunk_2", "yes")], answer="yes"),
    ]
    new_es, report = ingest(es, annots)
    case = new_es["test_cases"][0]
    assert case["review_status"] == "draft"
    conflict_report = [ln for ln in report if "conflicting labels on canonical answer" in ln]
    assert len(conflict_report) == 1
    assert conflict_report[0].startswith("case q1_alpha:")
    assert "fenris=no" in conflict_report[0] and "mlabel=yes" in conflict_report[0]


def test_validity_conflict_reported_in_report_lines():
    es = _evalset()
    annots = [
        _annot("q3_negative", "fenris", validity="no"),
        _annot("q3_negative", "mlabel", validity="yes"),
    ]
    new_es, report = ingest(es, annots)
    case = new_es["test_cases"][2]
    assert case["review_status"] == "draft"
    conflict_report = [ln for ln in report if "conflicting labels on negative-case validity" in ln]
    assert len(conflict_report) == 1
    assert conflict_report[0].startswith("case q3_negative:")
    assert "fenris=no" in conflict_report[0] and "mlabel=yes" in conflict_report[0]


# --- 5. skip is silent: no drop, no conflict, blocks approval ----------------


def test_skip_is_silent_but_blocks():
    es = _evalset()
    annots = [
        _annot("q1_alpha", "fenris", [("a_chunk_1", "skip"), ("a_chunk_2", "yes")], answer="yes")
    ]
    new_es, _ = ingest(es, annots)
    case = new_es["test_cases"][0]
    assert case["review_status"] == "draft"
    ids = [p["chunk_id"] for p in case["retrieval_ground_truth"]["expected_passages"]]
    assert ids == ["a_chunk_1", "a_chunk_2"]  # no drop
    assert _markers(case) == []  # no markers at all


# --- 6. partial labeling -> not approved -------------------------------------


def test_partial_labeling_not_approved():
    es = _evalset()
    annots = [_annot("q1_alpha", "fenris", [("a_chunk_1", "yes")], answer="yes")]
    new_es, _ = ingest(es, annots)
    case = new_es["test_cases"][0]
    assert case["review_status"] == "draft"


# --- 7. negative case validity ------------------------------------------------


def test_negative_case_validity_yes_approves():
    es = _evalset()
    annots = [_annot("q3_negative", "fenris", validity="yes")]
    new_es, _ = ingest(es, annots)
    case = new_es["test_cases"][2]
    assert case["review_status"] == "expert_approved"


def test_negative_case_validity_no_blocks_with_marker():
    es = _evalset()
    annots = [_annot("q3_negative", "fenris", validity="no")]
    annots[0]["negative_case_review"]["notes"] = "this is answerable from doc_a"
    new_es, _ = ingest(es, annots)
    case = new_es["test_cases"][2]
    assert case["review_status"] == "draft"
    markers = _markers(case)
    assert len(markers) == 1
    assert "negative-case validity labeled no" in markers[0]
    assert "this is answerable from doc_a" in markers[0]


# --- 8. idempotency: same-day re-run over the same annot set is byte-identical


def test_idempotent_same_day_rerun():
    es = _evalset()
    annots = [
        _annot("q1_alpha", "fenris", [("a_chunk_1", "yes"), ("a_chunk_2", "yes")], answer="yes"),
        _annot("q2_beta", "mlabel", [("b_chunk_1", "no"), ("b_chunk_2", "yes")], answer="yes"),
    ]
    once, _ = ingest(es, annots)
    twice, _ = ingest(once, annots)
    assert json.dumps(twice, ensure_ascii=False, indent=2) == json.dumps(
        once, ensure_ascii=False, indent=2
    )
    # markers regenerated, not appended
    assert len(_markers(twice["test_cases"][1])) == 1


# --- 9. re-ingest after a drop: already-dropped chunk stays a no-op block -----


def test_reingest_after_drop_is_byte_identical():
    es = _evalset()
    annots = [
        _annot("q2_beta", "mlabel", [("b_chunk_1", "no"), ("b_chunk_2", "yes")], answer="yes")
    ]
    # simulate the state left by an earlier ingest run: chunk already gone,
    # its drop marker already in the note
    already_dropped = copy.deepcopy(es)
    ps = already_dropped["test_cases"][1]["retrieval_ground_truth"]["expected_passages"]
    already_dropped["test_cases"][1]["retrieval_ground_truth"]["expected_passages"] = [
        p for p in ps if p["chunk_id"] != "b_chunk_1"
    ]
    already_dropped["test_cases"][1]["note"] = (
        "[review 2026-09-04 r=mlabel] passage b_chunk_1 dropped (labeled no); "
        "fact needs re-sourcing: fact three text"
    )
    once, _ = ingest(already_dropped, annots)
    assert once["test_cases"][1]["review_status"] == "draft"
    twice, _ = ingest(once, annots)
    assert json.dumps(once, ensure_ascii=False, indent=2) == json.dumps(
        twice, ensure_ascii=False, indent=2
    )
    # content-dedup: no second reduced marker despite the no-vote reappearing
    assert len(_markers(twice["test_cases"][1])) == 1


def test_already_dropped_no_marker_present_gets_reduced_marker():
    es = _evalset()
    ps = es["test_cases"][1]["retrieval_ground_truth"]["expected_passages"]
    es["test_cases"][1]["retrieval_ground_truth"]["expected_passages"] = [
        p for p in ps if p["chunk_id"] != "b_chunk_1"
    ]
    annots = [_annot("q2_beta", "mlabel", [("b_chunk_1", "no"), ("b_chunk_2", "yes")])]
    new_es, _ = ingest(es, annots)
    case = new_es["test_cases"][1]
    assert case["review_status"] == "draft"
    markers = _markers(case)
    assert markers == [
        "[review 2026-09-04 r=mlabel] passage b_chunk_1 labeled no "
        "(already dropped; fact unknown)"
    ]


# --- 10/11. bad input raises with the file name -------------------------------


def test_unknown_query_id_raises_with_file_name():
    es = _evalset()
    annots = [_annot("qX_missing", "fenris")]
    annots[0]["_annot_file"] = "annot-test_evalset-qX_missing-by-fenris.json"
    with pytest.raises(ValueError) as exc:
        ingest(es, annots)
    assert "annot-test_evalset-qX_missing-by-fenris.json" in str(exc.value)


def test_invalid_label_raises_with_file_name():
    es = _evalset()
    annots = [_annot("q1_alpha", "fenris", [("a_chunk_1", "maybe")])]
    annots[0]["_annot_file"] = "annot-test_evalset-q1_alpha-by-fenris.json"
    with pytest.raises(ValueError) as exc:
        ingest(es, annots)
    assert "annot-test_evalset-q1_alpha-by-fenris.json" in str(exc.value)
    assert "maybe" in str(exc.value)


# --- 12. updated set to today, version untouched ------------------------------


def test_updated_set_version_untouched():
    es = _evalset()
    annots = [_annot("q1_alpha", "fenris", [("a_chunk_1", "yes"), ("a_chunk_2", "yes")], answer="yes")]
    new_es, _ = ingest(es, annots)
    assert new_es["updated"] == date.today().isoformat()
    assert new_es["version"] == es["version"] == "3"


# --- 13. case with no annots -> completely untouched --------------------------


def test_case_without_annots_untouched():
    es = _evalset()
    annots = [_annot("q1_alpha", "fenris", [("a_chunk_1", "yes"), ("a_chunk_2", "yes")], answer="yes")]
    new_es, _ = ingest(es, annots)
    untouched = new_es["test_cases"][1]
    original = es["test_cases"][1]
    assert "review_status" not in untouched
    assert untouched == original
    assert "review_status" not in new_es["test_cases"][2]
    # input not mutated
    assert es["updated"] == "2026-09-01"


# --- CLI wrapper ---------------------------------------------------------------


def test_cli_empty_annot_dir_leaves_evalset_byte_identical(tmp_path):
    es_path = tmp_path / "evalset_test_evalset.json"
    es_path.write_text(json.dumps(_evalset(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    before = es_path.read_bytes()
    annot_dir = tmp_path / "review-output"
    annot_dir.mkdir()
    proc = subprocess.run(
        [sys.executable, str(SCRIPT), "--evalset", str(es_path), "--annot", str(annot_dir)],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )
    assert proc.returncode == 0, proc.stderr
    assert "no annot files found" in proc.stdout
    assert es_path.read_bytes() == before


def test_cli_ingests_and_writes_back(tmp_path):
    es_path = tmp_path / "evalset_test_evalset.json"
    es_path.write_text(json.dumps(_evalset(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    annot_dir = tmp_path / "review-output"
    annot_dir.mkdir()
    _write_annot(
        annot_dir,
        _annot("q1_alpha", "fenris", [("a_chunk_1", "yes"), ("a_chunk_2", "yes")], answer="yes"),
    )
    proc = subprocess.run(
        [sys.executable, str(SCRIPT), "--evalset", str(es_path), "--annot", str(annot_dir)],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )
    assert proc.returncode == 0, proc.stderr
    written = json.loads(es_path.read_text(encoding="utf-8"))
    assert written["test_cases"][0]["review_status"] == "expert_approved"
    # dry-run leaves the file alone but still prints the report
    es_path.write_text(json.dumps(_evalset(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    proc = subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--evalset",
            str(es_path),
            "--annot",
            str(annot_dir),
            "--dry-run",
        ],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )
    assert proc.returncode == 0, proc.stderr
    dry = json.loads(es_path.read_text(encoding="utf-8"))
    assert "review_status" not in dry["test_cases"][0]
