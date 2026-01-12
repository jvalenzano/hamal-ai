# Agent Experience Design Spec
## Core Principle: Agents Surface During Execution

This document outlines the UX strategy for integrating Hamal's agent personas into the application. We avoid front-loading the roster as "documentation" and instead introduce agents organically during the pipeline execution.

### 1. The Pipeline Progress Component

The current progress bar/spinner should transform into a **vertical timeline** where each agent is represented by a "Spotlight Card."

#### States

1.  **Queued**
    *   **Appearance:** Collapsed, greyed out / low opacity.
    *   **Content:** Icon + Name + "Waiting..."
    *   **Goal:** Show the roadmap without distraction.

2.  **Active (The Spotlight)**
    *   **Appearance:** Expanded card, distinct accent-colored left border (3px).
    *   **Transitions:** Queued → Active expands with a 300ms ease-out.
    *   **Content:**
        *   **Header:** Agent Name + Role (e.g., "The Discovery Agent").
        *   **Status:** A one-liner description of current action (e.g., "Drilling into root causes...").
        *   **Activity Feed:** A scrolling log below the status.
            *   **Cap:** Show the 3 most recent thoughts. 
            *   **Overflow:** Older items fade out or collapse into "12 more actions..." (expandable on click).
    *   **Goal:** Create narrative momentum. Show *work*, not just waiting, without overwhelming the user.

3.  **Complete**
    *   **Appearance:** Collapsed to summary view. Green checkmark or accent-colored completion icon.
    *   **Transitions:** Active → Complete collapses with a slight delay (let the "done" moment linger).
    *   **Content:** Agent Name + Key Output Stat (e.g., "Identified 3 critical assumptions").
    *   **Goal:** Give a sense of accomplishment and tangible output.

4.  **Failed** (Error State)
    *   **Appearance:** Red border, distinct error icon. Collapsed to summary but expandable.
    *   **Content:** "The [Agent Name] hit a wall: [Error Message]." + Retry Action.
    *   **Microcopy:** "The Skeptic hit a wall: API rate limit exceeded. Retry?"
    *   **Goal:** Clearly communicate where the pipeline stopped and why.

### 2. Personality & Microcopy

Personality is conveyed through **text**, not cartoons. Using the `PipelineStatus` messages or a dedicated "thought stream":

*   **Generic:** "Running market research..."
*   **On-Brand:** "The Scout is scanning 47 competitor repositories..."

*   **Generic:** "Validation complete."
*   **On-Brand:** "The Skeptic found 2 critical flaws. You'll want to see this."

### 3. Visual Identity & Color Coding

Keep the UI professional. Use geometric icons or simple glyphs. Assign subtle accent colors for active states:

*   **🕵️‍♀️ The Discovery Agent (The Inquisitor)**
    *   **Color:** Gold/Yellow (#EAB308) - *Illuminating truth, distinct from Brand Orange.*
    *   **Icon:** Magnifying glass / Lightbulb

*   **🔭 The Research Agent (The Scout)**
    *   **Color:** Blue (Intel, exploration, horizon)
    *   **Icon:** Telescope / Binoculars / Radar

*   **⚖️ The Validation Agent (The Skeptic)**
    *   **Color:** Red/Coral (Warning, stop sign, critical review)
    *   **Icon:** Scales / Shield / X-mark

*   **🏗️ The Architecture Agent (The Blueprint)**
    *   **Color:** Teal/Cyan (Technical, precision, blueprint paper)
    *   **Icon:** Layers / GitBranch / Box - *Structural symbols, avoiding Compass (header conflict).*

*   **📝 The Summary Agent (The Closer)**
    *   **Color:** Purple (Royal, executive synthesis, finished product)
    *   **Icon:** Quill / Clipboard / Briefcase

### 4. The Roster Panel (Optional)

Do not create a main navigation tab for "The Team." Instead, offer a small **"View Roster"** button (e.g., in the footer or header help menu) that opens a slide-out panel.

*   **Content:** The full descriptions from `docs/AGENT_ROSTER.md`.
*   **Purpose:** For users who want the "lore" or backstory, but optional for utilization.

---

### Implementation Plan

#### 1. Backend (Python)
Define a standard status event schema in `agents/utils.py` or a new `agents/events.py` to ensure all agents report status identically.

```json
{
  "agent": "scout",
  "state": "active",  // or "queued", "complete", "error"
  "message": "Scanning for competitor repositories...",
  "stats": {
    "repos_found": 12,
    "papers_analyzed": 4
  },
  "timestamp": "2026-01-12T10:00:00Z"
}
```

#### 2. Frontend (React)
   a. **Create `AgentCard` Component:**
      - Props: `agent` (enum), `state` (enum), `activityLog` (array), `stats` (object).
      - Handles the 4 visual states (Queued, Active, Complete, Failed).
      - Encapsulates the specific color/icon logic for each agent.
      - Implements the expand/collapse transitions (300ms ease-out).

   b. **Refactor `PipelineProgress`:**
      - Replace current spinner/bar with a vertical stack of `<AgentCard />` components.
      - Map the "Global Status" coming from the backend to specific Agent states.

   c. **Add `useAgentStatus` Hook:**
      - Manage the complex state of which agents are done vs. active.
      - Handle the "Activity Feed" accumulation logic (capping at 3 items).

#### 3. Content Strategy
   - Write 5-8 microcopy variants per agent for specific activity messages to populate the backend events.

