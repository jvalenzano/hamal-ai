---
trigger: always_on
---

# Python & FastAPI Standards

## Code Quality
*   **Type Hints**: Use Pydantic models for API schemas when helpful.
*   **Async/Await**: Use `async def` for route handlers and I/O bound operations.
*   **Docstrings**: Include basic docstrings for complex logic only.

## Framework Patterns
*   **LiteLLM**: Use `litellm` for all AI inference.
*   **Environment**: Load config via `python-dotenv`. Never commit API keys.
*   **Routing**: Keep `main.py` clean. Split into `api/routes/` if needed.

## Error Handling
*   Use `HTTPException` with clear status codes (400, 404, 500).
*   Wrap AI calls in try/except blocks.

> **POC Exception:** Hardcoded values are acceptable during prototyping. See `KEEP_IT_SIMPLE.md`.
