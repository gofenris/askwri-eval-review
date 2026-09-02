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
    # ANSWER-mode eval review

    Review the evalset for AskWRI Answer mode.

    For each query, step through its `expected_passages` (retrieved
    chunks) and confirm whether each one actually supports the stated key
    fact, then review the synthesized `canonical_answer` as a whole.
    """)
    return


@app.cell
def _():
    import json
    import re

    import httpx
    import yaml
    import marimo as mo
    from molabel import SimpleLabel
    from mohtml import div, p, span

    import pandas as pd

    return SimpleLabel, div, httpx, json, mo, p, pd, re, span, yaml


@app.cell
def _(mo):
    REPO_ROOT = mo.notebook_dir().parent

    EVALSET_DIR = REPO_ROOT / "evalsets"
    MARKDOWN_DIR = REPO_ROOT / "kp-docs" / "markdown"
    REVIEW_OUTPUT_DIR = REPO_ROOT / "review-output"
    return EVALSET_DIR, MARKDOWN_DIR, REPO_ROOT, REVIEW_OUTPUT_DIR


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
def _(EVALSET_DIR):
    # Get available evalsets

    # remove bkup sets
    eval_set_list = [e for e in sorted(EVALSET_DIR.iterdir()) if "bkup" not in e.name.lower()]

    # filter to "answer" mode evalsets only
    eval_set_list = [e for e in eval_set_list if "answer" in e.name.lower()]
    return (eval_set_list,)


@app.cell(hide_code=True)
def _(mo):
    reviewer_name_input = mo.ui.text(label="Reviewer name", value="reviewer", placeholder="reviewer")
    mo.vstack([
        mo.hstack(
        [reviewer_name_input], justify="start", gap=1),
        mo.md("*Providing your name is optional -- it helps us track reviews and reach out if we have any questions.*")
    ])
    return (reviewer_name_input,)


@app.cell
def _(eval_set_list, mo):
    # Select evalset from available options
    evalset_names = [e.name for e in eval_set_list]
    default_idx = evalset_names.index("evalset_answer_02.json") if "evalset_answer_02.json" in evalset_names else 0

    evalset_dropdown = mo.ui.dropdown(
        options=evalset_names,
        value=evalset_names[default_idx],
        label="Select Evaluation Set:"
    )

    mo.vstack([
        mo.md("**Select an evaluation set**"),
        evalset_dropdown
    ])
    return (evalset_dropdown,)


@app.cell(hide_code=True)
def _(EVALSET_DIR, evalset_dropdown):
    # Derive the paths from the selected dropdown value
    SELECTED_EVALSET_PATH = EVALSET_DIR / evalset_dropdown.value
    EVALSET_NAME = SELECTED_EVALSET_PATH.stem
    return EVALSET_NAME, SELECTED_EVALSET_PATH


@app.cell
def _(SELECTED_EVALSET_PATH, json):
    evalset = json.loads(SELECTED_EVALSET_PATH.read_text())
    test_cases = evalset["test_cases"]
    return evalset, test_cases


@app.cell(hide_code=True)
def _(EVALSET_NAME, evalset, test_cases):
    print(f"Selected Evalset: `{EVALSET_NAME}`")
    print(f"---")
    for _f in ['name', 'version', 'created', 'updated']:
        print (f"{_f:<20} : {evalset.get(_f)}")
    print(f"Number of test cases : {len(test_cases)}")
    print(f"---")
    print(f"Description: \n{evalset.get("description", "—")}")
    return


@app.cell(hide_code=True)
def _(pd, test_cases):
    _query_type_counts = pd.Series([tc["query_type"] for tc in test_cases]).value_counts()
    _difficulty_counts = pd.Series([tc["difficulty"] for tc in test_cases]).value_counts()

    def _counts_to_md_table(_counts, _label):
        _rows = "\n".join(f"| {_k} | {_v} |" for _k, _v in _counts.items())
        return f"| {_label} | Count |\n| --- | --- |\n{_rows}"

    # mo.hstack([
    #     mo.md(f"""<span style="white-space: nowrap">**By query_type**</span>

    # {_counts_to_md_table(_query_type_counts, "query_type")}"""),
    #     mo.md(f"""<span style="white-space: nowrap">**By difficulty**</span>

    # {_counts_to_md_table(_difficulty_counts, "difficulty")}"""),
    # ], justify="start", gap=3, widths="equal")
    return


