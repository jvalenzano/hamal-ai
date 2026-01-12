# Hamal Usage Guide

CLI examples and common workflows for the Hamal AI validation framework.

***

## Quick Reference

```bash
# Full pipeline (all agents)
python hamal.py run <charter_file>

# Individual agents
python agents/discovery.py <charter_file>
python agents/research.py outputs/<project>/
python agents/validation.py outputs/<project>/
python agents/architecture.py outputs/<project>/
python agents/summary.py outputs/<project>/

# Check status
python hamal.py status outputs/<project>/

# Regenerate summary only
python agents/summary.py outputs/<project>/
```

***

## Example: Peace Corps Recruitment Chatbot

This example demonstrates a complete validation run using the Peace Corps charter.

### 1. Prepare Charter

Create `data/peace-corps-charter.txt`:

```
Peace Corps Recruitment Chatbot

BACKGROUND:
Peace Corps struggles with volunteer recruitment efficiency. Current process:
- 200+ recruitment officers manually answer repetitive questions
- Average 45 min per inquiry (visa, health, language requirements)
- 60% of inquiries are FAQ-level (already documented)

PROPOSED SOLUTION:
AI chatbot to handle Tier 1 questions, escalate complex cases to humans.

SUCCESS METRICS:
- Reduce officer workload by 40%
- Maintain 90%+ satisfaction scores
- Handle 10,000+ monthly conversations

CONSTRAINTS:
- Must comply with federal privacy rules (PII handling)
- Integrate with existing Salesforce CRM
- Spanish + French language support required
```

### 2. Run Full Pipeline

```bash
python hamal.py run data/peace-corps-charter.txt
```

**Output:**
```
🚀 Hamal Pipeline: peace-corps-charter
📁 Output directory: outputs/peace-corps-charter/

🔍 Discovery Agent: Interrogating problem...
🌐 Discovery Agent: Gathering context on Peace Corps...
📝 Discovery Agent: Generating problem statement...
✅ Discovery Agent complete: outputs/peace-corps-charter/problem.md

🔬 Research Agent: Searching for precedents...
🌐 Research Agent: Found 12 similar projects
📝 Research Agent: Generating research report...
✅ Research Agent complete: outputs/peace-corps-charter/research.md

⚖️ Validation Agent: Scoring feasibility...
📊 Validation Agent: Risk analysis complete
✅ Validation Agent complete: outputs/peace-corps-charter/validation.md
   Score: 25/50 (CONDITIONAL GO)

🏗️ Architecture Agent: Analyzing requirements...
💰 Architecture Agent: Cost estimate: $101,250
📅 Architecture Agent: Timeline: 12 weeks
✅ Architecture Agent complete: outputs/peace-corps-charter/architecture.md

📊 Summary Agent: Generating executive report...
✅ Summary Agent complete: outputs/peace-corps-charter/summary.html

✅ Pipeline complete! (Runtime: 8m 23s)
```

### 3. Review Outputs

```bash
# View validation score
cat outputs/peace-corps-charter/validation.md

# Open interactive summary
open outputs/peace-corps-charter/summary.html
```

***

## Running Individual Agents

### Discovery Agent

**Purpose:** Transform charter into validated problem statement

```bash
python agents/discovery.py data/peace-corps-charter.txt
```

**Output:** `outputs/peace-corps-charter/problem.md`

**Contains:**
- Core problem statement
- Pain severity (High/Medium/Low)
- Stakeholder map
- Agency context from web search

### Research Agent

**Purpose:** Find similar projects, competitors, failures

```bash
python agents/research.py outputs/peace-corps-charter/
```

**Requires:** `problem.md` (from Discovery Agent)

**Output:** `outputs/peace-corps-charter/research.md`

**Contains:**
- Government precedents (similar projects)
- Commercial competitors
- Failure cases and lessons learned

### Validation Agent

**Purpose:** Score feasibility, identify risks

```bash
python agents/validation.py outputs/peace-corps-charter/
```

**Requires:** `problem.md`, `research.md`

**Output:** `outputs/peace-corps-charter/validation.md`

**Contains:**
- Feasibility score (0-50)
- Risk register (5 dimensions)
- Red flags and mitigation strategies
- GO/NO-GO recommendation

### Architecture Agent

**Purpose:** Recommend tech stack, estimate costs

```bash
python agents/architecture.py outputs/peace-corps-charter/
```

**Requires:** `problem.md`, `validation.md`, `data/projects.json`

**Output:** `outputs/peace-corps-charter/architecture.md`

