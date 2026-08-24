# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo",
#     "anywidget",
#     "pandas",
# ]
# ///

import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # CITE-mode eval review: propose a query

    Propose new queries for the AskWRI CITE (Citation) mode evalset.

    Pick a source evalset for context, then write a question and select the
    documents you'd expect it to retrieve. Submit / Export to create an
    updated eval set with your proposed queries added.
    """)
    return


@app.cell
def _():
    import copy
    import datetime
    import json
    import re

    import marimo as mo

    import pandas as pd

    return copy, datetime, json, mo, pd, re


@app.cell
def _(mo):
    REPO_ROOT = mo.notebook_dir().parent

    # Everything under source_evalsets/ is read-only reference data, tracked as plain files.
    EVALSET_DIR = REPO_ROOT / "evalsets"
    REVIEW_OUTPUT_DIR = REPO_ROOT / "review-output"
    DOCUMENTS_LIST_PATH = REPO_ROOT / "eval-generation-notes" / "documents-list_20260817.txt"

    return (
        DOCUMENTS_LIST_PATH,
        EVALSET_DIR,
        REPO_ROOT,
        REVIEW_OUTPUT_DIR,
    )


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


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Propose a new query
    """)
    return


@app.cell
def _(DOCUMENTS_LIST_PATH, mo):
    def _parse_documents_list(path):
        _docs = []
        for _block in path.read_text().strip().split("\n\n"):
            _block = _block.strip()
            if not _block:
                continue
            _docs.append(dict(_line.split(": ", 1) for _line in _block.splitlines()))
        return _docs

    # documents are loaded from  `{DOCUMENTS_LIST_PATH.relative_to(REPO_ROOT)}`

    ALL_DOCUMENTS = _parse_documents_list(DOCUMENTS_LIST_PATH)
    mo.md(f"**{len(ALL_DOCUMENTS)}** documents loaded.")

    return (ALL_DOCUMENTS,)


@app.cell
def _(mo, test_cases):
    new_query_text = mo.ui.text(
        label="New query question",
        placeholder="e.g. What has WRI published on ...?",
        full_width=True,
    )
    new_query_type = mo.ui.dropdown(
        options=sorted({tc["query_type"] for tc in test_cases}),
        label="Query type",
    )
    new_query_difficulty = mo.ui.dropdown(
        options=sorted({tc["difficulty"] for tc in test_cases}),
        value="medium",
        label="Difficulty",
    )

    mo.vstack([
        new_query_text,
        mo.hstack([new_query_type, new_query_difficulty], gap=1, justify="start"),
    ])

    return new_query_difficulty, new_query_text, new_query_type


@app.cell
def _(ALL_DOCUMENTS, DocumentPicker, mo):
    doc_picker = mo.ui.anywidget(DocumentPicker(documents=ALL_DOCUMENTS))
    doc_picker

    return (doc_picker,)


@app.cell
def _(mo):
    add_query_button = mo.ui.run_button(label="Add proposed query")
    mo.vstack([
        add_query_button,
        mo.md("*Adds this question + selected documents as a new test case, included when you Submit / Export.*"),
    ])

    return (add_query_button,)


@app.cell
def _():
    proposed_queries = []

    return (proposed_queries,)


@app.cell
def _(
    ALL_DOCUMENTS,
    add_query_button,
    doc_picker,
    mo,
    new_query_difficulty,
    new_query_text,
    new_query_type,
    proposed_queries,
    re,
    reviewer_name_input,
    test_cases,
):
    mo.stop(not add_query_button.value, mo.md(""))

    _question = new_query_text.value.strip()
    mo.stop(not _question, mo.md("**Cannot add:** please enter a query question first."))

    _docs_by_external_id = {d["external_id"]: d for d in ALL_DOCUMENTS}
    _selected_docs = [_docs_by_external_id[e] for e in doc_picker.value["selected"] if e in _docs_by_external_id]

    _slug = re.sub(r"[^a-z0-9]+", "-", _question.lower()).strip("-")[:50]
    _existing_ids = [tc["id"] for tc in test_cases] + [pq["id"] for pq in proposed_queries]
    _existing_nums = [int(_m.group(1)) for _id in _existing_ids if (_m := re.match(r"[a-zA-Z]*(\d+)", _id))]
    _next_n = (max(_existing_nums) + 1) if _existing_nums else 1

    _new_test_case = {
        "id": f"new{_next_n}_{_slug}",
        "question": _question,
        "task_description": "",
        "expected_document_ids": [d["document_id"] for d in _selected_docs],
        "expected_external_ids": [d["external_id"] for d in _selected_docs],
        "source_document_id": _selected_docs[0]["document_id"] if _selected_docs else "",
        "source_language": _selected_docs[0]["language"] if _selected_docs else "",
        "difficulty": new_query_difficulty.value,
        "query_type": new_query_type.value,
        "note": f"Proposed via review notebook by {reviewer_name_input.value}.",
    }

    proposed_queries.append(_new_test_case)

    mo.md(f"""
    **Added proposed query** `{_new_test_case["id"]}`

    - Question: {_new_test_case["question"]}
    - Documents selected: {len(_selected_docs)}
    - Query type: {_new_test_case["query_type"]} · Difficulty: {_new_test_case["difficulty"]}

    Total proposed queries this session: **{len(proposed_queries)}**
    """)

    return


