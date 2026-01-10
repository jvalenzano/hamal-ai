# LLM Council Tutorial: What It Is, How It Works, and How It Fits Your Incubator

## 1. Scraped Metadata (From the Tutorial)

From the YouTube page and transcript:

- **Title:** *OpenAI's NEW LLM Council – Here’s how to use it*  
- **Creator:** Nick Puru | AI Automation  
- **Channel focus:** AI automation, AI agencies, AI for business owners  
- **Publish date:** December 26, 2025  
- **Duration:** ~13 minutes (0:13:02)  
- **High-level intent:**  
  - Explain Andrej Karpathy’s open-source **LLM Council** project  
  - Show non-technical users how to set it up using **Cursor** (and note that similar could be done with Google **Antigravity** / other AI IDEs)  
  - Position it as a **“free AI board of directors”** for important business decisions  

Key external components used in the tutorial:

- **GitHub repo:** Karpathy’s LLM Council project (user clones via Cursor)
- **Model router:** **OpenRouter** (to access multiple frontier models with one API)
- **Models demoed:** GPT variants, Claude, Gemini, Grok, Llama (configurable)
- **Environment:** Cursor IDE, natural-language-driven setup (no manual terminal work in the tutorial)

***

## 2. Core Mechanics of LLM Council (As Described in the Video)

The tutorial outlines a very clean four-stage pipeline that matches what you’ve been doing manually with an “LLM council”:

### Stage 1 – First Opinions

- Your **question** is sent **in parallel** to multiple frontier models (e.g., GPT, Claude, Gemini, Grok).
- Each model:
  - Answers **independently**
  - **Cannot see** the others’ answers at this stage
- You can inspect each answer individually (e.g., tabbed view).

Semantically: “one question → N independent answers.”

***

### Stage 2 – Review (Ranking Phase)

- Each model is now shown **all the other responses**.
- **Identities are anonymized**:
  - Claude doesn’t know which answer was GPT
  - GPT doesn’t know which was Gemini, etc.
- Each model **ranks** the answers based on:
  - Accuracy
  - Insightfulness / quality

This is explicitly to avoid “reputation bias” (e.g., always trusting GPT because “it’s GPT”).

***

### Stage 3 – Critique Phase

- Models now go beyond ranking:
  - They **actively criticize** the other responses.
  - They point out:
    - Hallucinations
    - Logical gaps
    - Weak assumptions
- This is where real “peer review” happens:
  - If one model hallucinated a fact, others can call it out.
  - You get a list of **identified weaknesses**, not just a ranking.

***

### Stage 4 – Chairman Synthesis

- A designated **“chairman” model** (typically the one you trust most for synthesis) reads:
  - All original answers
  - All rankings
  - All critiques
- It then produces a **single synthesized answer** that:
  - Pulls the best elements from each model
  - Incorporates critiques and risk/ROI reasoning
- Net result: A response that has effectively been **pressure-tested** by several distinct model architectures.

The tutorial repeatedly frames this as:

> A **board of AI directors** for any high-stakes decision.

***

## 3. Setup Flow Highlighted in the Tutorial

The actual implementation steps demonstrated:

1. **Clone the repo in Cursor**  
   - Use “Clone a repository” with Karpathy’s GitHub URL.
   - Cursor opens the project as a new workspace.

2. **Use natural language to run the setup**  
   - Copy the “setup” block from the GitHub README into Cursor’s chat.
   - Say something like: *“I need you to set this up for me.”*  
   - Cursor:
     - Installs dependencies
     - Configures the environment
     - Requests permissions to modify files

3. **Configure OpenRouter API key**
   - Create an API key on OpenRouter.
   - Paste it into the config / env as instructed.
   - This is what lets you hit multiple models with one endpoint.

4. **Customize council composition**
   - In natural language:
     - “Change the council models to GPT-4.0, Claude 4.5 Sonnet, and a Llama model; update the config files.”
     - “Set GPT 5.1 as the chairman model for final synthesis.”
   - Cursor edits the config accordingly.

5. **Cost considerations**
   - Each “council meeting” uses:
     - N model calls + 1 chairman call
   - So roughly **5× the tokens** of a single query if you have 4 council models + 1 chairman.
   - In practice, they quote:
     - About **$0.05–$0.20 per council session**, depending on length.
   - Framed as:
     - Trading **a few cents** for **multi-perspective validation on decisions** that might cost thousands.

***

## 4. How This Relates to Your “LLM Council” Practice

