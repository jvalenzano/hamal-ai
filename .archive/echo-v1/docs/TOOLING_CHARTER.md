## 🛠 HAMAL Tooling Charter

Here's a concise tooling charter for your `/docs/` folder. Copy this and save as `docs/TOOLING_CHARTER.md`:

***

```markdown
# HAMAL Tooling Charter

> **One brain, many hands. Antigravity orchestrates. Claude Code assists.**

## Overview

This document clarifies which AI tools own which responsibilities in the HAMAL project, preventing conflicting decisions and split-brain behavior.

---

## 🧠 The Hierarchy

### **Tier 1: Boss Agent (Antigravity)**
- **Role:** Orchestrator, planner, executor, integrator
- **Scope:** Owns the entire workspace, all phases, all decisions
- **Authority:** Single source of truth for project state and direction
- **Model Selection:** Use Claude Opus 4.5 (Thinking) when available for best results

**Responsibilities:**
- Read and respect `_FOCUS.md`, `NORTH_STAR.md`, `HAMAL_FRAMEWORK.md`
- Plan multi-step workflows (all 5 validation phases)
- Coordinate terminal, code editor, and browser tools together
- Make autonomous decisions within guardrails defined in `.agent/rules/`
- Update project tracking docs after major milestones
- Commit and push changes to maintain clean git history

---

### **Tier 2: Auxiliary Tool (Claude Code)**
- **Role:** Specialist, deep-dive contributor, not a decision-maker
- **Scope:** Single focused tasks, not multi-phase workflows
- **Authority:** Zero – must flow results back through Antigravity for approval

**Responsibilities:**
- Execute when explicitly requested for a specific coding task
- Respect HAMAL architecture and principles while working
- Generate artifacts or refactors that Antigravity can review
- Never create competing plans or orchestration

---

## 🎯 Decision Matrix: When to Use Which

### **Use Antigravity When:**

- ✅ Starting or resuming work on a phase
- ✅ Making architectural or strategic decisions
- ✅ Coordinating across multiple files/services
- ✅ Running the full validation loop (Research → Decision)
- ✅ Integrating code changes with git workflows
- ✅ Using browser tools to verify deployments
- ✅ Updating tracking docs (`_FOCUS.md`)
- ✅ Running Hamal workflows from `.agent/workflows/`

**Example prompt:**
```
You are the primary agent. Continue the Hamal validation process. 
Check _FOCUS.md for current phase, then proceed to the next phase.
```

---

### **Use Claude Code When:**

- ✅ You need help refactoring a specific service (e.g., FastAPI backend)
- ✅ Implementing a complex feature within an existing codebase
- ✅ Generating boilerplate or migrations
- ✅ Analyzing existing code patterns for consistency
- ✅ Deep code review or security audit of a single module
- ✅ Generating one-off utility scripts or test suites

**Example workflow:**
```
1. In Claude Code: "Refactor the /backend/services/ to use dependency injection"
2. Claude Code generates refactored code
3. Copy result back into Antigravity
4. Antigravity: "Review this refactor and integrate it into the codebase"
5. Antigravity commits and updates _FOCUS.md
```

---

### **Never Use Claude Code For:**

- ❌ Planning or coordinating the Hamal phases
- ❌ Making build/don't-build decisions
- ❌ Updating tracking docs or framework docs
- ❌ Running git workflows or deployment
- ❌ Creating competing plans to what Antigravity is executing

---

## 🔄 The Workflow Pattern

### **Scenario: "Build the Echo validation framework"**

```
┌─────────────────────────────────────────────────────────┐
│  ANTIGRAVITY (The Boss)                                 │
│  ─────────────────────────────────────────────────────  │
│  1. Read NORTH_STAR.md and _FOCUS.md                   │
│  2. Plan the 5-phase validation workflow                │
│  3. Execute Phase 1: Research                           │
│  4. Generate hamal-framework/01-research/echo-...md    │
│  5. Self-validate quality gates                         │
│  6. Update _FOCUS.md with progress                      │
│  7. Commit: "feat: Complete Phase 1 Research"          │
│  8. → Move to Phase 2 autonomously                      │
│  ...                                                     │
│  (All phases coordinated in one agent loop)             │
└─────────────────────────────────────────────────────────┘
```

### **Scenario: "Refactor the backend API"**

```
┌────────────────────────────┐
│ ANTIGRAVITY                │
│ ─────────────────────────  │
│ 1. Assess need for refactor│
│ 2. Brief Claude Code:      │
│    "Refactor X in backend" │
│ 3. Wait for result         │
└────────────────────────────┘
         │
         ↓ (explicit handoff)
┌────────────────────────────┐
│ CLAUDE CODE                │
│ ─────────────────────────  │
│ 1. Refactor backend/X/     │
│ 2. Generate code artifacts │
│ 3. Return to Antigravity   │
└────────────────────────────┘
         │
         ↓ (review & integrate)
