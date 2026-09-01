Research Report: Document Chunk Storage in Postgres
1. The table: document_chunks
Canonical DDL (original migration): src/db/migrations/1781280000000-Migration.ts:59-87
CREATE TABLE "document_chunks" (
  "id" uuid NOT NULL DEFAULT uuid_generate_v4(),
  "document_id" uuid NOT NULL REFERENCES "documents"("id") ON DELETE CASCADE,
  "legacy_chunk_id" text,
  "chunk_index" integer NOT NULL,
  "unit_type" text NOT NULL DEFAULT 'text',
  "unit_number" text,
  "section_path" text,
  "page" integer,
  "caption" text,
  "text" text NOT NULL,
  "structured" jsonb,
  "language" text,
  "node_metadata" jsonb NOT NULL DEFAULT '{}',
  "embedding" vector,
  "embedding_model" text,
  "dimension" integer,
  "sparse" sparsevec,
  "created_at" TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT now(),
  CONSTRAINT "UQ_document_chunks_legacy_chunk_id" UNIQUE ("legacy_chunk_id"),
  CONSTRAINT "PK_document_chunks" PRIMARY KEY ("id")
)

Plus indices: idx_chunks_document (document_id), HNSW indexes on embedding (per embedding_model).

Later additions (still same table):
- corpus_order integer — src/db/migrations/1781290000000-Migration.ts:10 (BM25 tie-break position, appended monotonically).
- sparse column (BGE/keyword sparse vector) already present in original DDL; populated later by search-service/app/sparse_keyword.py + worker/stages/embed.py.

There is no TypeORM entity for document_chunks — it's explicitly Python-owned (comment in src/db/migrations/1787160000000-TopicTaxonomy.ts:7-8 and 1787480000000-SearchVocab.ts:7). No Next.js/TS query file touches it directly.

2. Columns (with roles)

Column	Type
id	uuid (PK)
document_id	uuid (FK → documents.id)
legacy_chunk_id	text (UNIQUE)
chunk_index	integer
unit_type	text
page	integer
text	text
node_metadata	jsonb
embedding	vector
sparse	sparsevec
corpus_order	integer
Related table document_texts (document_id PK, full_text, page_boundaries jsonb array of {page, end_pos}, char_count) holds the full doc text used to derive page per chunk (search-service/app/indexing.py:20-30, get_page_number_for_position).

3. chunk_id format/generation — it's legacy_chunk_id, deterministic, NOT a UUID
The app-facing "chunk_id" is the document_chunks.legacy_chunk_id column. It is generated deterministically as:
{external_id}_chunk_{chunk_index}     # regular chunk (0-based index)
{external_id}_summary                  # one synthetic summary node per doc, chunk_index = -1
Generation sites (identical logic, duplicated deliberately per code comments "must match production chunking"):
- search-service/app/indexing.py:360 and :396 (Phase-0 / batch migration path, used by scripts/migrate_csv_to_postgres.py)
- search-service/worker/stages/embed.py:114 and :128 (live per-document ingestion worker path)
Chunking parameters: SimpleNodeParser.from_defaults(chunk_size=400, chunk_overlap=80) (characters), documented explicitly in docs/plans/2026-06-09-phase0-store-and-migration-plan.md:20 and docs/plans/2026-06-10-phase1-ingestion-implementation-plan.md:19.
node_metadata also carries prev_chunk_id/next_chunk_id (same format, ±1 index) for passage-context stitching, and chunk_id is duplicated inside node_metadata itself.
The document_chunks.id UUID PK is never surfaced as "chunk_id" in any API/eval code — only legacy_chunk_id is.

4. Relationship: chunk_id vs. document_id (UUID) vs. external_id (slug)
- documents table has both id (uuid, PK) and external_id (text, unique) — src/db/migrations/1781280000000-Migration.ts:12-13.
- external_id = legacy doc slug = file_path minus .pdf extension (e.g. 2021_accelerating-…_1054) — confirmed in docs/plans/2026-06-09-phase0-store-and-migration-plan.md:21 and s3_key_for() in scripts/migrate_csv_to_postgres.py:114-130.
- document_chunks.document_id is a foreign key to the Postgres UUID (documents.id), used for joins/cascades — this is independent of the chunk_id string.
- legacy_chunk_id (the "chunk_id") is derived from external_id (the slug), not from the UUID: f"{doc['external_id']}_chunk_{idx}" (embed.py:114) / f"{doc['doc_id']}_chunk_{chunk_idx}" where doc['doc_id'] is populated from CSV/external_id (indexing.py:360).
- Everywhere in the /query API response and eval code, the field called doc_id is actually the external_id/slug, not the Postgres UUID (search-service/app/main.py:1656, :1807-1809; confirmed by pg_store.py:58-66 which maps {external_id: full_text}).
So: chunk_id = "{external_id}_chunk_{N}" (or "{external_id}_summary") — a deterministic, human-readable string keyed off the slug, unrelated in format to the Postgres document_id UUID (which only exists as an FK column for referential integrity).