@app.cell(hide_code=True)
def _(mo):
    submit_button = mo.ui.run_button(label="Submit / Export")
    mo.vstack([
        submit_button,
        mo.md("*Creates an updated eval set with your proposed queries added.*"),
    ])
    return (submit_button,)


@app.cell(hide_code=True)
def _(
    EVALSET_NAME,
    REPO_ROOT,
    REVIEW_OUTPUT_DIR,
    build_updated_evalset,
    datetime,
    evalset,
    json,
    mo,
    proposed_queries,
    submit_button,
):
    mo.stop(not submit_button.value, mo.md(""))
    mo.stop(not proposed_queries, mo.md("**Nothing to export.** Propose at least one new query before exporting."))

    _updated_evalset = build_updated_evalset(evalset, proposed_queries)

    _timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    REVIEW_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    _evalset_path = REVIEW_OUTPUT_DIR / f"{EVALSET_NAME}-{_timestamp}.json"
    _evalset_path.write_text(json.dumps(_updated_evalset, indent=2))

    mo.md(f"""
    Exported!

    Proposed new queries added: {len(proposed_queries)}

    Updated evalset:\n`{_evalset_path.relative_to(REPO_ROOT)}`
    """)

    return


@app.cell
def _(copy):
    def build_updated_evalset(source_evalset, proposed_queries=None):
        updated_evalset = copy.deepcopy(source_evalset)
        if proposed_queries:
            updated_evalset["test_cases"].extend(copy.deepcopy(proposed_queries))
        return updated_evalset


    return (build_updated_evalset,)


