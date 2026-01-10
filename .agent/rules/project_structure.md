# Project Structure & Organization

## Directory Standards
*   **Prototypes**: All functional code belongs in `hamal-ai/` (or similar top-level folders).
    *   Must maintain `backend/` (Python) and `frontend/` (React/Vite) separation.
*   **Concepts**: Documentation and ideation belong in `ventures/`.
    *   Use `concepts/`, `memory/`, and `directives/` subfolders for clarity.

## File Naming
*   **Python**: Snake_case for files (`main.py`, `data_processor.py`).
*   **frontend**: PascalCase for React components (`AgentStatus.tsx`), camelCase for logic (`apiClient.ts`).
*   **Docs**: Kebab-case/search-friendly names (`implementation-plan.md`).

## Dependency Management
*   **Backend**: Always update `backend/requirements.txt` when adding Python packages.
*   **Frontend**: Always update `frontend/package.json` (use `npm install --save`) for JS packages.
