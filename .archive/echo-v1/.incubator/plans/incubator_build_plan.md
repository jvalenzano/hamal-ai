# Build Plan: The Incubator OS (Phase 1)

**Goal:** Transform the repo from a "Project Workspace" to a "Venture Building System."
**Driver:** The insight that *Execution > Validation*.

## 1. The Core Infrastructure (`.incubator/`)
This folder is the "Product" we are building. It must be venture-agnostic.

*   [ ] **Create Directory Base:**
    *   `.incubator/skills/` (The Tools)
    *   `.incubator/agents/` (The Team)
    *   `.incubator/protocols/` (The Rhythm)

*   [ ] **Define the "Execution Protocol":**
    *   Create `.incubator/protocols/execution_rhythm.md`.
    *   *Content:* Defines the Weekly Review, The Metric that Matters, and the Monday Commit.

## 2. The Skill pods
We need to refactor existing ideas into "Skills" that the OS can call.

*   [ ] **Skill: `llm_council`**
    *   Create `.incubator/skills/llm_council/`.
    *   Add `skill.yaml` (Defines inputs: Question, Context).
    *   Add `system_prompt.md` (The "Board of Directors" persona).

## 3. The Migration of Echo (`ventures/echo/`)
Echo becomes "Client Zero" for the OS.

*   [ ] **Move Specifics:**
    *   `directives/` (Echo spec) -> `ventures/echo/directives/`.
    *   `prototypes/` -> `ventures/echo/concepts/`.
*   [ ] **Link to OS:**
    *   Create `ventures/echo/active_protocol.md` that *imports* the Execution Protocol from the OS.

## 4. Execution Order
1.  **Refactor Structure:** Move files to their new homes (OS vs Venture).
2.  **Define Protocol:** Write the `execution_rhythm.md` based on the research.
3.  **Validate:** Run a manual "Week 1 Review" for Echo using the new protocol.