@app.cell
def _(mo, test_cases):
    query_dropdown = mo.ui.dropdown(
        options={tc["question"]: tc for tc in test_cases},
        value=test_cases[0]["question"],
        label="Select a query to review",
    )
    query_dropdown
    return (query_dropdown,)


@app.cell(hide_code=True)
def _(dirty_query_ids, last_selected_query_id_box, mo, query_dropdown):
    _prev_query_id = last_selected_query_id_box[0]
    selected_query = query_dropdown.value

    _switch_warning = None
    if (
        _prev_query_id is not None
        and _prev_query_id != selected_query["id"]
        and _prev_query_id in dirty_query_ids
    ):
        _switch_warning = mo.md(
            f"⚠️ **Unsaved annotations lost**: you switched away from query "
            f"`{_prev_query_id}` without clicking Save. Those annotations were not saved."
        ).callout(kind="danger")
        dirty_query_ids.discard(_prev_query_id)

    last_selected_query_id_box[0] = selected_query["id"]

    _query_info = mo.md(f"""

    **Selected Query:** "{selected_query["question"]}"


    **id:** `{selected_query["id"]}`&nbsp;&nbsp;|&nbsp;&nbsp;
    **query_type:** `{selected_query["query_type"]}`&nbsp;&nbsp;|&nbsp;&nbsp;
    **difficulty:** `{selected_query["difficulty"]}`&nbsp;&nbsp;


    {f"**note:** {selected_query['note']}" if selected_query.get("note") else ""}
    """)

    mo.vstack([_switch_warning, _query_info]) if _switch_warning else _query_info
    return (selected_query,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Review expected passages

    For each passage below, confirm whether it actually supports the key fact
    it's meant to back.
    """)
    return


@app.cell(hide_code=True)
def _(MARKDOWN_DIR, selected_query, yaml):
    def _parse_frontmatter(doc_id):
        text = (MARKDOWN_DIR / f"{doc_id}.md").read_text()
        _, frontmatter, _ = text.split("---", 2)
        return yaml.safe_load(frontmatter)


    _doc_meta_cache = {}


    def _doc_meta(doc_id):
        if doc_id not in _doc_meta_cache:
            _doc_meta_cache[doc_id] = _parse_frontmatter(doc_id)
        return _doc_meta_cache[doc_id]


    passage_contexts = [
        {
            "doc_id": passage["doc_id"],
            "chunk_id": passage["chunk_id"],
            "page": passage.get("page"),
            "text_snippet": passage.get("text_snippet", ""),
            "text_snippet_translation_en": passage.get("text_snippet_translation_en", ""),
            "supports_key_fact": passage.get("supports_key_fact", ""),
            "question": selected_query["question"],
            "doc_title": (meta := _doc_meta(passage["doc_id"])).get("title", passage["doc_id"]),
            "doc_title_en": meta.get("title_en", ""),
            "doc_authors": meta.get("authors", ""),
            "doc_date_published": str(meta.get("date_published", "")),
        }
        for passage in selected_query["retrieval_ground_truth"]["expected_passages"]
    ]
    return (passage_contexts,)


@app.cell(hide_code=True)
def _(div, p, span):
    def render_passage_card(example):
        _query_style = (
            "font-size:0.85rem; color:#664d03; background:#fff3bf; border-radius:6px; "
            "padding:0.5rem 0.8rem; margin:0 0 0.75rem 0; max-width:65ch;"
        )
        _badge_style = (
            "background:#f1f3f5; color:#495057; border-radius:999px; "
            "padding:0.15rem 0.6rem; font-size:0.75rem; font-weight:500;"
        )
        _title_style = "font-size:1.05rem; font-weight:600; color:#1a1a1a; margin:0 0 0.2rem 0; line-height:1.3;"
        _title_native_style = "font-size:0.9rem; font-style:italic; color:#6c757d; margin:0 0 0.3rem 0; line-height:1.3;"
        _authors_style = "font-size:0.8rem; color:#6c757d; margin:0 0 0.6rem 0;"
        _native_style = (
            "font-size:0.95rem; color:#333; line-height:1.6; margin:0 0 0.6rem 0; "
            "padding:0.6rem 0.8rem; background:#f8f9fa; border-radius:6px; max-width:65ch;"
        )
        _translation_style = (
            "font-size:0.9rem; color:#495057; font-style:italic; line-height:1.55; "
            "margin:0 0 0.75rem 0; max-width:65ch;"
        )
        _fact_style = (
            "font-size:0.9rem; color:#1a1a1a; line-height:1.5; margin:0 0 0.5rem 0; "
            "padding:0.5rem 0.8rem; border-left:3px solid #4c6ef5; background:#eef2ff; max-width:65ch;"
        )
        _label_style = "font-size:0.8rem; font-weight:600; color:#6c757d; margin:0 0 0.25rem 0;"

        _title_en = (example.get("doc_title_en") or "").strip()
        _title_native = (example.get("doc_title") or "").strip()
        _primary_title = _title_en or _title_native
        _show_native = bool(_title_native) and _title_native.lower() != _primary_title.lower()

        _title_els = [p(_primary_title, style=_title_style)]
        if _show_native:
            _title_els.append(p(_title_native, style=_title_native_style))

        _authors_line = " · ".join(
            _bit for _bit in [example.get("doc_authors", ""), example.get("doc_date_published", "")] if _bit
        )

        return str(
            div(
                p(f"Query: \u201c{example['question']}\u201d", style=_query_style),
                *_title_els,
                p(_authors_line, style=_authors_style),
                div(
                    span(example["doc_id"], style=_badge_style),
                    span(f"page {example['page']}", style=_badge_style) if example.get("page") else "",
                    style="display:flex; gap:0.4rem; flex-wrap:wrap; margin-bottom:0.6rem;",
                ),
                p("Source passage (native language):", style=_label_style),
                p(example["text_snippet"], style=_native_style),
                p("English translation:", style=_label_style),
                p(example["text_snippet_translation_en"], style=_translation_style),
                p("This passage is meant to support:", style=_label_style),
                p(example["supports_key_fact"], style=_fact_style),
                p("Does this passage actually support the stated key fact?",
                  style="font-size:0.95rem; font-weight:600; color:#1a1a1a; margin:0.75rem 0 0 0; padding-top:0.5rem; border-top:1px solid #e9ecef;"),
                klass="molabel-passage-context",
            )
        )

    return (render_passage_card,)


@app.cell(hide_code=True)
def _(SimpleLabel, mo, passage_contexts, render_passage_card):
    passage_widget = mo.ui.anywidget(SimpleLabel(examples=passage_contexts, render=render_passage_card))
    passage_widget
    return (passage_widget,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Review synthesized answer

    Review the `canonical_answer` below: does it accurately and completely
    answer the query, based on the source document? `key_facts` are shown for
    context only and are not individually reviewed at this stage.
    """)
    return