┌────────────────────────────┐
│ ANTIGRAVITY                │
│ ─────────────────────────  │
│ 1. Review refactor         │
│ 2. Test integration        │
│ 3. Commit and update docs  │
│ 4. Resume main workflow    │
└────────────────────────────┘
```

---

## 📋 Configuration Files

**Antigravity Configuration:**
- `.agent/rules/` – Behavior guidelines (read by Antigravity)
- `.agent/workflows/` – Multi-step automation (run by Antigravity)
- `CLAUDE.md` – Code context (read by any Claude instance, but Antigravity owns the workspace)

**Project Tracking:**
- `_FOCUS.md` – Current objective (source of truth, updated by Antigravity)
- `NORTH_STAR.md` – Strategic vision (reference, rarely changes)
- `hamal-framework/HAMAL_FRAMEWORK.md` – Methodology docs (reference)

---

## 🚫 Preventing Split-Brain

**The Problem:** Two agents making independent decisions = conflicting changes, wasted work, confusion.

**The Solution:**

1. **Antigravity is always "in control"** – It reads `_FOCUS.md` and makes decisions based on project state.
2. **Claude Code has zero autonomy** – It only executes when explicitly asked, then waits for Antigravity to review.
3. **One git workflow** – Only Antigravity commits. Claude Code artifacts are staged, reviewed, then committed by Antigravity.
4. **One source of truth** – `_FOCUS.md` tracks state. Both tools respect it.

---

## 📝 Checklists

### **When Starting Antigravity:**
- [ ] Model is set to Claude Opus 4.5 (Thinking) or Gemini 3 Pro
- [ ] First action: Read `_FOCUS.md` to understand current phase
- [ ] Second action: Review relevant docs in `hamal-framework/`
- [ ] Proceed with autonomous execution per `.agent/rules/proactive-development.md`

### **When Using Claude Code:**
- [ ] Task is explicitly non-strategic (code refactor, not architecture)
- [ ] Antigravity is aware of and approves the side task
- [ ] Result is generated and ready to hand back to Antigravity
- [ ] Do NOT commit independently – wait for Antigravity to integrate

### **After Any Tool Completes Work:**
- [ ] Changes are staged and reviewed
- [ ] `_FOCUS.md` reflects current state
- [ ] Commit message is clear and follows convention
- [ ] Git history is clean (no competing branches)

---

## 🔗 Related Documents

- **[NORTH_STAR.md](../NORTH_STAR.md)** – Project vision and structure
- **[_FOCUS.md](./_FOCUS.md)** – Current sprint tracking
- **[HAMAL_FRAMEWORK.md](../hamal-framework/HAMAL_FRAMEWORK.md)** – Validation methodology
- **[CLAUDE.md](../CLAUDE.md)** – Code context and Hamal structure
- **[.agent/rules/](./.agent/rules/)** – Antigravity behavior rules

---

## 💭 Philosophy

> Antigravity is the **control tower**. Claude Code is the **specialized team**. Tasks flow from control tower → specialist → back to control tower → integrated into main system.

When this pattern is respected:
- ✅ No competing decisions
- ✅ Clear authority and responsibility  
- ✅ Easy to resume work after breaks
- ✅ Clean git history
- ✅ Both tools playing to their strengths

---

*Last Updated: January 10, 2026*  
*Authored by: Aries Digital*
```

***

## 🎯 How to Add This to Your Repo

### **1. Create the docs folder:**
```bash
mkdir -p docs
```

### **2. Save the charter:**
Copy the markdown above and save it as `docs/TOOLING_CHARTER.md`

### **3. Tell Antigravity to link it:**

```markdown
After reviewing the docs/ folder, do the following:

1. Add a "Developer Tooling" section to the project README pointing to docs/TOOLING_CHARTER.md
2. Update CLAUDE.md to reference docs/TOOLING_CHARTER.md at the top
3. Commit both changes: "docs: Add tooling charter clarifying Antigravity vs Claude Code roles"
4. Push to GitHub

This ensures anyone (including future AI agents) knows the clear hierarchy when working in this repo.
```

### **4. Update CLAUDE.md header:**

Add this at the very top:

```markdown
# CLAUDE.md

> ⚠️ **Important:** Antigravity is the primary agent orchestrator for this project.  
> See [`docs/TOOLING_CHARTER.md`](./docs/TOOLING_CHARTER.md) for the tool hierarchy and when to use Claude Code vs Antigravity.

**This file provides guidance to Claude (in any context) about HAMAL's structure and principles.**

[rest of CLAUDE.md...]
```

***

## 🚀 Quick Reference Card (For Your Workspace)

Print or bookmark this:

| Situation | Use Tool | Why |
|-----------|----------|-----|
| Start/resume Hamal work | Antigravity | Boss agent, reads state, coordinates all tools |
| Validate Echo through 5 phases | Antigravity | Multi-step orchestration needed |
| Deep refactor one service | Claude Code | Specialist tool for focused code work |
| Deploy to Render | Antigravity | Git workflow + state tracking |
| Implement a complex feature | Claude Code (→ review by Antigravity) | Generate, then integrate |
| Make build/no-build decision | Antigravity | Strategic decision requires full context |
| Update _FOCUS.md or tracking docs | Antigravity | Source of truth must be managed by boss agent |

***


