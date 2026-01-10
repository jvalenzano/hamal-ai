---
description: Scaffold a new prototype tailored to the Hamal workspace pattern
---

1.  **Setup Directory**
    *   Ask for the prototype name (e.g., `project-nexus`).
    *   Create directory: `[name]/`
    *   Create subdirectories: `[name]/backend`, `[name]/frontend`.

2.  **Scaffold Backend**
    *   Create `backend/requirements.txt` with `fastapi`, `uvicorn`, `litellm`.
    *   Create basic `backend/main.py` Hello World.
    *   Create `backend/Dockerfile`.

3.  **Scaffold Frontend**
    *   Initialize Vite app in `frontend`: `npm create vite@latest . -- --template react-ts`.
    *   Install dependencies.

4.  **Finalize**
    *   Add a root `README.md` for the prototype.