@app.cell(hide_code=True)
def _(selected_query):
    synthesis_contexts = [
        {
            "query_id": selected_query["id"],
            "question": selected_query["question"],
            "canonical_answer": selected_query["synthesis_ground_truth"].get("canonical_answer", ""),
            "key_facts": selected_query["synthesis_ground_truth"].get("key_facts", []),
        }
    ]
    return (synthesis_contexts,)


@app.cell(hide_code=True)
def _(div, mo, p):
    def render_synthesis_card(example):
        _query_style = (
            "font-size:0.85rem; color:#664d03; background:#fff3bf; border-radius:6px; "
            "padding:0.5rem 0.8rem; margin:0 0 0.75rem 0; max-width:65ch;"
        )
        _label_style = "font-size:0.8rem; font-weight:600; color:#6c757d; margin:0 0 0.25rem 0;"
        _answer_style = (
            "font-size:0.95rem; color:#333; line-height:1.6; margin:0 0 0.75rem 0; "
            "padding:0.6rem 0.8rem; background:#f8f9fa; border-radius:6px; max-width:65ch;"
        )
        _facts_list_style = "font-size:0.85rem; color:#495057; line-height:1.6; margin:0 0 0.75rem 0; padding-left:1.2rem; max-width:65ch;"

        _facts_items = "".join(f"<li>{fact}</li>" for fact in example.get("key_facts", []))
        _facts_html = f'<ul style="{_facts_list_style}">{_facts_items}</ul>' if _facts_items else ""

        return str(
            div(
                p(f"Query: \u201c{example['question']}\u201d", style=_query_style),
                p("canonical_answer:", style=_label_style),
                p(example["canonical_answer"], style=_answer_style),
                p("key_facts (context only, not individually reviewed):", style=_label_style),
                mo.Html(_facts_html) if _facts_html else "",
                p("Does this synthesized answer accurately and completely answer the query, based on the source document?",
                  style="font-size:0.95rem; font-weight:600; color:#1a1a1a; margin:0.75rem 0 0 0; padding-top:0.5rem; border-top:1px solid #e9ecef;"),
                klass="molabel-synthesis-context",
            )
        )

    return (render_synthesis_card,)


