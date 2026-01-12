# Hamal System Architecture

## 1. The Runtime Configuration
When you deploy to Render, you are not just "uploading files". You are provisioning a **Linux Container** (a lightweight Virtual Machine) that builds your specific environment from scratch.

### The Build Process (What you see in logs)
1.  **Provisioning**: Render allocates a server.
2.  **Cloning**: It pulls your code from GitHub.
3.  **Refining Dependencies**:
    *   **The "Heavy" Stuff**: You noticed `NVIDIA`, `Torch`, `CUDA` in the logs.
    *   **Why?**: Hamal uses `sentence-transformers` for local semantic search (finding similar projects). This library relies on **PyTorch**, a massive deep-learning framework. Even though we run on CPU, the standard packages include support for GPUs (NVIDIA CUDA), making the download size huge (~1-2 GB).
    *   **Result**: This is why the build takes 3-5 minutes. It's downloading the "brain" structure.
4.  **Snapshotting ("Uploading Build")**:
    *   Once everything is installed, Render takes a **Snapshot** of this entire environment (the "Image").
    *   It uploads this image to its internal registry.
    *   **Why?**: This is the "Save Game" point. Next time, it downloads this image instead of reinstalling everything.

## 2. The Execution Flow ("How it runs")
Once built, the start command (`python hamal.py serve`) triggers the following chain:

```mermaid
graph TD
    User((User/Public)) -->|HTTP Request| RenderLB[Render Load Balancer]
    RenderLB -->|Forward| FastAPI[FastAPI Web Server]
    
    subgraph "Hamal Application (The Container)"
        FastAPI -->|1. Receive CMD| Orchestrator[Orchestrator (hamal.py)]
        Orchestrator -->|2. Invoke| Agents[Agent Swarm]
        
        subgraph "Memory & Logic"
            Agents -->|3. Embed/Search| Torch[PyTorch/SentenceTransformers]
            Agents -->|4. Reason| LiteLLM[LiteLLM Proxy]
        end
    end
    
    LiteLLM -->|5. API Call| Anthropic[Anthropic API (Claude)]
    LiteLLM -->|5. API Call| OpenAI[OpenAI API (GPT-4)]
    
    Torch -.->|Local Compute| CPU[Server CPU]
```

## 3. Key Components
-   **FastAPI**: The "Front Door". It accepts web requests and talks to the underlying Python code.
-   **LiteLLM**: The "Universal Translator". It standardizes calls so we can swap between OpenAI, Anthropic, or even local models without code changes.
-   **PyTorch**: The "Local Muscle". It performs mathematical operations to understand text similarity (Embeddings) without needing an external API.

## 4. Security & Isolation
-   **API Keys**: stored in the process environment (`os.environ`). They never leave the server.
-   **Isolation**: The execution happens inside the container. If the code crashes, the container restarts. Files are ephemeral (unless we attach a disk), meaning each deploy starts fresh.

## 5. Build Caching (The "Smart" Part)
Render uses **Layer Caching** to optimize future deploys:
1.  **Dependencies**: If `requirements.txt` is unchanged, Render **skips** the heavy download. It reuses the cached layer from the previous build.
    *   *Result*: Deploys take ~30 seconds.
2.  **Code Changes**: If you modify `hamal.py` or add a feature, Render only copies the new code on top of the cached dependencies.
3.  **Full Rebuild**: Only happens if you touch `requirements.txt` (add a new library) or clear the cache manually.
