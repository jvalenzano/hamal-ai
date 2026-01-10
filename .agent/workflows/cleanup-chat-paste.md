---
description: Clean up markdown files that were copy-pasted from chat/AI outputs
---

# Chat-Pasted Markdown Cleanup

Use this workflow when a markdown file was copy-pasted from a chat interface (Claude, ChatGPT, etc.) and contains unnecessary formatting artifacts.

## What to Remove

1. **Outer code fence wrappers** — ` ```markdown ` at the start and ` ``` ` at the end that wrap the entire document
2. **Redundant filename titles** — `# FILENAME.md` at line 1 when the file is already named that
3. **Chat artifact labels** — `**Output:**`, `**Response:**`, `[Artifact]`, etc.
4. **Nested ` ```markdown ` blocks** — example output blocks that use ` ```markdown ` / ` ``` ` when the content is already valid markdown (headers, lists, tables)

## What to Keep

- **Legitimate code blocks** — Python (` ```python `), YAML (` ```yaml `), JSON (` ```json `), shell commands
- **ASCII diagrams** — need plain ` ``` ` to preserve monospace formatting
- **Mermaid diagrams** — ` ```mermaid `
- **Actual markdown content** — headers, lists, tables, links, bold/italic text

## Steps

// turbo-all

1. View the file to analyze its structure
2. Identify all instances of:
   - Outer ` ```markdown ` wrapper (usually lines 1-3)
   - Nested ` ```markdown ` / ` ``` ` pairs around example outputs
   - Chat-specific labels or annotations
3. Report findings to user before making changes
4. Remove unnecessary wrappers while preserving:
   - The actual content inside the blocks
   - Legitimate code/diagram fences
5. Verify the cleaned file renders correctly as markdown