@app.cell(hide_code=True)
def _(SimpleLabel, mo, render_synthesis_card, synthesis_contexts):
    synthesis_widget = mo.ui.anywidget(SimpleLabel(examples=synthesis_contexts, render=render_synthesis_card))
    synthesis_widget
    return (synthesis_widget,)


@app.cell(hide_code=True)
def _():
    saved_annot_paths = set()
    dirty_query_ids = set()
    last_selected_query_id_box = [None]
    return dirty_query_ids, last_selected_query_id_box, saved_annot_paths


@app.cell(hide_code=True)
def _(dirty_query_ids, passage_widget, selected_query, synthesis_widget):
    _ = passage_widget.value  # dependency: mark query dirty whenever passage annotation state changes
    _ = synthesis_widget.value  # dependency: mark query dirty whenever synthesis annotation state changes

    if passage_widget.get_annotations() or synthesis_widget.get_annotations():
        dirty_query_ids.add(selected_query["id"])
    return


@app.cell(hide_code=True)
def _(mo):
    save_button = mo.ui.run_button(label="Save", tooltip="Click to Save")
    save_button
    return (save_button,)


@app.cell(hide_code=True)
def _(
    EVALSET_NAME,
    REPO_ROOT,
    REVIEW_OUTPUT_DIR,
    dirty_query_ids,
    json,
    mo,
    passage_widget,
    re,
    reviewer_name_input,
    save_button,
    saved_annot_paths,
    selected_query,
    submit_to_review_dashboard,
    synthesis_widget,
):
    mo.stop(not save_button.value, mo.md("**Saved Results**: None. <br>_Click the button above to save your review for this query._"))

    _reviewer = re.sub(r"[^\w\-]+", "_", reviewer_name_input.value.strip()) or "reviewer"

    _passage_annotations = passage_widget.get_annotations()
    _reviewed_passages = [
        {
            "chunk_id": _a["example"]["chunk_id"],
            "doc_id": _a["example"]["doc_id"],
            "label": _a["_label"],
            "notes": _a["_notes"],
            "timestamp": _a["_timestamp"],
        }
        for _a in _passage_annotations
    ]

    _synthesis_annotations = synthesis_widget.get_annotations()
    _synthesis_review = None
    if _synthesis_annotations:
        _syn = _synthesis_annotations[0]
        _synthesis_review = {
            "label": _syn["_label"],
            "notes": _syn["_notes"],
            "timestamp": _syn["_timestamp"],
        }

    _payload = {
        "query_id": selected_query["id"],
        "question": selected_query["question"],
        "reviewer": _reviewer,
        "reviewed_passages": _reviewed_passages,
        "synthesis_review": _synthesis_review,
    }
    _filename = f"annot-{EVALSET_NAME}-{selected_query['id']}-by-{_reviewer}.json"

    REVIEW_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    _annotations_path = REVIEW_OUTPUT_DIR / _filename
    _annotations_path.write_text(json.dumps(_payload, indent=2))
    saved_annot_paths.add(_annotations_path)
    dirty_query_ids.discard(selected_query["id"])

    print(f"Saved annotations to: {_annotations_path.relative_to(REPO_ROOT)}")

    _submitted, _submit_error = submit_to_review_dashboard(_filename, _payload)

    _submit_status = (
        "\u2705 Submitted to the shared review dashboard."
        if _submitted
        else f"\u26a0\ufe0f Saved locally, but submitting to the review dashboard failed: `{_submit_error}`"
    )

    mo.md(f"""
    Saved!

    Annotations file:
    `{_annotations_path.relative_to(REPO_ROOT)}`

    Reviewed passages: {len(_reviewed_passages)} \u00b7 Synthesis reviewed: {"yes" if _synthesis_review else "no"}

    {_submit_status}
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Track progress in this session

    This displays what you've reviewed and saved in this session. A query is
    marked done once both its passages and its synthesized answer have been
    saved. If you close and reopen the notebook, this section will refresh.
    """)
    return


