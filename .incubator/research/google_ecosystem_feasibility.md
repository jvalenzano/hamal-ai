# Feasibility Report: Google Ecosystem Pivot

**Date:** 2026-01-10
**Verdict:** **Mixed Viability.** The "Consumer" tools (NotebookLM, Gems) lack APIs. The "Developer" tools (A2UI, Conductor) are ready.

## 1. Component Analysis

| Component | Status | Reality Check |
| :--- | :--- | :--- |
| **A2UI** | ✅ **Valid** | Open-source Google protocol for "Generative UI". Valid choice for the dashboard. |
| **Conductor** | ✅ **Valid** | Refers to "Gemini Conductor" (CLI extension). Aligns perfectly with our `directives` patterns. |
| **NotebookLM** | ⚠️ **Risk** | **No Public API.** Enterprise-only. We cannot programmatically "read" a NotebookLM source from an Agent without scraping (brittle). |
| **Gemini Gems** | ❌ **Blocker** | **No API.** Gems are strictly for the Gemini Chat App. We cannot embed a "Gem" into a custom React Dashboard. |

## 2. The Architectural Pivot
To achieve your visual roadmap, we must shift from **Consumer Tools** to **Developer Equivalents**:

*   **Instead of "NotebookLM":** We build a **Local RAG System** (using Vertex AI Search or simple Vector Store) that *mimics* NotebookLM's "Source Guide" feature.
*   **Instead of "Gems":** We build **Vertex Agents** (or LangGraph nodes) that *act* like Gems but give us JSON outputs for the A2UI dashboard.

## 3. Revised Stack Recommendation
*   **Frontend:** React + **A2UI** (for Generative Dashboards).
*   **Backend:** Google Cloud Run + **Vertex AI** (Agents).
*   **Orchestration:** **LangGraph** (as proposed).
*   **Workflow:** **Gemini Conductor** (for the "Plan-First" coding flow).
