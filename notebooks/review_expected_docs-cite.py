# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo",
#     "molabel==0.1.5",
#     "mohtml==0.1.11",
#     "pandas==3.0.5",
#     "pyyaml==6.0.3",
#     "httpx==0.28.1",
# ]
# ///

import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # CITE-mode eval review

    Review the evalset for AskWRI CITE (Citation) mode.

    For each query, step through its `expected_document_ids` and confirm
    whether each document is actually a correct match.
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
    from mohtml import div, p, span, a

    import pandas as pd

    return SimpleLabel, a, div, httpx, json, mo, p, pd, re, span, yaml


@app.cell
def _(mo):
    REPO_ROOT = mo.notebook_dir().parent

    # Everything under source_evalsets/ is read-only reference data, tracked as plain files.
    EVALSET_DIR = REPO_ROOT / "evalsets"
    MARKDOWN_DIR = REPO_ROOT / "kp-docs" / "markdown"
    REVIEW_OUTPUT_DIR = REPO_ROOT / "review-output"
    return EVALSET_DIR, MARKDOWN_DIR, REPO_ROOT, REVIEW_OUTPUT_DIR


@app.cell
def _():
    # Where "Save" submissions get POSTed so reviews land somewhere the
    # notebook owner can see them, even when run read-only via molab/WASM
    # (which has no persistent server-side filesystem of its own).
    #
    # This URL is not a secret credential -- it's a Google Apps Script Web
    # App endpoint that can only append a file to one Drive folder and a row
    # to one Sheet (see TECH_INFO.md "Submitting notebook output to a
    # filedrop you own" for how this was set up, and how to rotate/replace
    # it). Treat it as security-through-obscurity: fine for a short-lived,
    # low-stakes review period; revoke the deployment in Apps Script when
    # the review period ends.
    SUBMIT_ENDPOINT_URL = "https://script.google.com/macros/s/AKfycbxNoFNUBXJkYEQK_m2yNeNMilhEqh22bXxbFjiWeZA03JCKxayTTScht2938U3mVakO/exec"
    return (SUBMIT_ENDPOINT_URL,)


