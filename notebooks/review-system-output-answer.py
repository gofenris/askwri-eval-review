# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo",
#     "molabel==0.1.5",
#     "mohtml==0.1.11",
#     "pandas==3.0.5",
#     "httpx==0.28.1",
#     "anywidget==0.11.0",
#     "traitlets==5.16.1",
#     "pyyaml==6.0.3",
# ]
# ///

import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # ANSWER-mode system-output review (mode 2)

    Judge calibration: review the *stored system outputs* produced by the
    answer-eval harness against the human-labeled evalset (spec §4.5). Each
    capture file holds, per case and pass, the retrieved passages that were
    sent to the model, the synthesized sentences, and their citations. You
    label each key fact (stated / partial / absent) and each sentence
    (supported / unsupported); the labels are the ground truth the LLM judge
    is calibrated against.

    **How to get a capture file:** the maintainer shares
    `evaluation/answer/artifacts/capture-<label>.json` (produced by the
    harness's capture stage). Upload it below — labels are written to
    `review-output/` as
    `labels-<capture-label>-<case_id>-pass<N>-by-<reviewer>.json` with schema
    `answer-eval/human-labels@1`, and POSTed to the shared review dashboard.
    """)
    return


@app.cell
def _():
    import hashlib
    import json
    import re

    import httpx
    import marimo as mo
    from mohtml import div, p, span

    return div, hashlib, httpx, json, mo, p, re, span


@app.cell
def _(mo):
    REPO_ROOT = mo.notebook_dir().parent

    REVIEW_OUTPUT_DIR = REPO_ROOT / "review-output"
    return REPO_ROOT, REVIEW_OUTPUT_DIR


@app.cell
def _():
    # Same Apps Script Web App / Drive folder / Sheet deployment used by
    # review_expected_docs-cite.py -- see TECH_INFO.md "Submitting notebook
    # output to a filedrop you own" for how this was set up, and how to
    # rotate/replace it. Treat this URL as security-through-obscurity: fine
    # for a short-lived, low-stakes review period; revoke the deployment in
    # Apps Script when the review period ends.
    SUBMIT_ENDPOINT_URL = "https://script.google.com/macros/s/AKfycbxNoFNUBXJkYEQK_m2yNeNMilhEqh22bXxbFjiWeZA03JCKxayTTScht2938U3mVakO/exec"
    return (SUBMIT_ENDPOINT_URL,)


@app.cell
def _(SUBMIT_ENDPOINT_URL, httpx, json):
    def submit_to_review_dashboard(filename, payload):
        """Best-effort POST of a saved review file to the shared dashboard.

        Never raises -- returns (success, error_message) so callers can
        surface a warning without blocking the (already-successful) local
        save.

        Sends Content-Type: text/plain (not the default application/json)
        so the request stays a CORS "simple request". Browsers (e.g. molab's
        WASM/Pyodide runtime) otherwise send a preflight OPTIONS request
        first, which this Apps Script endpoint doesn't answer with the
        required CORS headers, causing a NetworkError. Apps Script's doPost
        reads the raw request body regardless of Content-Type, so this
        doesn't change what the server receives.
        """
        try:
            httpx.post(
                SUBMIT_ENDPOINT_URL,
                content=json.dumps({"filename": filename, "content": json.dumps(payload, indent=2)}),
                headers={"Content-Type": "text/plain;charset=utf-8"},
                timeout=10,
            )
            return True, None
        except Exception as e:
            return False, str(e)


    return (submit_to_review_dashboard,)


@app.cell(hide_code=True)
def _(hashlib, json):
    # Python mirror of the harness's captureFingerprint (judge.ts):
    #   createHash('sha256').update(JSON.stringify(capture.cases)).digest('hex')
    # JSON.stringify is compact (no spaces) and emits non-ASCII raw, hence
    # separators=(",", ":") and ensure_ascii=False. Pinned cross-language by
    # tests/test_capture_fingerprint.py.
    def mirror(capture: dict) -> str:
        cases = capture["cases"]
        return hashlib.sha256(
            json.dumps(cases, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
        ).hexdigest()


    return (mirror,)


@app.cell
def _(mo):
    capture_file = mo.ui.file(
        filetypes=[".json"],
        kind="area",
        label="Upload a capture-<label>.json",
    )
    capture_file
    return (capture_file,)


@app.cell
def _(capture_file, json, mirror, mo, re):
    capture_state = {}

    mo.stop(
        not capture_file.value,
        mo.md("⬆️ Upload a `capture-<label>.json` file above to begin."),
    )

    _upload = capture_file.value[0]
    _capture = json.loads(_upload.contents.decode("utf-8"))

    mo.stop(
        _capture.get("schema") != "answer-eval/capture@1",
        mo.callout(
            mo.md(
                f"Expected schema `answer-eval/capture@1`, but the uploaded file "
                f"declares `{_capture.get('schema')!r}`. Not a harness capture artifact."
            ),
            kind="danger",
        ),
    )

    capture_state = {
        "capture": _capture,
        "name": _upload.name,
        # e.g. "capture-q1-retry.json" -> "q1-retry"
        "label": re.sub(r"^capture-", "", _upload.name).removesuffix(".json"),
        "fingerprint": mirror(_capture),
        "provenance": _capture.get("provenance", {}),
    }
    return (capture_state,)


@app.cell
def _(capture_state, mo):
    mo.stop(
        not capture_state.get("capture"),
        mo.md("⬆️ Upload a `capture-<label>.json` file above to begin."),
    )

    _prov = capture_state["provenance"]
    _cases = capture_state["capture"]["cases"]
    _synthesis_model = (_prov.get("synthesis") or {}).get("model", "—")
    _passes = _prov.get("passes", "—")
    _target_urls = ", ".join((_prov.get("target") or {}).get("urls", []) or ["—"])

    mo.vstack([
        mo.md(f"""
    **Capture loaded:** `{capture_state["name"]}` (label `{capture_state["label"]}`)

    | | |
    | --- | --- |
    | cases | {len(_cases)} |
    | passes | {_passes} |
    | synthesis model | `{_synthesis_model}` |
    | target | {_target_urls} |
    | capture fingerprint | `{capture_state["fingerprint"][:16]}…` |
    """),
    ])
    return


@app.cell
def _(capture_state, mo):
    mo.stop(
        not capture_state.get("capture"),
        mo.md("⬆️ Upload a `capture-<label>.json` file above to begin."),
    )

    _capture = capture_state["capture"]

    case_dropdown = mo.ui.dropdown(
        options={c["fixture_case"]["question"]: c for c in _capture["cases"]},
        value=_capture["cases"][0]["fixture_case"]["question"],
        label="Select a case to review",
    )
    case_dropdown
    return (case_dropdown,)


@app.cell(hide_code=True)
def _(mo):
    reviewer_name_input = mo.ui.text(label="Reviewer name", value="reviewer", placeholder="reviewer")
    mo.vstack([
        mo.hstack(
        [reviewer_name_input], justify="start", gap=1),
        mo.md("*Providing your name is optional -- it helps us track reviews and reach out if we have any questions.*")
    ])
    return (reviewer_name_input,)


@app.cell(hide_code=True)
def _():
    saved_label_paths = set()
    dirty_keys = set()  # (case_id, pass) with unsaved verdicts
    last_selected_case_id_box = [None]
    return dirty_keys, last_selected_case_id_box, saved_label_paths


@app.cell(hide_code=True)
def _(case_dropdown, dirty_keys, last_selected_case_id_box, mo):
    _prev_case_id = last_selected_case_id_box[0]
    selected_case = case_dropdown.value

    _switch_warning = None
    if (
        _prev_case_id is not None
        and _prev_case_id != selected_case["case_id"]
        and _prev_case_id in dirty_keys
    ):
        _switch_warning = mo.md(
            f"⚠️ **Unsaved labels lost**: you switched away from case "
            f"`{_prev_case_id}` without clicking Save. Those labels were not saved."
        ).callout(kind="danger")
        for _k in [k for k in dirty_keys if k[0] == _prev_case_id]:
            dirty_keys.discard(_k)

    last_selected_case_id_box[0] = selected_case["case_id"]

    _fixture = selected_case["fixture_case"]
    _review_status = _fixture.get("review_status")

    _case_info = mo.md(f"""

    **Selected case:** "{_fixture["question"]}"

    **id:** `{selected_case["case_id"]}`&nbsp;&nbsp;|&nbsp;&nbsp;
    **review_status:** `{_review_status if _review_status else "—"}`

    {f"**note:** {_fixture['note']}" if _fixture.get("note") else ""}
    """)

    mo.vstack([_switch_warning, _case_info]) if _switch_warning else _case_info
    return (selected_case,)


@app.cell(hide_code=True)
def _(mo, selected_case):
    pass_radio = mo.ui.radio(
        options={f"pass {_i}": _i for _i in range(len(selected_case["passes"]))},
        value="pass 0",
        label="Pass",
    )
    pass_radio
    return (pass_radio,)


@app.cell(hide_code=True)
def _(div, p, span):
    def render_reference_passage_card(ps):
        _badge_style = (
            "background:#f1f3f5; color:#495057; border-radius:999px; "
            "padding:0.15rem 0.6rem; font-size:0.75rem; font-weight:500;"
        )
        _text_style = (
            "font-size:0.95rem; color:#333; line-height:1.6; margin:0.4rem 0 0.9rem 0; "
            "padding:0.6rem 0.8rem; background:#f8f9fa; border-radius:6px; max-width:65ch;"
        )
        return str(
            div(
                div(
                    span(f"id {ps['id']}", style=_badge_style),
                    span(ps["doc_id"], style=_badge_style),
                    span(f"page {ps['page']}", style=_badge_style),
                    style="display:flex; gap:0.4rem; flex-wrap:wrap;",
                ),
                p(ps["text"], style=_text_style),
            )
        )

    return (render_reference_passage_card,)


@app.cell(hide_code=True)
def _(mo, pass_radio, render_reference_passage_card, selected_case):
    _fixture = selected_case["fixture_case"]
    _key_facts = (_fixture.get("synthesis_ground_truth") or {}).get("key_facts") or []
    KEY_FACTS = list(_key_facts)
    selected_passage = selected_case["passes"][pass_radio.value]

    _facts_md = "\n".join(f"{_i + 1}. {_fact}" for _i, _fact in enumerate(KEY_FACTS)) or "—"
    _review_status = _fixture.get("review_status")

    mo.vstack([
        mo.md(f"""
    ### Context

    **Question:** {_fixture["question"]}

    **key_facts** (label each below):

    {_facts_md}

    {f"**review_status:** `{_review_status}`" if _review_status else ""}
    """),
        mo.md("**Passages sent to the model for this pass** (reference only):"),
        mo.Html("".join(render_reference_passage_card(ps) for ps in selected_passage["answer"]["passages_sent"])),
    ])
    return KEY_FACTS, selected_passage


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Fact verdicts

    For each key fact: is it stated in the synthesized answer (`stated`),
    partially stated (`partial`), or missing (`absent`)? An evidence quote is
    optional but encouraged for `partial`.
    """)
    return


