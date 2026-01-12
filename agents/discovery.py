#!/usr/bin/env python3
"""
Discovery Agent - Problem Interrogation via 5 Whys + Context Gathering

Purpose: Transform vague agency charter into validated problem statement
Method: Socratic questioning + autonomous web research
Output: problem.md (validated problem statement)
"""

import os
import sys
import logging

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents.utils import call_llm, get_response_content, DEFAULT_MODEL, safe_tavily_search, FatalError, log_verbose
from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)

# Initialize clients
# claude = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))


def interrogate_problem(charter_text: str) -> dict:
    """
    Use 5 Whys methodology to extract core problem.
    
    Returns dict with:
    - core_problem: str
    - pain_severity: str (High/Medium/Low)
    - frequency: str
    - current_workaround: str
    - stakeholders: list
    """
    
    system_prompt = """You are a critical problem discovery agent for government AI projects.
Your job: Use Socratic questioning to get from surface request → root cause → validated problem statement.

Framework (5 Whys):
1. What specific task is painful?
2. Why is that task painful?
3. What's the consequence of that pain?
4. How often does this happen?
5. What's the current workaround?

Be direct. Ask one question at a time. Don't explain your reasoning - just ask the question.

After 5 questions, synthesize into:
- Core Problem: [one sentence, specific]
- Pain Severity: High/Medium/Low [with reasoning]
- Frequency: [X times per year/month]
- Current Workaround: [what they do today]
- Stakeholders: [who feels pain, who pays, who blocks]
- Willingness to Pay: [evidence from charter]
"""
    
    try:
        log_verbose("Interrogating problem with LLM...")
        response = call_llm(
            model="claude-sonnet-4-20250514",
            max_tokens=2048,
            system=system_prompt,
            messages=[{
                "role": "user",
                "content": f"""Agency charter:

{charter_text}

Run through the 5 Whys framework and extract:
1. Core Problem (one specific sentence)
2. Pain Severity (High/Medium/Low with reasoning)
3. Frequency (how often this happens)
4. Current Workaround (what they do today)
5. Stakeholders (who feels pain, who pays, who blocks)
6. Willingness to Pay (evidence from charter)

Format as structured output, not conversational questions."""
            }]
        )
        
        result_text = get_response_content(response)
        log_verbose("Problem interrogation successful")
        
        return {
            "raw_analysis": result_text,
            "charter": charter_text
        }
    except FatalError as e:
        print(f"\n❌ Fatal error during problem interrogation: {e}")
        raise
    except Exception as e:
        print(f"\n❌ Error during problem interrogation: {e}")
        raise


def gather_context(agency_name: str, problem_domain: str) -> dict:
    """
    Search web for agency background:
    - Mission statement
    - Recent news
    - Budget info
    - Leadership
    
    Returns dict with context findings.
    """
    
    # Search queries
    queries = [
        f"{agency_name} mission statement",
        f"{agency_name} {problem_domain} recent news",
        f"{agency_name} budget 2026"
    ]
    
    context = {"findings": []}
    
    for query in queries:
        log_verbose(f"Searching for: {query}")
        results = safe_tavily_search(tavily, query, max_results=3, fallback_empty=True)
        
        if "error" in results:
            context["findings"].append({
                "query": query,
                "error": results["error"]
            })
        else:
            context["findings"].append({
                "query": query,
                "results": results.get("results", [])
            })
    
    return context


def generate_problem_statement(interrogation: dict, context: dict) -> str:
    """
    Synthesize interrogation + context into final problem.md
    
    Uses Claude to combine findings into clean markdown.
    """
    
    system_prompt = """You are synthesizing problem discovery findings into a validated problem statement.

Output format (markdown):

# Validated Problem Statement

## Core Problem
[One sentence, specific, quantified if possible]

## Pain Severity
**Level:** High / Medium / Low
**Reasoning:** [Why this severity?]

## Frequency
[How often does this problem occur?]

## Current Workaround
[What are they doing today to cope?]

## Stakeholders
- **Pain Sufferers:** [who experiences the problem daily]
- **Budget Owner:** [who would pay to solve this]
- **Potential Blockers:** [who might resist change]

## Willingness to Pay
**Evidence:** [from charter/context - is budget approved? pilot funding? or speculative?]

## Agency Context
[Brief background on agency mission, recent initiatives related to this problem]

***

**Confidence Level:** [High/Medium/Low - based on charter clarity]
**Recommended Next Step:** [Research similar projects / Schedule stakeholder interviews / Request more detail on X]
"""
    
    try:
        log_verbose("Generating problem statement with LLM...")
        response = call_llm(
            model="claude-sonnet-4-20250514",
            max_tokens=3000,
            system=system_prompt,
            messages=[{
                "role": "user",
                "content": f"""Synthesize these findings into a validated problem statement:

## Interrogation Results:
{interrogation['raw_analysis']}

## Agency Context from Web Search:
{context}

Generate the markdown problem statement following the template."""
            }]
        )
        
        result = get_response_content(response)
        log_verbose("Problem statement generation successful")
        return result
    except FatalError as e:
        print(f"\n❌ Fatal error generating problem statement: {e}")
        raise
    except Exception as e:
        print(f"\n❌ Error generating problem statement: {e}")
        raise


def run_discovery(charter_text: str, project_name: str) -> str:
    """
    Full discovery pipeline.
    
    Returns: path to generated problem.md
    """
    
    logger.info("🔍 Discovery Agent: Interrogating problem...")
    interrogation = interrogate_problem(charter_text)
    
    # Extract agency name (simple heuristic for POC)
    agency_name = "USDA Forest Service" if "forest" in charter_text.lower() else "Federal Agency"
    problem_domain = "post-fire recovery" if "fire" in charter_text.lower() else "operations"
    
    logger.info(f"🌐 Discovery Agent: Gathering context on {agency_name}...")
    context = gather_context(agency_name, problem_domain)
    
    logger.info("📝 Discovery Agent: Generating problem statement...")
    problem_md = generate_problem_statement(interrogation, context)
    
    # Save output
    output_dir = f"outputs/{project_name}"
    os.makedirs(output_dir, exist_ok=True)
    
    output_path = f"{output_dir}/problem.md"
    with open(output_path, "w") as f:
        f.write(problem_md)
    
    logger.info(f"✅ Discovery Agent complete: {output_path}")
    
    return output_path


# CLI Interface (for standalone testing)
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python agents/discovery.py <charter_file.txt>")
        print("\nExample:")
        print("  python agents/discovery.py data/ranger_charter.txt")
        sys.exit(1)
    
    charter_file = sys.argv[1]
    
    # Read charter
    with open(charter_file, "r") as f:
        charter = f.read()
    
    # Extract project name from filename
    project_name = os.path.basename(charter_file).replace(".txt", "").replace("_charter", "")
    
    # Run discovery
    output = run_discovery(charter, project_name)
    
    print("\n" + "="*60)
    print("DISCOVERY COMPLETE")
    print("="*60)
    print(f"Output: {output}")
    print("\nNext steps:")
    print("1. Review problem.md")
    print("2. Run Research Agent: python agents/research.py")