@app.cell
def _(SUBMIT_ENDPOINT_URL, httpx, json):
    def submit_to_review_dashboard(filename, payload):
        """Best-effort POST of a saved review file to the shared dashboard.

        Never raises -- returns (success, error_message) so callers can
        surface a warning without blocking the (already-successful) local
        save.
        """
        try:
            httpx.post(
                SUBMIT_ENDPOINT_URL,
                json={"filename": filename, "content": json.dumps(payload, indent=2)},
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

    # filter to "cite" mode evalsets only
    eval_set_list = [e for e in eval_set_list if "cite" in e.name.lower()]
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
    default_idx = evalset_names.index("evalset_cite_02.json") if "evalset_cite_02.json" in evalset_names else 0

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
def _(mo, pd, test_cases):
    _query_type_counts = pd.Series([tc["query_type"] for tc in test_cases]).value_counts()
    _difficulty_counts = pd.Series([tc["difficulty"] for tc in test_cases]).value_counts()

    def _counts_to_md_table(_counts, _label):
        _rows = "\n".join(f"| {_k} | {_v} |" for _k, _v in _counts.items())
        return f"| {_label} | Count |\n| --- | --- |\n{_rows}"

    mo.hstack([
        mo.md(f"""<span style="white-space: nowrap">**By query_type**</span>

    {_counts_to_md_table(_query_type_counts, "query_type")}"""),
        mo.md(f"""<span style="white-space: nowrap">**By difficulty**</span>

    {_counts_to_md_table(_difficulty_counts, "difficulty")}"""),
    ], justify="start", gap=3, widths="equal")
    return


@app.cell
def _(SELECTED_EVALSET_PATH, json):
    evalset = json.loads(SELECTED_EVALSET_PATH.read_text())
    test_cases = evalset["test_cases"]
    #test_cases[:1]
    return evalset, test_cases


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
            f"\u26a0\ufe0f **Unsaved annotations lost**: you switched away from query "
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
def _(SimpleLabel, doc_contexts, mo, render_molabel_card):
    widget = mo.ui.anywidget(SimpleLabel(examples=doc_contexts, render=render_molabel_card))
    widget
    return (widget,)


@app.cell
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
    doc_contexts,
    json,
    mo,
    re,
    reviewer_name_input,
    save_button,
    saved_annot_paths,
    selected_query,
    submit_to_review_dashboard,
    widget,
):
    mo.stop(not save_button.value, mo.md("**Saved Results**: None. <br>_Click the button above to save your review for this query._"))

    _reviewer = re.sub(r"[^\w\-]+", "_", reviewer_name_input.value.strip()) or "reviewer"
    _annotations = widget.get_annotations()
    _records = [
        {
            "doc_id": doc_contexts[a["index"]]["doc_id"],
            "label": a["_label"],
            "notes": a["_notes"],
            "timestamp": a["_timestamp"],
        }
        for a in _annotations
    ]

    _payload = {
        "query_id": selected_query["id"],
        "question": selected_query["question"],
        "task_description": selected_query["task_description"],
        "reviewer": _reviewer,
        "reviewed_documents": _records,
    }
    _filename = f"annot-{EVALSET_NAME}-{selected_query['id']}-by-{_reviewer}.json"

    REVIEW_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    _annotations_path = REVIEW_OUTPUT_DIR / _filename
    _annotations_path.write_text(json.dumps(_payload, indent=2))
    saved_annot_paths.add(_annotations_path)
    dirty_query_ids.discard(selected_query["id"])

    print(f"Saved annotations to: {_annotations_path.relative_to(REPO_ROOT)}")

    # Also push to the remote folder (Drive + Sheet) so submissions
    # are visible to the notebook owner even when run read-only via
    # molab/WASM
    _submitted, _submit_error = submit_to_review_dashboard(_filename, _payload)

    _submit_status = (
        "✅ Submitted to Fenris' shared folder."
        if _submitted
        else f"⚠️ Saved locally, but submitting to the review dashboard failed: `{_submit_error}`"
    )

    mo.md(f"""
    Saved!

    Annotations file:\n`{_annotations_path.relative_to(REPO_ROOT)}`

    {_submit_status}
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Track progress in this session

    This displays what you've reviewed and suggested in this session. If you close and reopen the notebook, this section will refresh.
    """)
    return


@app.cell
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

    _rejected_by_query = {}
    for _path in sorted(saved_annot_paths):
        _data = json.loads(_path.read_text())
        _qid = _data["query_id"]
        _rejected = {d["doc_id"] for d in _data["reviewed_documents"] if d["label"] == "no"}
        _rejected_by_query.setdefault(_qid, set()).update(_rejected)

    total_expected = sum(len(tc["expected_document_ids"]) for tc in test_cases)
    total_current = sum(
        len(tc["expected_document_ids"]) - len(_rejected_by_query.get(tc["id"], set()))
        for tc in test_cases
    )
    total_rejected = total_expected - total_current


    def _chip(tc):
        _n = re.match(r"[a-zA-Z]*(\d+)", tc["id"]).group(1)
        _done = tc["id"] in _rejected_by_query
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
                mo.stat(value=total_expected, label="Total expected docs (all queries)", bordered=True),
                mo.stat(
                    value=total_current,
                    label="Total expected (after review)",
                    caption=f"{total_rejected} rejected" if total_rejected else "No rejections yet",
                    direction="decrease" if total_current < total_expected else None,
                    target_direction="increase",
                    bordered=True,
                ),
            ],
            gap=2,
        ),
        mo.md(f"Queries reviewed in this eval set **'{EVALSET_NAME}'**"),
        mo.Html(checklist_html),
    ])
    return


@app.cell
def _():
    saved_annot_paths = set()
    dirty_query_ids = set()
    last_selected_query_id_box = [None]
    return dirty_query_ids, last_selected_query_id_box, saved_annot_paths


