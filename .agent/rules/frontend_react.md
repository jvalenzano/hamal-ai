# React & Vite Standards

## Stack
*   **Framework**: React 18+ with TypeScript (Strict mode).
*   **Build Tool**: Vite (configure in `vite.config.ts`).

## Component Practices
*   **Functional Components**: Use `const Component = () => {}` syntax.
*   **Hooks**: Encapsulate complex state logic in custom hooks (e.g., `useAgentStatus`).
*   **Types**: Define interfaces for all props and API responses. Avoid `any`.

## Performance
*   Use `useEffect` sparingly; prefer derived state where possible.
*   Clean up subscriptions/intervals in `useEffect` return functions.
