# Keep It Simple: Hamal Development Manifesto

**This is a proof-of-concept, not production software.**

Our goal is to **validate that agent swarms save time**, not build enterprise-grade infrastructure. Every technical decision should optimize for **speed of learning**, not scalability, security, or elegance.

## Core Principles

### 1. **Functional > Perfect**
- Hardcode values instead of building config systems
- Use `.env` files, not secret managers
- JSON files in `/data`, not databases (until we need search)
- Print statements for debugging, not observability platforms

### 2. **Prototype-Grade Code Is Fine**
- No CI/CD pipelines (deploy manually)
- No test coverage requirements (manual testing on real projects)
- No error handling beyond try/catch (crash loudly, fix what breaks)
- No type hints or linting (unless it helps you think)

### 3. **Agents First, Infrastructure Later**
- **Spend 80% of time tuning prompts**, 20% on code structure
- If an agent isn't useful, delete it—don't optimize it
- Prove the concept with ugly code, refactor if it works

### 4. **Ship Weekly, Kill Early**
- Every Friday: Does this save time? Yes → continue. No → kill.
- If Week 2 doesn't improve on Week 1, stop and reassess
- No sunk cost fallacy: 10 hours wasted is better than 40

### 5. **No Premature Abstraction**
- Don't build "agent frameworks"—write scripts that call APIs
- Don't build "plugin systems"—copy/paste code for now
- Don't build "reusable libraries"—solve the problem in front of you

## What "Simple" Looks Like

### ✅ **DO THIS:**
```python
# discovery.py - One file, does one thing

import anthropic
import os

def discover_problem(charter_text):
    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
    
    # Hardcoded prompt (iterate this 10 times before abstracting)
    response = client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=2000,
        messages=[{
            "role": "user", 
            "content": f"Extract the core problem from this charter:\n\n{charter_text}"
        }]
    )
    
    return response.content.text

# Test it
if __name__ == "__main__":
    with open("ranger_charter.txt") as f:
        result = discover_problem(f.read())
    print(result)
```

**Why this is good:**
- Runs in 30 seconds
- Tests the prompt immediately
- No classes, no config, no abstractions
- Easy to throw away if prompt doesn't work

---

### ❌ **DON'T DO THIS:**
```python
# agents/base.py - Abstract base class
class BaseAgent(ABC):
    def __init__(self, config: AgentConfig, logger: Logger, metrics: MetricsCollector):
        self.config = self._validate_config(config)
        self.logger = logger
        self.metrics = metrics
        
    @abstractmethod
    def execute(self, input: AgentInput) -> AgentOutput:
        pass
    
    def _validate_config(self, config: AgentConfig) -> AgentConfig:
        # 50 lines of validation logic
        ...

# agents/discovery.py - Inherits from base
class DiscoveryAgent(BaseAgent):
    def execute(self, input: AgentInput) -> AgentOutput:
        # Now you need to learn your own framework to test a prompt
        ...
```

**Why this is bad:**
- Can't test a prompt change without understanding 200 lines of boilerplate
- Solving problems you don't have yet (metrics? validation?)
- Takes 2 hours to set up before you learn if the prompt even works

---

## Decision Framework: Should I Build This?

Ask these 3 questions:

### 1. **Does it help me test agent prompts faster?**
- ✅ Yes → Build it (e.g., CLI script to run agent on 3 test files)
- ❌ No → Skip it (e.g., monitoring dashboard, config UI)

### 2. **Will I use this in the next 7 days?**
- ✅ Yes → Build it (e.g., markdown export, RANGER test case)
- ❌ No → Defer it (e.g., team auth, database, GCP deployment)

### 3. **Can I delete this easily if the agent doesn't work?**
- ✅ Yes → Good (single-file scripts, isolated functions)
- ❌ No → Bad (frameworks, abstractions, "reusable" systems)

---

## What We're NOT Building (Yet)

### ❌ **Authentication/Authorization**
- It's just you using this (or 2-3 teammates with shared `.env` file)
- Add auth in Phase 2 if validated

### ❌ **Database**
- JSON files in `/data` are fine for 10-20 projects
- Add Supabase in Phase 2 if you need search

### ❌ **API Layer**
- CLI is faster to test than HTTP endpoints
- Add FastAPI in Week 8 only if building UI

### ❌ **Error Handling**
- Let it crash. Read the stack trace. Fix the prompt.
- Add try/catch when patterns emerge (Week 6+)

### ❌ **Logging/Observability**
- `print()` statements are fine
- Add structured logging in Phase 2 if team needs visibility

### ❌ **Tests**
- Manual testing on real projects (RANGER, TrailWatch)
- Add pytest in Phase 2 if refactoring

### ❌ **CI/CD**
- Deploy manually (`git push` + `vercel deploy`)
- Add GitHub Actions in Phase 2 if deploying daily

---

