## 🎯 HAMAL PROJECT: NORTH STAR DOCUMENT

**Last Updated:** January 10, 2026  
**Status:** Framework Testing Phase (Phase 1 Research In Progress)

***

## 🏭 WHAT IS HAMAL?

**Hamal is a structured agentic framework that validates business ideas BEFORE you write code.**

It's a 5-phase methodology with templates, workflows, and decision frameworks that help solopreneurs avoid building things nobody wants. Eventually it will become software, but it starts as a proven methodology.

**Core Philosophy:** Ideas are cheap. Validated ideas are gold. Hamal is the validation engine.

***

## 🎯 THE MISSION

Build and prove the Hamal Framework works by:
1. Creating the framework structure (folders, workflows, docs)
2. Testing it on a real idea (Echo - the Second Brain concept)
3. Evaluating if Hamal produces better decisions than ad-hoc validation
4. Deciding if it should become software or stay a methodology

**Key Mental Model:**
- **Hamal = The Assembly Line** (the product we're building)
- **Echo = The First Car** (the test case to prove the assembly line works)

***

## 🔄 THE 5-PHASE HAMAL FRAMEWORK

### **Phase 1: Research**
- Market analysis and competitor research
- Problem space validation
- Technical feasibility assessment
- **Output:** `01-research/[idea-name]-research.md`
- **Workflow:** `/research-idea`

### **Phase 2: Validation**  
- Problem/solution fit analysis
- Riskiest assumptions identified
- User signal gathering
- **Output:** `02-validation/[idea-name]-validation.md`
- **Workflow:** `/validate-idea`

### **Phase 3: Architecture**
- Tech stack decisions
- System design and feasibility
- Implementation approach
- **Output:** `03-architecture/[idea-name]-architecture.md`
- **Workflow:** `/architecture-plan`

### **Phase 4: Prototyping**
- MVP specification
- Wireframes and user flows
- Implementation plan
- **Output:** `04-prototyping/[idea-name]-spec.md`
- **Workflow:** `/prototype-spec`

### **Phase 5: Decision**
- Go/No-Go recommendation based on evidence
- Risk assessment summary
- Resource requirements
- **Output:** `05-decision/[idea-name]-decision.md`
- **Workflow:** `/go-no-go`

***

## 📁 PROJECT STRUCTURE

```
HAMAL/
├── .agent/
│   ├── rules/                    # Antigravity behavior rules
│   │   ├── frontend_react.md
│   │   ├── ops_security.md
│   │   ├── project_structure.md
│   │   ├── project-standards.md
│   │   ├── python_fastapi.md
│   │   ├── response-format.md    # Low verbosity control
│   │   └── proactive-development.md  # Agent autonomy
│   └── workflows/                # Antigravity workflows
│       ├── research-idea.md      # Phase 1 automation
│       ├── validate-idea.md      # Phase 2 automation
│       ├── architecture-plan.md  # Phase 3 automation
│       ├── prototype-spec.md     # Phase 4 automation
│       └── go-no-go.md          # Phase 5 automation
│
├── hamal-framework/             # THE FRAMEWORK (the product)
│   ├── 01-research/
│   ├── 02-validation/
│   ├── 03-architecture/
│   ├── 04-prototyping/
│   ├── 05-decision/
│   └── HAMAL_FRAMEWORK.md       # Complete methodology docs
│
├── ventures/                     # Ideas being validated
│   └── echo/                    # Test case: Second Brain concept
│       └── [Echo-specific materials]
│
├── backend/                     # Generic API boilerplate
├── frontend/                    # Generic UI boilerplate
├── _FOCUS.md                    # Current mission tracker
└── README.md                    # Public positioning
```

***

## 🧪 CURRENT TEST: PROJECT ECHO

**Echo Concept:** Hands-free "Second Brain" that captures voice/ambient context → processes via AI agent → syncs to Obsidian Vault (no screen required)

**Why Echo?** It's a real idea you care about, making it perfect for testing if Hamal produces useful validation insights.

**Test Success Criteria:**
- Does Hamal find real competitors and market data?
- Does it surface technical challenges we hadn't considered?
- Does it help make better build/don't-build decisions?
- Would other solopreneurs find this process valuable?

***

## 📋 CURRENT STATUS & NEXT STEPS

### ✅ **Completed:**
1. Workspace restructured and flattened
2. Git initialized and pushed to GitHub
3. Backend deployed to Render (live at hamal-api.onrender.com)
4. Antigravity rules configured (low verbosity + proactive mode)
5. Hamal framework structure created
6. Phase workflows built in `.agent/workflows/`
7. **Phase 1 Research on Echo: IN PROGRESS**

### 🎯 **Next Actions:**

**When Phase 1 Research Completes:**
```markdown
Review hamal-framework/01-research/echo-research.md and evaluate:

Quality Check:
- [ ] Found real competitors (Limitless, Rewind, Otter.ai, etc.)?
- [ ] Identified market size and trends?
- [ ] Surfaced technical challenges (privacy, battery, ambient noise)?
- [ ] Cited sources (no hallucinations)?
- [ ] Provided actionable insights?

If PASS → Tell Antigravity: "Phase 1 passed. Proceed to Phase 2: Validation."
If FAIL → Tell Antigravity: "Phase 1 needs improvement. [Specific feedback]. Refine /research-idea workflow."
```

**After All 5 Phases Complete:**
1. Review all Echo validation artifacts
2. Decide if Hamal framework is useful enough to share/build
3. Choose path forward:
   - **Path A:** Package as methodology (docs, templates, courses)
   - **Path B:** Build software product (UI, automation, SaaS)
   - **Path C:** Use internally, iterate, don't productize yet

***

## 🚀 HOW TO RESUME WORK

### **If You Return After a Break:**

1. **Check Current Status:**
   - Read `_FOCUS.md` for current objective
   - Check `hamal-framework/01-research/` to see what's been completed

2. **Prompt Antigravity:**
```markdown
I'm back. Review _FOCUS.md and the hamal-framework/ directory, then:
1. Summarize what's been completed
2. Show me any completed validation artifacts
3. Tell me what phase we're on
4. Recommend the next action

Use the North Star document as context for the overall mission.
```

3. **Continue the Test:**
   - Review any completed phase outputs
   - Approve or request refinements
   - Proceed to next phase when ready

***

## 🎯 KEY PRINCIPLES TO REMEMBER

1. **Hamal is the product, not Echo** - We're building a reusable framework
2. **Echo is the test case** - We're using it to prove Hamal works
3. **Quality over speed** - Each phase output should be genuinely useful
4. **Reusability matters** - Everything should work for future ideas
5. **Evidence-based decisions** - No more "gut feel" idea validation

***

## 🔧 ANTIGRAVITY CONFIGURATION

**Rules Applied:**
- `response-format.md` → Low verbosity, concise answers
- `proactive-development.md` → Agent suggests next steps autonomously
- `project-standards.md` → Code quality and commenting standards

**Key Workflows:**
- `/research-idea` → Phase 1 automation
- `/validate-idea` → Phase 2 automation
- `/architecture-plan` → Phase 3 automation
- `/prototype-spec` → Phase 4 automation
- `/go-no-go` → Phase 5 decision framework

***

## 💡 PROMPTS FOR COMMON SITUATIONS

### **"What phase are we on?"**
```markdown
Review _FOCUS.md and hamal-framework/ folders. Tell me:
- What phase we're currently testing
- What's been completed so far
- What the next action is
```

### **"Continue where we left off"**
```markdown
Review the current state and continue the Hamal validation test. Pick up where we left off and proceed with the next phase.
```

### **"Show me what Hamal has produced so far"**
```markdown
List all files in hamal-framework/ and summarize the key findings from each completed phase. Has Hamal provided valuable insights?
```

### **"I want to validate a different idea"**
```markdown
We're going to test Hamal on a new idea: [DESCRIBE IDEA]

Run it through Phase 1 Research using /research-idea and generate the output in hamal-framework/01-research/[idea-name]-research.md
```

***

## 🎯 SUCCESS METRICS

**Framework is validated when:**
- ✅ All 5 phases tested on Echo
- ✅ Each phase produces actionable, non-obvious insights
- ✅ Decision quality is better than ad-hoc validation
- ✅ Process is repeatable for other ideas
- ✅ Other solopreneurs would find it valuable

**Then decide:** Methodology vs Software Product

***

## 📞 CONTEXT FOR AI ASSISTANTS

If you're an AI reading this to help the user:
- The user is building Hamal (a validation framework)
- Echo is just a test case to prove the framework works
- Focus on framework quality, not Echo features
- Check `_FOCUS.md` for current phase
- Review completed artifacts in `hamal-framework/` folders
- Maintain the "assembly line vs car" mental model

***

**END OF NORTH STAR DOCUMENT**

*Keep this in your repo root or .agent/rules/ folder for quick reference*

***

## 💾 Where to Save This

I recommend creating: `HAMAL_NORTH_STAR.md` in your repo root

Then add a reminder to Antigravity in `.agent/rules/hamal-context.md`:

```markdown
# Hamal Project Context

* Always refer to HAMAL_NORTH_STAR.md for project direction
* Hamal is the product (framework/methodology)
* Echo is the test case proving Hamal works
* Focus on framework quality over specific idea features
* Update _FOCUS.md as phases complete
```

**Copy the entire North Star document above and save it now.** When you return, just tell Antigravity: "Review HAMAL_NORTH_STAR.md and continue where we left off." 🎯
