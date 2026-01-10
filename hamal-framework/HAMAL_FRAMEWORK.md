# The Hamal Framework 🏭

> **Vision:** See [NORTH_STAR.md](/Users/jvalenzano/Projects/HAMAL/NORTH_STAR.md) for the high-level strategy.
> **Philosophy:** "We shape our tools, and thereafter our tools shape us."

**Hamal** is an agentic framework for validating solopreneur ideas. It forces a disciplined, evidence-based approach to product development, leveraging AI agents to do the heavy lifting of research, validation, and planning.

## The Phases

The framework moves an idea through 5 distinct phases. Do not skip phases.

### Phase 1: Research (`01-research/`)
*   **Goal:** Understand the problem space and competitors.
*   **Agent Workflow:** `run_workflow("research-idea")`
*   **Output:** `[idea]-research.md`

### Phase 2: Validation (`02-validation/`)
*   **Goal:** Test your assumptions using "Mom Test" principles.
*   **Agent Workflow:** `run_workflow("validate-idea")`
*   **Output:** `[idea]-validation.md`

### Phase 3: Architecture (`03-architecture/`)
*   **Goal:** Define *how* to build it (if validated).
*   **Agent Workflow:** `run_workflow("architecture-plan")`
*   **Output:** `[idea]-architecture.md`

### Phase 4: Prototyping (`04-prototyping/`)
*   **Goal:** Create the build specs for the MVP.
*   **Agent Workflow:** `run_workflow("prototype-spec")`
*   **Output:** `[idea]-spec.md` + `implementation_plan.md`

### Phase 5: Decision (`05-decision/`)
*   **Goal:** Commit to Build, Pivot, or Kill.
*   **Agent Workflow:** `run_workflow("go-no-go")`
*   **Output:** `[idea]-decision.md`

## How to Use

1.  **Start a New Idea:**
    ```bash
    # Create a tracking issue or file in your notes
    # Run the research workflow
    @agent run /research-idea
    ```

2.  **Review & Iterate:**
    *   Review the agent's output in `hamal-framework/01-research/`.
    *   Refine your "Shower Thought" based on data.

3.  **Proceed:**
    *   If the idea survives Research, move to Validation.
    *   `@agent run /validate-idea`

## The "Hamal" Philosophy

1.  **Code Last:** Writing code is the most expensive way to validate an idea. Do it last.
2.  **Agents First:** Use AI to simulate users, critics, and architects before you hire/build real ones.
3.  **Evidence over Intuition:** Make decisions based on the `Validation Score`, not your gut.