@app.cell
def _(MARKDOWN_DIR, selected_query, yaml):
    def _parse_frontmatter(doc_id):
        text = (MARKDOWN_DIR / f"{doc_id}.md").read_text()
        _, frontmatter, _ = text.split("---", 2)
        return yaml.safe_load(frontmatter)


    doc_contexts = [
        {
            "doc_id": doc_id,
            "title": (meta := _parse_frontmatter(doc_id)).get("title", doc_id),
            "authors": meta.get("authors", ""),
            "date_published": meta.get("date_published", ""),
            "article_type": meta.get("article_type", ""),
            "sub_tag": meta.get("sub_tag", ""),
            "url": meta.get("url", ""),
            "summary": meta.get("summary", ""),
        }
        for doc_id in selected_query["expected_external_ids"]
    ]
    return (doc_contexts,)


@app.cell
def _(a, div, p, span):
    _badge_style = (
        "background:#f1f3f5; color:#495057; border-radius:999px; "
        "padding:0.15rem 0.6rem; font-size:0.75rem; font-weight:500;"
    )
    _doc_link_style = (
        "display:inline-block; background:#e9ecef; color:#495057; "
        "text-decoration:none; font-size:0.85rem; font-weight:500; "
        "padding:0.4rem 0.9rem; border-radius:6px;"
    )
    _doc_link_disabled_style = (
        "display:inline-block; background:#f1f3f5; color:#adb5bd; "
        "text-decoration:none; font-size:0.85rem; font-weight:500; "
        "padding:0.4rem 0.9rem; border-radius:6px; cursor:not-allowed; "
        "pointer-events:none;"
    )
    _summary_style = (
        "font-size:0.95rem; color:#333; line-height:1.55; margin:0 0 0.75rem 0; max-width:65ch;"
    )
    _summary_missing_style = (
        "font-size:0.95rem; color:#adb5bd; font-style:italic; line-height:1.55; "
        "margin:0 0 0.75rem 0; max-width:65ch;"
    )


    def render_doc_info(example):
        doc_url = example["url"]
        if doc_url:
            doc_link = a("\U0001F4C4 View document", href=doc_url, target="_blank",
                          style=_doc_link_style)
        else:
            doc_link = span("\U0001F4C4 URL not available", style=_doc_link_disabled_style)

        summary = example["summary"]
        if summary:
            summary_el = p(summary, style=_summary_style)
        else:
            summary_el = p("No summary available", style=_summary_missing_style)

        return str(
            div(
                p(example["title"],
                  style="font-size:1.25rem; font-weight:600; color:#1a1a1a; margin:0 0 0.25rem 0; line-height:1.3;"),
                p(example["authors"],
                  style="font-size:0.85rem; color:#6c757d; margin:0 0 0.6rem 0;"),
                p(f"Date Published: {example['date_published']}",
                  style="font-size:0.85rem; color:#495057; margin:0 0 0.5rem 0;"),
                div(
                    span(example["article_type"], style=_badge_style),
                    span(example["sub_tag"], style=_badge_style),
                    style="display:flex; gap:0.4rem; flex-wrap:wrap; margin-bottom:0.6rem;",
                ),
                summary_el,
                doc_link,
                klass="molabel-doc-context",
            )
        )


    return (render_doc_info,)


@app.cell
def _(div, p, render_doc_info):
    def render_molabel_card(example):
        return str(
            div(
                render_doc_info(example),
                p("Is this document a correct result for the query?",
                  style="font-size:0.95rem; font-weight:600; color:#1a1a1a; margin:0.75rem 0 0 0; padding-top:0.5rem; border-top:1px solid #e9ecef;"),
            )
        )


    return (render_molabel_card,)


@app.cell(hide_code=True)
def _(EVALSET_DIR, evalset_dropdown):
    # Derive the paths from the selected dropdown value
    SELECTED_EVALSET_PATH = EVALSET_DIR / evalset_dropdown.value
    EVALSET_NAME = SELECTED_EVALSET_PATH.stem
    return EVALSET_NAME, SELECTED_EVALSET_PATH


@app.cell
def _(dirty_query_ids, selected_query, widget):
    _ = widget.value  # dependency: mark query dirty whenever annotation state changes

    if widget.get_annotations():
        dirty_query_ids.add(selected_query["id"])
    return


if __name__ == "__main__":
    app.run()