## The "Production Readiness" Trap

AI tools (Cursor, Claude, Antigravity) love to suggest:
- "Let's add proper error handling"
- "Should we set up a database schema?"
- "This needs logging for production"
- "We should write tests for this"

**Your response:** "Not yet. Prove the agent works first."

### When to Upgrade (Phase 2 Triggers)
Only add infrastructure when you hit these **actual problems**:

| Problem | Solution | Phase |
|---------|----------|-------|
| "JSON files are too slow to search" | Add Supabase with vector search | Phase 2 |
| "Can't remember which prompt version worked" | Add git tags + version in output | Phase 2 |
| "Teammates can't run this without my help" | Add README + Docker container | Phase 2 |
| "Agents crash and I don't know why" | Add structured logging | Phase 2 |
| "I'm manually testing the same 3 projects" | Add pytest with fixtures | Phase 2 |

**Until then:** Keep it ugly, keep it fast, keep iterating.

---

## Weekly Reminder

**Before every working session, ask:**

1. **What's the smallest thing I can build to test my hypothesis?**
   - Hypothesis (Week 1): "Agent can ask better questions than I would manually"
   - Smallest test: One Python file that runs 5 Socratic questions on RANGER charter

2. **Am I building infrastructure, or am I testing agent prompts?**
   - If infrastructure → Stop. Test prompts first.
   - If prompts → Keep going.

3. **Could I throw this away tomorrow without regret?**
   - Yes → Good. It's a prototype.
   - No → You've over-invested. Simplify.

---

## The One-Paragraph Reminder (Copy This Into Every Session)

**Paste this at the start of every Cursor/Antigravity session:**

```
This is a proof-of-concept to validate that agent swarms save time on TechTrend 
Design phases. Our goal is to test agent prompts, not build production 
infrastructure. Use single-file Python scripts, hardcoded values, JSON files 
for storage, and print() for debugging. No databases, no auth, no tests, no 
CI/CD until we prove agents work. Ship ugly code weekly, iterate on prompts 
aggressively, and kill anything that doesn't save time by Friday. 
Functional > perfect. Speed > elegance. Learning > scaling.
```

---

## Examples of "Simple" Wins

### Week 1: Discovery Agent
- **Simple approach:** 1 Python file, hardcoded prompt, prints to terminal
- **Time to test prompt:** 5 minutes
- **Iterations per hour:** 10-12 prompt tweaks

### Week 3: Research Agent
- **Simple approach:** Tavily API call → save JSON to `/outputs/ranger/research.json`
- **Time to test:** 2 minutes
- **Iterations per hour:** 20+ searches tested

### Week 8: A2UI
- **Simple approach:** React app that polls `/status.json` every 2 seconds (no WebSockets)
- **Time to test:** Deploy to Vercel, refresh browser
- **Complexity saved:** No WebSocket server, no state management

**Result:** All 8 weeks spent tuning agent behavior, not fighting infrastructure.

---

## Anti-Patterns to Avoid

### 🚫 **"Let's make this configurable"**
- Instead: Hardcode it. Change it manually when needed.

### 🚫 **"We should abstract this pattern"**
- Instead: Copy/paste the code. Refactor after 3rd use.

### 🚫 **"This needs proper architecture"**
- Instead: One folder, one agent per file, done.

### 🚫 **"Let's add [framework] for [future need]"**
- Instead: Solve the problem in front of you with raw code.

### 🚫 **"What if we need to scale this?"**
- Instead: We don't. It's for 1 user (you) testing 3 projects (RANGER, TrailWatch, new).

---

## Final Word

**You're not building a product. You're running an experiment.**

The output of 8 weeks is not "production-ready Hamal." It's:
1. **Knowledge:** Do agent swarms save me time?
2. **Prompts:** What agent skills actually work?
3. **Decision:** Build Phase 2 (scale it) or Kill (archive learnings)?

Everything else—infrastructure, tests, deploy pipelines—is **premature optimization** that slows down learning.

**Keep it simple. Ship ugly. Learn fast.**

---

**Version:** 1.0  
**Use this:** Paste the one-paragraph reminder into every working session  
**Update this:** When you discover new "simple" patterns, add them here

---

## BONUS: One-Sentence Version (For Cursor/Antigravity Prompts)

**Copy/paste this at the start of every session:**

```
This is a POC to test agent prompts, not production software—use single-file 
scripts, hardcoded values, JSON storage, print() debugging, no databases/auth/
tests/CI until we prove agents save time. Functional > perfect. Speed > elegance.
```

***

**Where to put this file:**
- Root of repo: `KEEP_IT_SIMPLE.md` (so it's always visible)
- Link from `README.md`: "⚠️ Read this first: [Keep It Simple](KEEP_IT_SIMPLE.md)"
- Pin in Cursor chat: Add as context file for every session

**Done. Your "no technical debt" manifesto is ready.**