You’ve already been doing an informal version of this:

- Ask **multiple LLMs (Claude, GPT, Gemini, etc.)** the same question.
- Compare their answers.
- Use your own judgment to synthesize or let them “debate”.

LLM Council operationalizes that as code:

- **Formalizes** parallel querying and structured critique.
- **Automates**:
  - Orchestrating requests
  - Anonymizing sources
  - Ranking/critique logic
  - Generating a single final answer
- **Abstracts out the router** via OpenRouter so you’re not hand-wiring each vendor.

It is *exactly* the “multi-LLM research council” pattern, encoded as a reusable engine.

***

## 5. Fit With Your Startup Incubator Architecture

You’re building:

- A **7-Agent Persona System** (Researcher, Skeptic, Builder, Storyteller, etc.).
- A **Directive-based** monorepo (natural language specs and ADRs drive prototypes).
- A **self-healing repo** with rich documentation and AI reading the “why” before coding.
- Stack including **Antigravity, Claude Code, local markdown memory (Obsidian)**.

Here’s how LLM Council conceptually and practically fits.

### 5.1 Conceptual Match

LLM Council gives you **orthogonal diversity** to what you already have:

- Your 7 agents = **different roles / thinking styles** over (likely) the same base model (or same vendor).
- LLM Council = **different underlying models** (GPT, Claude, Gemini, Llama) on **the same role/question**.

Combined:

- Horizontal diversity: **Researcher vs Skeptic vs Storyteller…**
- Vertical diversity: Each role can internally consult a **mini-council of models**.

That’s a powerful combo for a “Founder’s Brain”.

***

### 5.2 Concrete Integration Patterns

Here are a few concrete ways to use (or mirror) LLM Council inside your incubator.

#### Pattern A – “External Advisor Council” Agent

- Add a dedicated persona in your system: **AdvisorCouncilAgent**.
- Responsibilities:
  - For **high-stakes questions** (market entry, big pivots, capex decisions), this agent:
    - Calls out to the LLM Council endpoint (or an internal clone).
    - Provides:
      - Problem statement (from your `/directives/problem_statement.md`)
      - Current hypothesis/plan (from Builder / Skeptic outputs)
    - Receives:
      - Ranked model opinions
      - Critique summary
      - Chairman synthesis
  - Writes a new artifact:
    - `/directives/advisor_council_report.md`

Role in the pipeline:

- Founder → 7 internal agents → AdvisorCouncilAgent (cross-model council) → final recommendation.

This keeps the **multi-LLM orchestration encapsulated** in one place.

***

#### Pattern B – Councils Inside Specific Personas

For certain agents, instead of a single-model call, you can embed a council:

- **ResearcherAgent**:
  - Uses LLM Council to ask: “What are the major market dynamics and risks of X?”
  - Council results get distilled into `market_research.md`.
- **SkepticAgent**:
  - Uses a council specifically prompted to **attack the idea** from multiple angles.
  - Outcome: `risk_register.md`.
- **FinancierAgent**:
  - Council evaluates pricing models, unit economics, and financial risk on a scenario.

This turns each high-value agent into a **multi-model meta-agent**.

***

#### Pattern C – Council for ADR Validation

You specifically care about ADR-style directives in `/directives/`.

- For each **major ADR** (architecture decision, go/no-go on a product direction), you can:
  - Pass the ADR markdown into a council.
  - Ask:
    - “Critique this ADR as if you were a seasoned CTO and investor.”
    - “Highlight assumptions, risks, and missing failure scenarios.”
  - Store the result in:
    - `/directives/adr_council_review.md`.

This gives you an auditable trail of **“this decision was pressure-tested by multiple top models.”**

***

### 5.3 Relationship to Antigravity / Claude Code

The tutorial shows it in **Cursor**, but notes other AI IDEs like **Antigravity** are viable:

- In your stack:
  - Use **Antigravity** or **Claude Code** exactly like Cursor:
    - Clone Karpathy’s repo.
    - Use natural language to wire up:
      - OpenRouter config (or your preferred router)
      - Council composition (model list)
    - Wrap LLM Council behind a small internal API / CLI so your agents can programmatically call it.

Your future flow might look like:

- Antigravity orchestrates:
  - Local repo + Obsidian vault.
  - Internal multi-agent system.
  - External LLM Council calls over HTTP.

***

## 6. Strengths and Limitations for Your Use Case

### 6.1 Strengths

