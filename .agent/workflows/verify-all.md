---
description: Run verification steps for the current prototype
---

// turbo
1.  **Backend Check**
    *   Navigate to `hamal-ai/backend`.
    *   Run `python -m py_compile main.py` to check for syntax errors.

// turbo
2.  **Frontend Check**
    *   Navigate to `hamal-ai/frontend`.
    *   Run `npm run build` to verify regular build.
    *   Run `npx tsc --noEmit` to check types.
