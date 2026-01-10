# Research Synthesis: The "Incubator OS" Architecture
> **Date:** 2026-01-10
> **Status:** Architecture Validated
> **Verdict:** Novel Architecture. Build via Composition.

## 1. Executive Summary
The "LLM Council" (Claude, ChatGPT, Grok, Gemini) conducted a comprehensive sweep of the open-source landscape. **The consensus is unanimous:** No existing repository currently implements your specific "7-Agent + Directive-Based + Self-Healing" architecture.

*   **Novelty:** The combination of "Pre-Build Critique" (Skeptic Agent) and "Self-Healing Monorepo" (Docs updating Code) is a category-of-one.
*   **Strategy:** Do NOT fork a monolithic framework (like MetaGPT or Jedi). Do NOT build from scratch. **Build via Composition**—wiring together high-quality existing components on the Antigravity runtime.

## 2. The "Gap Analysis"
We analyzed 10+ frameworks. Here are the most relevant:

| Framework | What It Has | What It Lacks | Recommendation |
| :--- | :--- | :--- | :--- |
| **MetaGPT** | Best-in-class **Role Prompts** (PM, Architect). | Rigid waterfall workflow. No "Skeptic" loop. | **Fork the Prompts**, not the code. Port their PRD schema to our `directives/` folder. |
| **Jedi** | Correct **Topology** (Orchestrator + Specialized Agents). | Wrong Domain (Web3). Heavy Node.js stack. | **Adopt the Pattern.** Use Antigravity to replicate its "Specialist Swarm" structure. |
| **Sequa MCP** | **Self-Healing Documentation**. | Full venture context. | **Integrate Tool.** Use this generic MCP server to power our Self-Healing requirement. |
| **Startup Crew** | Good **Sequencing** (Idea -> MVP). | No parallel critique. No directive system. | Reference their sequence for our `active_protocol.md`. |

## 3. The Composition Architecture
Instead of a single codebase, we are building a **Venture Operating System** by composing these layers:

### Layer 1: The "Constitution" (Directives)
*   *Inspiration:* **PromptWare / Agent READMEs**
*   *Implementation:* A structured `directives/` folder serving as the "Source of Truth."
*   *Mechanism:* The AI reads `directives/001-vision.md` before writing a single line of code.

### Layer 2: The "Brain" (Orchestration)
*   *Platform:* **Google Antigravity + Claude Code**
*   *Why:* Antigravity provides the IDE/Terminal/Browser runtime natively. We do not need to build a custom runtime (like OpenDevin does).
*   *Agents:*
    *   **Researcher:** Powered by Gemini 1.5 Pro (Deep Reasoning).
    *   **Skeptic:** Powered by Claude 3.5 Sonnet (Nuanced Critique).
    *   **Builder:** Powered by Claude Code (CLI Execution).

### Layer 3: The "Memory" (Persistence)
*   *Tools:* **Sequa MCP + Obsidian MCP**
*   *Why:* Prevents "Context Rot."
*   *Mechanism:* 
    1.  User writes thought in Obsidian.
    2.  Agent drafts Directive.
    3.  Builder writes Code.
    4.  Sequa updates Docs.
    5.  Skeptic compares Docs vs Directive.

## 4. Immediate Next Steps (The "Monday Commit")
Based on this research, we must pivot from "Looking for a Repo" to "Assembling the Components."

1.  **Directives Schema:** Define the exact template for `directives/` (based on MetaGPT's PRD).
2.  **Tool Integration:** Install `@sequa-ai/sequa-mcp` (verified existence) to enable self-healing.
3.  **Council Boot:** Manually simulate the "Skeptic" loop on our first concept (Voice Interface).

## 5. Follow-Up Questions
1.  **Blocker Policy:** If the "Skeptic" Agent rejects a Directive (e.g., "This API is too expensive"), should it *hard block* the Builder, or just warn the User?
2.  **User Loop:** Do you want to be the "Judge" (breaking ties between Skeptic/Researcher) or the "CEO" (setting the vision and leaving)?
