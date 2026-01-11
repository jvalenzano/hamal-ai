# Echo Repository Strategy: Context-Rich Monorepo

## The Core Philosophy
**"How does the Brain (docs) connect to the Body (code)?"**

We operate as a **Context-Rich Monorepo**. We do not separate documentation (`docs`) from source code (`src`) into different repositories.

**Why:** AI agents (Anti-Gravity/Claude) need to "read" the Brand Narrative, Research, and Critiques to write code that aligns with the product vision. Separating them breaks the context window.

## The Evolution Path

### Phase 1: The Sandbox (`prototypes/`)
*   **Status:** **ACTIVE**
*   **Purpose:** Throwaway code, Proof-of-Concepts (POCs), "Spikes".
*   **Rule:** Code here is experimental. No strict linting or testing requirements.
*   **Workflow:**
    1.  Update `directives/product_spec.md` with intent.
    2.  Agent builds a script in `prototypes/` (e.g., `voice_capture_poc/`).
    3.  Validate feasibility.

### Phase 2: The Directives Bridge (`directives/`)
*   **Status:** **ACTIVE**
*   **Purpose:** The "API" between the Product Owner and the AI Builder.
*   **Rule:** **Don't just write code. Write the Directive first.**
*   **Components:**
    *   `product_spec.md`: The living specification.
    *   `architecture_decisions/`: ADRs defining *how* we build.

### Phase 3: The Production App (`src/`)
*   **Status:** **FUTURE** (Do not use yet)
*   **Purpose:** The "real" application.
*   **Rule:** Code graduates here only after validation in `prototypes/`.

## Directory Structure Map

```text
echo-product-workspace/
├── directives/          # THE BRAIN: Specs & Architecture Decisions
├── research/            # THE CONTEXT: Market Data & Feasibility
├── prototypes/          # THE SANDBOX: Messy Experiments & POCs
├── src/                 # THE BODY: Production Code (Future)
└── logs/                # THE MEMORY: Decisions & Progress Logs
```
