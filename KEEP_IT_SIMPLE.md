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

## The One-Paragraph Reminder

**Paste this at the start of every working session:**

```
This is a proof-of-concept to validate that agent swarms save time on Project 
Design phases. Our goal is to test agent prompts, not build production 
infrastructure. Use single-file Python scripts, hardcoded values, JSON files 
for storage, and print() for debugging. No databases, no auth, no tests, no 
CI/CD until we prove agents work. Ship ugly code weekly, iterate on prompts 
aggressively, and kill anything that doesn't save time by Friday. 
Functional > perfect. Speed > elegance. Learning > scaling.
```

***

**Version:** 1.0  
**Use this:** Paste the one-paragraph reminder into every working session  
**Update this:** When you discover new "simple" patterns, add them here