5. Existing reverse-lookup code (human passage → chunk_id)
Found — directly relevant, reusable/adaptable:
evaluation/map-passages-to-chunks.ts (285 lines) — exactly this workflow:
- Input: golden-set JSON entries with {doc_id, text_snippet, page?} and no/stale chunk_id.
- Calls the running hybrid search service's /query endpoint (answer mode, wide net: vector_top_k/bm25_top_k: 200; falls back to cite mode with 500/500 if no hits) with the snippet as the query.
- Filters results to the target doc_id (external_id).
- Scores each candidate chunk against the snippet via textOverlapScore() — word-level Jaccard + substring-containment heuristic (map-passages-to-chunks.ts:35-67).
- Picks the best-scoring chunk, writes its chunk_id/page back into the golden-set entry; warns if overlap score < 0.3.
- CLI: npx tsx evaluation/map-passages-to-chunks.ts [--input path] [--output path] [--remap].

Supporting pieces:
- evaluation/lib/service-client.ts — callPythonService() posts to ${PYTHON_SERVICE_URL}/query and returns RawServiceDoc[] with doc_id, content, page, metadata.chunk_id (this is what a fixture-builder should reuse for querying).
- evaluation/lib/types.ts — ExpectedPassage { doc_id, chunk_id, page, text_snippet } is the exact target shape for golden-set fixtures.
- Direct-SQL alternative pattern (no HTTP hop needed) in search-service/app/pg_store.py:21-45: query document_chunks joined to documents filtered by d.external_id = %s, ordered by corpus_order/chunk_index, then do the same text-overlap match against dc.text locally instead of calling the live service. This is what you'd adapt for an offline/DB-only reverse lookup that doesn't require the search-service running.

Also relevant/adjacent (not reverse-lookup per se, but related eval tooling):
- evaluation/relabel-answer-chunks.ts, evaluation/serve-label-review.ts, evaluation/calibrate-answer-thresholds.ts — all consume/produce chunk_id fields matching the legacy_chunk_id format for label review UIs.
- evaluation/README.md likely documents the golden-set workflow (not yet read in depth — worth checking if building new fixtures).

6. Docs on chunking strategy
Primary source of truth: docs/plans/2026-06-09-phase0-store-and-migration-plan.md — "Key facts" table (lines 15-33) states, verbatim:
- Chunking: SimpleNodeParser.from_defaults(chunk_size=400, chunk_overlap=80) (characters, not tokens)
- Legacy doc_id (= external_id): file_path minus .pdf
- Legacy chunk_id: {doc_id}_chunk_{n}; summary node = {doc_id}_summary
- One summary node per doc: text = f"{title}\n\n{summary}", is_summary_node=True, chunk_index=-1
- Embeddings computed over node.get_content(metadata_mode=EMBED) (text + selected metadata), not raw text alone
docs/plans/2026-06-10-phase1-ingestion-implementation-plan.md:19,36 reconfirms identical chunking for the live worker pipeline and lists the full node_metadata key set.
Page-boundary / PDF-split handling (not in a single doc paragraph, but in code, referenced by the plans):
- PDF text extraction produces a page_boundaries list of {page, end_pos} marking the cumulative character offset where each page's text ends, joined with "\n\n" between pages:
- pypdf backend: search-service/worker/stages/parse.py:268-282 (_parse_pdf_pypdf)
- Mistral OCR backend: search-service/worker/stages/parse.py:558-574 (mistral_pages_to_text)
- A chunk's page number is assigned by finding its start character offset (chunk_start_pos, found via full_text.find(node.text[:100]), with an index-based fallback if not found) against page_boundaries: first boundary whose end_pos >= position (search-service/app/indexing.py:20-30, get_page_number_for_position). So chunks that straddle a page boundary get attributed to the page where their first-100-chars start.
- For zh-language docs, boundaries are re-derived after OpenCC t2s normalization to keep offsets aligned (worker/stages/embed.py:24-50).

