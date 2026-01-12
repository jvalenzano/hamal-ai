#!/usr/bin/env python3
"""
Research Agent - Find Government Precedents, Competitors, Failures

Purpose: Search for similar projects to learn from
Method: Web search + LLM analysis of findings
Output: research.md (precedents, competitors, lessons learned)
"""

import os
import json
import sys
import logging

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents.utils import call_llm, get_response_content, DEFAULT_MODEL, safe_tavily_search, FatalError, log_verbose, clean_json_output
from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)

# claude = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))


def extract_search_keywords(problem_md: str) -> dict:
    """
    Parse problem.md to extract search keywords.
    
    Uses Claude to identify:
    - Agency name
    - Problem domain
    - Key technologies
    - Pain points (for finding similar problems)
    """
    
    try:
        log_verbose("Extracting search keywords with LLM...")
        response = call_llm(
            model="claude-sonnet-4-20250514",
            max_tokens=1024,
            messages=[{
                "role": "user",
                "content": f"""Extract search keywords from this problem statement:

{problem_md}

Return JSON with:
- agency_name: str (e.g., "USDA Forest Service")
- problem_domain: str (e.g., "wildfire post-fire recovery")
- key_technologies: list (e.g., ["AI", "data consolidation", "multi-format ingestion"])
- pain_points: list (e.g., ["manual data entry", "multi-agency coordination", "delayed decisions"])

Output ONLY valid JSON, no explanation."""
            }]
        )
        
        # Parse JSON from Claude's response
        response_text = get_response_content(response)
        keywords = json.loads(clean_json_output(response_text))
        log_verbose(f"Extracted keywords: {keywords}")
        return keywords
        
    except json.JSONDecodeError as e:
        print(f"⚠️  JSON parsing failed, using fallback keywords: {e}")
        log_verbose(f"Failed to parse: {response_text}")
        return {
            "agency_name": "Federal Agency",
            "problem_domain": "operations",
            "key_technologies": ["AI"],
            "pain_points": ["efficiency"]
        }
    except Exception as e:
        print(f"⚠️  Error extracting keywords, using fallback: {e}")
        return {
            "agency_name": "Federal Agency",
            "problem_domain": "operations",
            "key_technologies": ["AI"],
            "pain_points": ["efficiency"]
        }


def search_government_precedents(keywords: dict) -> list:
    """
    Search for similar government projects.
    
    Sources:
    - DigitalGov.gov (case studies)
    - Challenge.gov (prize competitions, past projects)
    - SAM.gov (contract awards)
    - GitHub (18F, USDS open source projects)
    """
    
    queries = [
        f"{keywords['problem_domain']} site:digital.gov",
        f"{keywords['problem_domain']} government AI case study",
        f"{keywords['problem_domain']} federal agency success story",
        f"{' '.join(keywords['key_technologies'])} {keywords['agency_name']}"
    ]
    
    findings = []
    
    for query in queries:
        print(f"  🔍 Searching: {query}")
        results = safe_tavily_search(tavily, query, max_results=5, fallback_empty=True)
        
        for result in results.get("results", []):
            findings.append({
                "type": "government",
                "title": result.get("title", ""),
                "url": result.get("url", ""),
                "snippet": result.get("content", "")
            })
    
    return findings[:10]  # Limit to top 10


def search_competitors(keywords: dict) -> list:
    """
    Search for commercial solutions in this space.
    
    Focus on:
    - Palantir, Esri, Deloitte (known gov contractors)
    - Startups in this domain
    - SaaS platforms
    """
    
    # Known competitors in gov AI space
    competitors = ["Palantir", "Esri", "Deloitte", "Accenture Federal", "Booz Allen"]
    
    queries = [
        f"{comp} {keywords['problem_domain']}" for comp in competitors[:3]
    ]
    
    # Add generic search
    queries.append(f"{keywords['problem_domain']} commercial software solution")
    
    findings = []
    
    for query in queries:
        print(f"  🔍 Searching: {query}")
        results = safe_tavily_search(tavily, query, max_results=3, fallback_empty=True)
        
        for result in results.get("results", []):
            findings.append({
                "type": "commercial",
                "title": result.get("title", ""),
                "url": result.get("url", ""),
                "snippet": result.get("content", "")
            })
    
    return findings[:8]  # Limit to top 8


def search_failures(keywords: dict) -> list:
    """
    Find similar projects that failed - extract lessons.
    
    Search for:
    - "failed modernization"
    - "lessons learned"
    - "post-mortem"
    """
    
    queries = [
        f"{keywords['problem_domain']} failed project lessons learned",
        f"{keywords['agency_name']} modernization failure",
        f"government AI project failure {keywords['problem_domain']}"
    ]
    
    findings = []
    
    for query in queries:
        print(f"  🔍 Searching: {query}")
        results = safe_tavily_search(tavily, query, max_results=3, fallback_empty=True)
        
        for result in results.get("results", []):
            findings.append({
                "type": "failure",
                "title": result.get("title", ""),
                "url": result.get("url", ""),
                "snippet": result.get("content", "")
            })
    
    return findings[:5]  # Limit to top 5