**Contains:**
- Recommended tech stack (based on system defaults)
- Cost breakdown (GCP runtime + dev hours)
- Timeline (6/12/16 weeks)
- Similar project references

### Summary Agent

**Purpose:** Generate executive report with visualizations

```bash
python agents/summary.py outputs/peace-corps-charter/
```

**Requires:** All previous outputs

**Output:** `outputs/peace-corps-charter/summary.html`

**Contains:**
- Interactive HTML report
- Feasibility radar chart
- Cost breakdown chart
- Timeline Gantt chart
- Key metrics and recommendations

***

## Common Workflows

### Regenerate Summary After Edits

If you manually edit `validation.md` or `architecture.md`:

```bash
python agents/summary.py outputs/peace-corps-charter/
```

This regenerates `summary.html` without re-running expensive LLM calls.

### Resume Failed Pipeline

If pipeline fails mid-run:

```bash
# Check what completed
python hamal.py status outputs/peace-corps-charter/

# Resume from last checkpoint
python hamal.py run data/peace-corps-charter.txt
```

Hamal tracks state in `outputs/peace-corps-charter/state.json` and skips completed agents.

### Compare Multiple Charters

```bash
# Run multiple validations
python hamal.py run data/peace-corps-charter.txt
python hamal.py run data/forest-service-charter.txt
python hamal.py run data/va-chatbot-charter.txt

# Compare outputs
ls -lh outputs/*/summary.html
```

### Override Model for Single Run

Edit `agents/utils.py` temporarily:

```python
DEFAULT_MODEL = "claude-opus-4-20250514"  # Higher quality, slower
```

Or modify agent file directly:

```python
response = call_llm(
    model="claude-opus-4-20250514",  # Override
    messages=[...]
)
```

***

## CLI Arguments

### `hamal.py run`

```bash
python hamal.py run <charter_file> [options]

Options:
  --output-dir DIR    Custom output directory (default: outputs/<project-name>/)
  --skip-discovery    Skip Discovery Agent (use existing problem.md)
  --skip-research     Skip Research Agent (use existing research.md)
  --skip-validation   Skip Validation Agent (use existing validation.md)
  --skip-architecture Skip Architecture Agent (use existing architecture.md)
```

**Example:**
```bash
# Skip discovery, start from research
python hamal.py run data/peace-corps-charter.txt --skip-discovery
```

### `hamal.py status`

```bash
python hamal.py status <output_dir>

# Example
python hamal.py status outputs/peace-corps-charter/
```

**Output:**
```json
{
  "project_name": "peace-corps-charter",
  "status": "complete",
  "agents": {
    "discovery": "✅ complete",
    "research": "✅ complete",
    "validation": "✅ complete",
    "architecture": "✅ complete",
    "summary": "✅ complete"
  },
  "runtime": "8m 23s"
}
```

***

## Output Files

Each validation run creates:

```
outputs/peace-corps-charter/
├── state.json              # Pipeline state (for resume)
├── problem.md              # Discovery Agent output
├── research.md             # Research Agent output
├── validation.md           # Validation Agent output
├── architecture.md         # Architecture Agent output
└── summary.html            # Summary Agent output (interactive)
```

***

## Tips & Best Practices

### Charter Quality

**Good charter:**
- Specific problem statement
- Quantified pain points
- Clear success metrics
- Realistic constraints

**Bad charter:**
- Vague ("improve efficiency")
- No metrics
- Solution-first ("we need AI")

### Model Selection

- **Claude Sonnet 4:** Default (fast, accurate)
- **Claude Opus 4:** Complex validations (slower, higher quality)
- **Gemini 1.5 Pro:** Cost optimization (cheaper, slightly lower quality)

### Cost Management

Typical run costs (using Claude Sonnet 4):
- Discovery: ~$0.15
- Research: ~$0.25
- Validation: ~$0.20
- Architecture: ~$0.30
- Summary: ~$0.10
- **Total:** ~$1.00 per validation

Use Gemini for high-volume testing:
```python
DEFAULT_MODEL = "gemini/gemini-1.5-pro"  # ~$0.20 total
```

***

## Troubleshooting

See [TROUBLESHOOTING.md](TROUBLESHOOTING.md) for detailed error solutions.

**Quick fixes:**
- Pipeline hangs → Check API keys in `.env`
- Empty outputs → Verify charter file exists and is readable
- Model errors → Check model name in `agents/utils.py`

***

## Next Steps

1. ✅ Run your first validation
2. 📊 Review `summary.html` in browser
3. 🔄 Iterate on charter based on validation feedback
4. 📈 Track time savings vs. manual Design phase