@app.cell
def _():
    import anywidget
    import traitlets


    class DocumentPicker(anywidget.AnyWidget):
        _esm = """
        function fuzzyScore(query, target) {
          query = query.toLowerCase();
          target = target.toLowerCase();
          if (!query) return 0;
          let qi = 0, score = 0, consecutive = 0;
          for (let ti = 0; ti < target.length && qi < query.length; ti++) {
            if (target[ti] === query[qi]) {
              score += 1 + consecutive;
              consecutive += 1;
              qi += 1;
            } else {
              consecutive = 0;
            }
          }
          if (qi < query.length) return -1;
          if (target.includes(query)) score += 10;
          return score;
        }

        function render({ model, el }) {
          el.innerHTML = "";

          const documents = model.get("documents");
          let query = "";
          let selected = new Set(model.get("selected") || []);

          const container = document.createElement("div");
          container.className = "doc-picker";

          const chipsRow = document.createElement("div");
          chipsRow.className = "doc-picker-chips";

          const input = document.createElement("input");
          input.type = "text";
          input.placeholder = "Search documents by title or external id...";
          input.className = "doc-picker-search";

          const resultsList = document.createElement("div");
          resultsList.className = "doc-picker-results";

          container.appendChild(chipsRow);
          container.appendChild(input);
          container.appendChild(resultsList);
          el.appendChild(container);

          function docByExternalId(externalId) {
            return documents.find((d) => d.external_id === externalId);
          }

          function commitSelection() {
            model.set("selected", Array.from(selected));
            model.save_changes();
          }

          function renderChips() {
            chipsRow.innerHTML = "";
            if (selected.size === 0) {
              const empty = document.createElement("span");
              empty.className = "doc-picker-empty";
              empty.textContent = "No documents selected yet.";
              chipsRow.appendChild(empty);
              return;
            }
            for (const extId of selected) {
              const doc = docByExternalId(extId);
              const chip = document.createElement("span");
              chip.className = "doc-picker-chip";
              const label = document.createElement("span");
              label.textContent = doc ? `${doc.title} (${doc.language})` : extId;
              const remove = document.createElement("button");
              remove.type = "button";
              remove.textContent = "\u00d7";
              remove.className = "doc-picker-chip-remove";
              remove.addEventListener("click", () => {
                selected.delete(extId);
                commitSelection();
                renderChips();
                renderResults();
              });
              chip.appendChild(label);
              chip.appendChild(remove);
              chipsRow.appendChild(chip);
            }
          }

          function renderResults() {
            resultsList.innerHTML = "";
            const q = query.trim();
            let scored = documents.map((d) => ({
              doc: d,
              score: fuzzyScore(q, `${d.title} ${d.external_id}`),
            }));
            scored = scored.filter((s) => s.score >= 0);
            scored.sort((a, b) => b.score - a.score);
            const top = scored.slice(0, 20);
            if (top.length === 0) {
              const empty = document.createElement("div");
              empty.className = "doc-picker-empty";
              empty.textContent = "No matching documents.";
              resultsList.appendChild(empty);
              return;
            }
            for (const { doc } of top) {
              const item = document.createElement("label");
              item.className = "doc-picker-item";

              const checkbox = document.createElement("input");
              checkbox.type = "checkbox";
              checkbox.checked = selected.has(doc.external_id);
              checkbox.addEventListener("change", () => {
                if (checkbox.checked) {
                  selected.add(doc.external_id);
                } else {
                  selected.delete(doc.external_id);
                }
                commitSelection();
                renderChips();
              });

              const text = document.createElement("span");
              text.className = "doc-picker-item-text";

              const titleEl = document.createElement("div");
              titleEl.className = "doc-picker-item-title";
              titleEl.textContent = doc.title;

              const metaEl = document.createElement("div");
              metaEl.className = "doc-picker-item-meta";
              metaEl.textContent = `${doc.external_id} \u00b7 ${doc.language}`;

              text.appendChild(titleEl);
              text.appendChild(metaEl);
              item.appendChild(checkbox);
              item.appendChild(text);
              resultsList.appendChild(item);
            }
          }

          input.addEventListener("input", () => {
            query = input.value;
            renderResults();
          });

          renderChips();
          renderResults();
        }

        export default { render };
        """

        _css = """
        .doc-picker {
          display: flex;
          flex-direction: column;
          gap: 0.5rem;
          max-width: 520px;
          font-family: inherit;
          color: var(--foreground);
        }
        .doc-picker-chips {
          display: flex;
          flex-wrap: wrap;
          gap: 0.35rem;
          min-height: 1.75rem;
        }
        .doc-picker-chip {
          display: inline-flex;
          align-items: center;
          gap: 0.3rem;
          background: var(--accent);
          color: var(--accent-foreground);
          border-radius: 999px;
          padding: 0.2rem 0.6rem;
          font-size: 0.85rem;
        }
        .doc-picker-chip-remove {
          border: none;
          background: transparent;
          cursor: pointer;
          font-size: 0.9rem;
          line-height: 1;
          color: inherit;
          padding: 0;
        }
        .doc-picker-empty {
          color: var(--muted-foreground);
          font-size: 0.85rem;
          font-style: italic;
        }
        .doc-picker-search {
          padding: 0.4rem 0.6rem;
          border: 1px solid var(--input);
          border-radius: 6px;
          font-size: 0.9rem;
          background: var(--background);
          color: var(--foreground);
        }
        .doc-picker-results {
          max-height: 260px;
          overflow-y: auto;
          border: 1px solid var(--border);
          border-radius: 6px;
        }
        .doc-picker-item {
          display: flex;
          align-items: flex-start;
          gap: 0.5rem;
          padding: 0.4rem 0.6rem;
          cursor: pointer;
          border-bottom: 1px solid var(--border);
        }
        .doc-picker-item:last-child {
          border-bottom: none;
        }
        .doc-picker-item:hover {
          background: var(--muted);
        }
        .doc-picker-item input[type="checkbox"] {
          margin-top: 0.2rem;
        }
        .doc-picker-item-title {
          font-size: 0.9rem;
          font-weight: 600;
          color: var(--foreground);
        }
        .doc-picker-item-meta {
          font-size: 0.78rem;
          color: var(--muted-foreground);
        }
        """

        documents = traitlets.List(traitlets.Dict()).tag(sync=True)
        selected = traitlets.List(traitlets.Unicode()).tag(sync=True)


    return (DocumentPicker,)


@app.cell(hide_code=True)
def _(EVALSET_DIR, evalset_dropdown):
    # Derive the paths from the selected dropdown value
    SELECTED_EVALSET_PATH = EVALSET_DIR / evalset_dropdown.value
    EVALSET_NAME = SELECTED_EVALSET_PATH.stem
    return EVALSET_NAME, SELECTED_EVALSET_PATH


if __name__ == "__main__":
    app.run()