def analyze_findings(problem_md: str, precedents: list, competitors: list, failures: list) -> str:
    """
    Use Claude to synthesize findings into research.md
    
    Format:
    - Government Precedents (what worked, tech stack, outcomes)
    - Commercial Competitors (pricing, features, weaknesses)
    - Failure Patterns (why similar projects failed, lessons)
    - Recommendations (based on research)
    """
    
    system_prompt = """You are a government AI project researcher.

Synthesize search findings into a research report with these sections:

1. **Government Precedents** - List 3-5 most relevant projects with:
   - Project name, agency, year
   - Tech stack (if mentioned)
   - Outcome (deployed? pilot? failed?)
   - Key lesson (what did they learn?)

2. **Commercial Competitors** - List 2-4 vendors with:
   - Company name, product
   - Estimated pricing (if known, or "enterprise pricing")
   - Strengths (what they do well)
   - Weaknesses (gaps, cost, lock-in)

3. **Failure Patterns** - Common reasons similar projects failed:
   - Technical issues (wrong tech choice, scale problems)
   - Process issues (timeline too aggressive, wrong procurement vehicle)
   - Stakeholder issues (lack of buy-in, multi-agency coordination)

4. **Key Takeaways** - 3-5 insights from research:
   - What approaches worked best?
   - What should we avoid?
   - What's the realistic timeline/cost based on precedents?

Format in clean markdown. Be specific, cite URLs where relevant."""
    
    try:
        log_verbose("Analyzing findings with LLM...")
        
        # Combine findings into context
        findings_text = f"""
## Government Precedents Found:
{json.dumps(precedents, indent=2)}

## Commercial Competitors Found:
{json.dumps(competitors, indent=2)}

## Failure Cases Found:
{json.dumps(failures, indent=2)}
"""
        
        response = call_llm(
            model="claude-sonnet-4-20250514",
            max_tokens=4000,
            system=system_prompt,
            messages=[{
                "role": "user",
                "content": f"""Original problem:

{problem_md}

***

Research findings:

{findings_text}

Synthesize into research.md following the 4-section format."""
            }]
        )
        
        result = get_response_content(response)
        log_verbose("Analysis successful")
        return result
        
    except FatalError as e:
        print(f"\n❌ Fatal error analyzing findings: {e}")
        raise
    except Exception as e:
        print(f"\n❌ Error analyzing findings: {e}")
        raise


def run_research(problem_md_path: str) -> str:
    """
    Full research pipeline.
    
    Returns: path to generated research.md
    """
    
    # Read problem.md
    with open(problem_md_path, "r") as f:
        problem_md = f.read()
    
    project_name = os.path.basename(os.path.dirname(problem_md_path))
    
    logger.info("🔍 Research Agent: Extracting search keywords...")
    keywords = extract_search_keywords(problem_md)
    logger.debug(f"   Keywords: {keywords}")
    
    logger.info("\n🌐 Research Agent: Searching government precedents...")
    precedents = search_government_precedents(keywords)
    logger.info(f"   Found {len(precedents)} precedents")
    
    logger.info("\n🏢 Research Agent: Searching commercial competitors...")
    competitors = search_competitors(keywords)
    logger.info(f"   Found {len(competitors)} competitors")
    
    logger.info("\n⚠️  Research Agent: Searching failure cases...")
    failures = search_failures(keywords)
    logger.info(f"   Found {len(failures)} failure cases")
    
    logger.info("\n📝 Research Agent: Synthesizing findings...")
    research_md = analyze_findings(problem_md, precedents, competitors, failures)
    
    # Save output
    output_path = f"outputs/{project_name}/research.md"
    with open(output_path, "w") as f:
        f.write(research_md)
    
    logger.info(f"\n✅ Research Agent complete: {output_path}")
    
    return output_path


# CLI Interface
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python agents/research.py outputs/<project>/problem.md")
        print("\nExample:")
        print("  python agents/research.py outputs/ranger/problem.md")
        sys.exit(1)
    
    problem_path = sys.argv[1]
    
    if not os.path.exists(problem_path):
        print(f"Error: File not found: {problem_path}")
        sys.exit(1)
    
    output = run_research(problem_path)
    
    print("\n" + "="*60)
    print("RESEARCH COMPLETE")
    print("="*60)
    print(f"Output: {output}")
    print("\nNext steps:")
    print("1. Review research.md")
    print("2. Run Validation Agent: python agents/validation.py")