@app.cell(hide_code=True)
def _(
    EVALSET_NAME,
    div,
    json,
    mo,
    re,
    save_button,
    saved_annot_paths,
    test_cases,
):
    _ = save_button.value  # dependency: refresh whenever Save is clicked

    _reviewed_by_query = {}
    for _path in sorted(saved_annot_paths):
        _data = json.loads(_path.read_text())
        _qid = _data["query_id"]
        _prev = _reviewed_by_query.get(_qid, {"passages": False, "synthesis": False})
        _reviewed_by_query[_qid] = {
            "passages": _prev["passages"] or bool(_data.get("reviewed_passages")),
            "synthesis": _prev["synthesis"] or _data.get("synthesis_review") is not None,
        }

    _done_query_ids = {
        _qid for _qid, _flags in _reviewed_by_query.items()
        if _flags["passages"] and _flags["synthesis"]
    }

    total_queries = len(test_cases)
    total_done = len(_done_query_ids)


    def _chip(tc):
        _n = re.match(r"[a-zA-Z]*(\d+)", tc["id"]).group(1)
        _done = tc["id"] in _done_query_ids
        return div(
            _n, " ", "\u2705" if _done else "\u2b1c",
            title=tc["question"],
            style=(
                "display:inline-flex; align-items:center; justify-content:center; gap:0.3rem; "
                "padding:0.4rem 0.75rem; border-radius:8px; "
                "font-size:1rem; font-weight:600; "
                + ("background:#d4edda; color:#155724;" if _done else "background:#f1f3f5; color:#495057;")
            ),
        )


    checklist_html = str(div(
        *[_chip(tc) for tc in test_cases],
        style="display:grid; grid-template-columns:repeat(10, auto); gap:0.4rem; margin-top:0.75rem;",
    ))

    mo.vstack([
        mo.hstack(
            [
                mo.stat(value=total_queries, label="Total queries", bordered=True),
                mo.stat(
                    value=total_done,
                    label="Fully reviewed (passages + synthesis)",
                    bordered=True,
                ),
            ],
            gap=2,
        ),
        mo.md(f"Queries reviewed in this eval set **'{EVALSET_NAME}'**"),
        mo.Html(checklist_html),
    ])
    return


if __name__ == "__main__":
    app.run()