- **Embeds your manual best practice**  
  It formalizes what you’re already doing: multi-LLM consultation, cross-checking, synthesis.

- **Aligns philosophically with your “AI board of directors” vision**  
  The tutorial literally uses that metaphor.

- **Simple, composable primitive**  
  LLM Council exposes a clear, reusable contract:
  - Input: question + context.
  - Output: per-model responses, rankings, critique, synthesis.

- **Anonymized critique is a genuinely good design idea**  
  You can borrow this idea both for:
  - Cross-model councils.
  - Your **internal personas** (they don’t need to know which agent wrote which draft when critiquing each other).

- **Cost is acceptable for high-stakes decisions**  
  Council usage at **$0.05–$0.20/decision** is cheap compared to:
  - Consulting, mis-built features, or wrong product directions.

***

### 6.2 Limitations / Gaps vs Your Architecture

Relative to your planned “Founder’s Brain”:

1. **Not role-diverse, only model-diverse**  
   - All council members answer the **same role** question.
   - Your system needs **role diversity** (research vs narrative vs skeptic vs builder), not just vendor diversity.

2. **No persistent knowledge / monorepo integration**  
   - LLM Council as shown doesn’t:
     - Read from a long-term venture memory.
     - Write into a structured repo of ADRs, research docs, etc.
   - It’s a **stateless deliberation engine**, not a knowledge system.

3. **Not local-first**  
   - Depends on **OpenRouter + cloud LLMs**.
   - For your local-first / Obsidian-oriented vision:
     - You may want to copy the **architecture** but plug in:
       - Local Llama variants.
       - Self-hosted API frontends.
   - Or allow a “local-only” mode that runs multiple local models.

4. **No explicit tooling around product development lifecycle**  
   - LLM Council is question → debate → answer.
   - Your incubator needs:
     - Idea pipeline management
     - Multi-step validation workflow
     - Prototype generation
     - Continuous learning/feedback loops

So: it’s **not** a complete venture-building framework. It’s a **sharp sub-component** you can embed.

***

## 7. Opinionated Take: How You Should Use (or Copy) LLM Council

Short version:

- **Yes, this is absolutely worth leveraging.**
- But treat it as **one building block** inside your incubator, not the core architecture.

Concretely:

1. **Use Karpathy’s repo as a reference implementation**  
   - Study how it:
     - Structures council stages.
     - Implements anonymity.
     - Handles ranking/critique.
   - Either:
     - Integrate it directly (wrap as an internal service), or
     - Reimplement the pattern in your own stack (especially if you want local-first behavior).

2. **Create a dedicated “Model Council” agent in your 7-agent system**  
   - This agent is called only for **expensive / consequential decisions**:
     - Market entry
     - Major product pivots
     - Huge build vs buy choices
   - It queries multiple models via LLM Council (or your variant), then:
     - Writes structured findings into your `/directives/` folder.
     - Feeds that back to Skeptic, Builder, Storyteller, etc.

3. **Borrow anonymized critique and ranking**  
   - Apply this idea internally:
     - When your 7 personas review each other’s outputs, strip identities during critique.
     - Prevent “oh the Builder said this so it must be right” style bias.

4. **Be strategic about where you pay the 5× token cost**  
   - Don’t run *every* prompt through a council:
     - Use single high-quality models for day-to-day work (research summaries, routine critiques).
     - Reserve councils for:
       - ADR validation
       - Launch decisions
       - Strategy docs / investment memos.

5. **Future-proof with pluggable model backends**  
   - Architect your system so “council membership” is configuration-driven:
     - Today: OpenRouter to GPT/Claude/Gemini.
     - Later: mix in:
       - Local Mistral / Llama.
       - Organization-hosted fine-tuned models.

***

## 8. Bottom Line

The tutorial is a clear, practical walkthrough of an open-source implementation of exactly the **“LLM council”** pattern you care about:

- Multi-model answers → anonymized review → critique → chairman synthesis.

For your “AI-Native Founder’s Brain”:

- **Use LLM Council as a sub-module**:
  - An **External Advisor Council** agent that your 7 personas can consult.
- **Copy its good ideas**:
  - Anonymous critique
  - Structured four-stage pipeline
  - Configurable composition of committee members
- **Extend beyond it**:
  - Role-diverse agents
  - Directive-driven monorepo
  - Local-first, Obsidian-backed memory
  - Continuous venture lifecycle, not just one-off answers.

So: it’s **not** your incubator in a box, but it is almost the perfect **council engine** to plug into it.