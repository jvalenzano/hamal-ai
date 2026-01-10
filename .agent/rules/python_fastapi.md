# Python & FastAPI Standards

## Code Quality
*   **Type Hints**: Strictly use Pydantic models for all API schemas (Inputs/Outputs).
*   **Async/Await**: Use `async def` for all route handlers and I/O bound operations (like LiteLLM calls).
*   **Docstrings**: Include basic docstrings for complex logic, but avoid stating the obvious.

## Framework Patterns
*   **LiteLLM**: Use `litellm` for all AI inference (as seen in `requirements.txt`).
*   **Environment**: Load config via `python-dotenv`. Never hardcode keys.
*   **Routing**: Keep `main.py` clean. If routes exceed 10, split into `api/routes/`.

## Error Handling
*   Use `HTTPException` with clear status codes (400, 404, 500).
*   Wrap AI calls in try/except blocks to handle API failures gracefully.
