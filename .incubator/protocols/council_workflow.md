# Protocol: The Council Manual Boot

> **Status:** Manual Simulation
> **Goal:** Run the "Thought Loop" before the "Build Loop".

## The Workflow

### Phase 1: Research (The "PM")
1.  **Trigger:** User has an ID in `_FOCUS.md`.
2.  **Action:** Create a file `ventures/echo/directives/active/00X-feature-name.md`.
3.  **Prompt (Researcher):**
    > "I am the Product Manager. Fill out sections 1, 2, and 3 of this directive based on the user's concept. Be specific."

### Phase 2: Tribunal (The "Skeptic")
1.  **Trigger:** Directive exists.
2.  **Action:** Open the Directive.
3.  **Prompt (Skeptic):**
    > "I am the Skeptic. Review `00X-feature-name.md`. Fill out Section 4 (Risks). Be harsh. If the risks are critical, add a 'BLOCKED' tag to the status."

### Phase 3: The Verdict (The "Founder")
1.  **Action:** User reads Section 4.
2.  **Decision:**
    *   *Override:* Rewrite Section 4 as "Risk Accepted" and change Status to "Active".
    *   *Pivot:* Rewrite Section 2 better.
    *   *Kill:* Move file to `archive/`.

### Phase 4: Build (The "Engineer")
1.  **Trigger:** Status is "Active".
2.  **Action:** Run the Builder Agent.
3.  **Prompt:**
    > "Implement `00X-feature-name.md` into `ventures/echo/concepts/`. Do not deviate from the spec."
