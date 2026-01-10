# Obsidian Plugin POC (Experiment)

## Goal
Validate that we can programmatically append text to an Obsidian Daily Note without breaking the user's existing connections.

## Requirements
*   **Input:** Text string.
*   **Process:** Locate `Daily Notes` folder -> Find/Create today's file -> Append text under a formatted header.
*   **Output:** Updated Markdown file.

## Instructions for Builder
1.  Target a test vault, NOT your real vault first.
2.  Use standard Markdown I/O.