@app.cell(hide_code=True)
def _(KEY_FACTS, mo):
    fact_widgets = [
        (
            mo.ui.radio(
                options=["stated", "partial", "absent"],
                label=f"Fact {_i}",
                inline=True,
            ),
            mo.ui.text_area(label="evidence quote (optional)"),
        )
        for _i, _fact in enumerate(KEY_FACTS)
    ]

    mo.vstack([
        _el
        for _i, (_fact, (_radio, _evidence)) in enumerate(zip(KEY_FACTS, fact_widgets))
        for _el in (
            mo.md(f"**Fact {_i}:** {_fact}"),
            _radio,
            _evidence,
        )
    ])
    return (fact_widgets,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Sentence verdicts

    For each synthesized sentence: is it supported by the passages it cites?
    Sentences with no citations must be judged against ALL retrieved passages
    shown above.
    """)
    return


@app.cell(hide_code=True)
def _(mo, selected_passage):
    _answer = selected_passage["answer"]
    _sentences = _answer["sentences"]
    _cites = _answer["cites"]
    _passages_by_id = {ps["id"]: ps for ps in _answer["passages_sent"]}

    def _cited_label(_i):
        _ids = _cites[_i] if _i < len(_cites) else []
        _cited = [_passages_by_id[_j] for _j in _ids if _j in _passages_by_id]
        if not _cited:
            return "no citations — judge against ALL retrieved passages above"
        return " · ".join(
            f"[{ps['id']}] {ps['doc_id']} p.{ps['page']}: {ps['text'][:120]}…" for ps in _cited
        )

    sentence_widgets = [
        (
            mo.ui.radio(options=["supported", "unsupported"], label=f"Sentence {_i}", inline=True),
            mo.ui.text_area(label="note (optional)"),
        )
        for _i in range(len(_sentences))
    ]

    mo.vstack([
        _el
        for _i, (_sent, (_radio, _note)) in enumerate(zip(_sentences, sentence_widgets))
        for _el in (
            mo.md(f"**Sentence {_i}:** {_sent}"),
            mo.md(f"_{_cited_label(_i)}_"),
            _radio,
            _note,
        )
    ])
    return (sentence_widgets,)


@app.cell(hide_code=True)
def _(dirty_keys, fact_widgets, pass_radio, selected_case, sentence_widgets):
    _fact_touched = any(
        _radio.value is not None or _evidence.value
        for _radio, _evidence in fact_widgets
    )
    _sentence_touched = any(
        _radio.value is not None or _note.value
        for _radio, _note in sentence_widgets
    )
    if _fact_touched or _sentence_touched:
        dirty_keys.add((selected_case["case_id"], pass_radio.value))
    return


@app.cell(hide_code=True)
def _(mo):
    overall_note_input = mo.ui.text_area(label="overall note (optional)")
    overall_note_input
    return (overall_note_input,)


@app.cell(hide_code=True)
def _(mo):
    save_button = mo.ui.run_button(label="Save", tooltip="Click to Save")
    save_button
    return (save_button,)


@app.cell(hide_code=True)
def _(
    KEY_FACTS,
    REVIEW_OUTPUT_DIR,
    REPO_ROOT,
    capture_state,
    dirty_keys,
    fact_widgets,
    json,
    mo,
    overall_note_input,
    pass_radio,
    re,
    reviewer_name_input,
    save_button,
    saved_label_paths,
    selected_case,
    sentence_widgets,
    submit_to_review_dashboard,
):
    mo.stop(not save_button.value, mo.md("**Saved Results**: None. <br>_Click the button above to save your labels for this case._"))

    _reviewer = re.sub(r"[^\w\-]+", "_", reviewer_name_input.value.strip()) or "reviewer"

    _missing = [
        f"Fact {_i}"
        for _i, (_radio, _evidence) in enumerate(fact_widgets)
        if _radio.value is None
    ] + [
        f"Sentence {_i}"
        for _i, (_radio, _note) in enumerate(sentence_widgets)
        if _radio.value is None
    ]

    _out = None
    if _missing:
        _out = mo.callout(
            mo.md(
                "⚠️ **Not saved** — every fact and every sentence needs a verdict. "
                f"Still missing: {', '.join(_missing)}."
            ),
            kind="danger",
        )
    else:
        _payload = {
            "schema": "answer-eval/human-labels@1",
            "capture_file": capture_state["name"],
            "capture_fingerprint": capture_state["fingerprint"],
            "case_id": selected_case["case_id"],
            "pass": pass_radio.value,
            "reviewer": _reviewer,
            "question": selected_case["fixture_case"]["question"],
            "key_facts": KEY_FACTS,
            "fact_verdicts": [
                {
                    "fact_index": _i,
                    "verdict": _radio.value,
                    **({"evidence": _evidence.value} if _evidence.value else {}),
                }
                for _i, (_radio, _evidence) in enumerate(fact_widgets)
            ],
            "sentence_verdicts": [
                {
                    "sentence_index": _i,
                    "verdict": _radio.value,
                    **({"note": _note.value} if _note.value else {}),
                }
                for _i, (_radio, _note) in enumerate(sentence_widgets)
            ],
        }
        if overall_note_input.value.strip():
            _payload["overall_note"] = overall_note_input.value.strip()

        _filename = (
            f"labels-{capture_state['label']}-{selected_case['case_id']}"
            f"-pass{pass_radio.value}-by-{_reviewer}.json"
        )

        REVIEW_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        _labels_path = REVIEW_OUTPUT_DIR / _filename
        _labels_path.write_text(json.dumps(_payload, ensure_ascii=False, indent=2))
        saved_label_paths.add(_labels_path)
        dirty_keys.discard((selected_case["case_id"], pass_radio.value))

        _submitted, _submit_error = submit_to_review_dashboard(_filename, _payload)

        _submit_status = (
            "✅ Submitted to the shared review dashboard."
            if _submitted
            else f"⚠️ Saved locally, but submitting to the review dashboard failed: `{_submit_error}`"
        )

        _out = mo.md(f"""
    Saved!

    Labels file:
    `{_labels_path.relative_to(REPO_ROOT)}`

    Facts labeled: {len(_payload["fact_verdicts"])} · Sentences labeled: {len(_payload["sentence_verdicts"])}

    {_submit_status}
    """)
    _out
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Track progress in this session

    A (case, pass) pair is marked done once its labels have been saved. If
    you close and reopen the notebook, this section will refresh.
    """)
    return


@app.cell(hide_code=True)
def _(
    capture_state,
    div,
    json,
    mo,
    save_button,
    saved_label_paths,
):
    _ = save_button.value  # dependency: refresh whenever Save is clicked

    mo.stop(
        not capture_state.get("capture"),
        mo.md("⬆️ Upload a `capture-<label>.json` file above to begin."),
    )

    _reviewed_keys = set()
    for _path in sorted(saved_label_paths):
        _data = json.loads(_path.read_text())
        _reviewed_keys.add((_data["case_id"], _data["pass"]))

    _all_keys = [
        (_c["case_id"], _p)
        for _c in capture_state["capture"]["cases"]
        for _p in range(len(_c["passes"]))
    ]
    total_keys = len(_all_keys)
    total_done = len(_reviewed_keys & set(_all_keys))

    _label_by_key = {(_c["case_id"], _p): _c["fixture_case"]["question"] for _c in capture_state["capture"]["cases"] for _p in range(len(_c["passes"]))}

    def _chip(key):
        _cid, _p = key
        _done = key in _reviewed_keys
        return div(
            f"{_cid}·pass{_p}", " ", "✅" if _done else "⬜",
            title=_label_by_key.get(key, ""),
            style=(
                "display:inline-flex; align-items:center; justify-content:center; gap:0.3rem; "
                "padding:0.4rem 0.75rem; border-radius:8px; "
                "font-size:0.9rem; font-weight:600; "
                + ("background:#d4edda; color:#155724;" if _done else "background:#f1f3f5; color:#495057;")
            ),
        )


    checklist_html = str(div(
        *[_chip(key) for key in _all_keys],
        style="display:grid; grid-template-columns:repeat(6, auto); gap:0.4rem; margin-top:0.75rem;",
    ))

    mo.vstack([
        mo.hstack(
            [
                mo.stat(value=total_keys, label="Total (case, pass) pairs", bordered=True),
                mo.stat(value=total_done, label="Labeled and saved", bordered=True),
            ],
            gap=2,
        ),
        mo.Html(checklist_html),
    ])
    return


if __name__ == "__main__":
    app.run()
