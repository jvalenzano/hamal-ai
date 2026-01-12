#!/usr/bin/env python3
"""
Hamal - AI-Powered Validation Framework

Main orchestrator: Runs agents in sequence, tracks state, generates reports.
"""

import os
import sys
import json
import logging
import click
from datetime import datetime

# Import agents
sys.path.append(os.path.dirname(__file__))
from agents.discovery import run_discovery
from agents.research import run_research
from agents.validation import run_validation
from agents.architecture import run_architecture
from agents.summary import main as run_summary
from agents.summary import main as run_summary
from agents.utils import set_verbose, FatalError

# Optional: Import FastAPI/Uvicorn only inside serve to keep CLI fast? 
# For simplicity/readability, global import is fine for this scale, 
# but let's put it inside the command to avoid hard dependency if users just want CLI 
# and didn't install the server extras (though they are in requirements now).
# Actually, for type safety and global access if we expand, let's keep it clean.
try:
    from fastapi import FastAPI
    import uvicorn
except ImportError:
    pass  # Handled in serve command



@click.group()
@click.option('--verbose', is_flag=True, help='Enable verbose logging')
@click.pass_context
def cli(ctx, verbose):
    """Hamal - Validate government AI opportunities in 15-20 minutes"""
    # Configure logging
    log_level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=log_level,
        format='%(message)s',
        handlers=[logging.StreamHandler(sys.stdout)]
    )
    ctx.ensure_object(dict)
    ctx.obj['verbose'] = verbose


@cli.command()
@click.argument('charter_file', type=click.Path(exists=True))
@click.option('--project-name', default=None, help='Project name (default: from filename)')
@click.option('--verbose', is_flag=True, help='Enable verbose logging')
@click.option('--skip-on-error', is_flag=True, help='Continue pipeline even if an agent fails')
def run(charter_file, project_name, verbose, skip_on_error):
    """Run full validation pipeline on charter"""
    
    # Set verbose mode
    if verbose:
        set_verbose(True)
        click.echo("[VERBOSE MODE ENABLED]\n")
    
    # Extract project name
    if not project_name:
        project_name = os.path.basename(charter_file).replace('.txt', '').replace('_charter', '')
    
    click.echo(f"\n{'='*60}")
    click.echo(f"HAMAL VALIDATION: {project_name}")
    click.echo(f"{'='*60}\n")
    
    # Create output directory
    output_dir = f"outputs/{project_name}"
    os.makedirs(output_dir, exist_ok=True)
    
    # Configure logging to file as well
    log_file = os.path.join(output_dir, "activity.log")
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(logging.Formatter('%(message)s'))
    logging.getLogger().addHandler(file_handler)

    # Initialize state
    state = {
        "project_name": project_name,
        "started_at": datetime.now().isoformat(),
        "charter_file": charter_file,
        "agents": {},
        "errors": [],
        "warnings": []
    }
    
    # Read charter
    with open(charter_file, 'r') as f:
        charter_text = f.read()
    
    try:
        # 1. Discovery Agent
        click.echo("🔍 Running Discovery Agent...")
        state["agents"]["discovery"] = {"status": "running", "started_at": datetime.now().isoformat()}
        save_state(state, output_dir)
        
        try:
            problem_path = run_discovery(charter_text, project_name)
            state["agents"]["discovery"] = {
                "status": "complete",
                "output": problem_path,
                "completed_at": datetime.now().isoformat()
            }
            save_state(state, output_dir)
            click.echo("✅ Discovery complete\n")
        except FatalError as e:
            error_msg = f"Fatal error in Discovery Agent: {e}"
            click.echo(f"\n❌ {error_msg}", err=True)
            state["agents"]["discovery"] = {"status": "failed", "error": str(e), "error_type": "fatal"}
            state["errors"].append({"agent": "discovery", "error": str(e), "type": "fatal", "timestamp": datetime.now().isoformat()})
            save_state(state, output_dir)
            if not skip_on_error:
                raise
            click.echo("⚠️  Skipping remaining agents due to fatal error...")
            return
        except Exception as e:
            error_msg = f"Error in Discovery Agent: {e}"
            click.echo(f"\n❌ {error_msg}", err=True)
            state["agents"]["discovery"] = {"status": "failed", "error": str(e)}
            state["errors"].append({"agent": "discovery", "error": str(e), "timestamp": datetime.now().isoformat()})
            save_state(state, output_dir)
            if not skip_on_error:
                raise
            click.echo("⚠️  Continuing with next agent...\n")
        
        # 2. Research Agent
        click.echo("🌐 Running Research Agent...")
        state["agents"]["research"] = {"status": "running", "started_at": datetime.now().isoformat()}
        save_state(state, output_dir)
        
        try:
            research_path = run_research(problem_path)
            state["agents"]["research"] = {
                "status": "complete",
                "output": research_path,
                "completed_at": datetime.now().isoformat()
            }
            save_state(state, output_dir)
            click.echo("✅ Research complete\n")
        except Exception as e:
            error_msg = f"Error in Research Agent: {e}"
            click.echo(f"\n❌ {error_msg}", err=True)
            state["agents"]["research"] = {"status": "failed", "error": str(e)}
            state["errors"].append({"agent": "research", "error": str(e), "timestamp": datetime.now().isoformat()})
            save_state(state, output_dir)
            if not skip_on_error:
                raise
            click.echo("⚠️  Continuing with limited research data...\n")
        
        # 3. Validation Agent
        click.echo("📊 Running Validation Agent...")
        state["agents"]["validation"] = {"status": "running", "started_at": datetime.now().isoformat()}
        save_state(state, output_dir)
        
        try:
            validation_path = run_validation(output_dir)
            state["agents"]["validation"] = {
                "status": "complete",
                "output": validation_path,
                "completed_at": datetime.now().isoformat()
            }
            save_state(state, output_dir)
            click.echo("✅ Validation complete\n")
        except Exception as e:
            error_msg = f"Error in Validation Agent: {e}"
            click.echo(f"\n❌ {error_msg}", err=True)
            state["agents"]["validation"] = {"status": "failed", "error": str(e)}
            state["errors"].append({"agent": "validation", "error": str(e), "timestamp": datetime.now().isoformat()})
            save_state(state, output_dir)
            if not skip_on_error:
                raise
            click.echo("⚠️  Continuing without validation scores...\n")
        
        # 4. Architecture Agent
        click.echo("🏗️  Running Architecture Agent...")
        state["agents"]["architecture"] = {"status": "running", "started_at": datetime.now().isoformat()}
        save_state(state, output_dir)
        
        try:
            architecture_path = run_architecture(output_dir)
            state["agents"]["architecture"] = {
                "status": "complete",
                "output": architecture_path,
                "completed_at": datetime.now().isoformat()
            }
            save_state(state, output_dir)
            click.echo("✅ Architecture complete\n")
        except Exception as e:
            error_msg = f"Error in Architecture Agent: {e}"
            click.echo(f"\n❌ {error_msg}", err=True)
            state["agents"]["architecture"] = {"status": "failed", "error": str(e)}
            state["errors"].append({"agent": "architecture", "error": str(e), "timestamp": datetime.now().isoformat()})
            save_state(state, output_dir)
            if not skip_on_error:
                raise
            click.echo("⚠️  Continuing without architecture recommendations...\n")
        
        # 5. Summary Agent
        click.echo("📄 Generating Executive Summary...")
        state["agents"]["summary"] = {"status": "running", "started_at": datetime.now().isoformat()}
        save_state(state, output_dir)
        
        try:
            run_summary(output_dir)
            summary_path = os.path.join(output_dir, "summary.html")
            state["agents"]["summary"] = {
                "status": "complete",
                "output": summary_path,
                "completed_at": datetime.now().isoformat()
            }
            save_state(state, output_dir)
            click.echo("✅ Summary complete\n")
        except Exception as e:
            error_msg = f"Error in Summary Agent: {e}"
            click.echo(f"\n❌ {error_msg}", err=True)
            state["agents"]["summary"] = {"status": "failed", "error": str(e)}
            state["errors"].append({"agent": "summary", "error": str(e), "timestamp": datetime.now().isoformat()})
            save_state(state, output_dir)
            if not skip_on_error:
                raise
            click.echo("⚠️  Summary generation failed, but other outputs are available...\n")
        
        # Mark complete
        state["status"] = "complete"
        state["completed_at"] = datetime.now().isoformat()
        save_state(state, output_dir)
        
        # Summary
        click.echo("\n" + "="*60)
        if state.get("errors"):
            click.echo("VALIDATION COMPLETE (WITH ERRORS)")
        else:
            click.echo("VALIDATION COMPLETE")
        click.echo("="*60)
        click.echo(f"\nOutputs saved to: {output_dir}/")
        
        # Show completed outputs
        completed_outputs = []
        for agent_name, agent_state in state.get("agents", {}).items():
            if agent_state.get("status") == "complete":
                output_file = os.path.basename(agent_state.get("output", ""))
                completed_outputs.append(f"  - {output_file}")
        
        if completed_outputs:
            click.echo("\nGenerated files:")
            for output in completed_outputs:
                click.echo(output)
        
        # Show errors if any
        if state.get("errors"):
            click.echo("\n⚠️  Errors encountered:")
            for error in state["errors"]:
                click.echo(f"  - {error['agent']}: {error['error'][:100]}...")
        
        click.echo(f"\nNext steps:")
        if os.path.exists(os.path.join(output_dir, "summary.html")):
            click.echo(f"  1. Open {output_dir}/summary.html in browser")
            click.echo(f"  2. Review executive summary for Go/No-Go recommendation")
        else:
            click.echo(f"  1. Review generated markdown files in {output_dir}/")
        click.echo(f"  3. Check state.json for detailed execution log")
        
    except Exception as e:
        click.echo(f"\n❌ Error: {e}", err=True)
        state["status"] = "failed"
        state["error"] = str(e)
        save_state(state, output_dir)
        sys.exit(1)


@cli.command()
@click.argument('charter_file', type=click.Path(exists=True))
@click.option('--project-name', default=None)
def discover(charter_file, project_name):
    """Run Discovery Agent only"""
    
    if not project_name:
        project_name = os.path.basename(charter_file).replace('.txt', '').replace('_charter', '')
    
    with open(charter_file, 'r') as f:
        charter_text = f.read()
    
    click.echo(f"🔍 Running Discovery Agent on {project_name}...")
    output = run_discovery(charter_text, project_name)
    click.echo(f"✅ Output: {output}")


@cli.command()
@click.argument('problem_file', type=click.Path(exists=True))
def research(problem_file):
    """Run Research Agent on problem.md"""
    
    click.echo(f"🌐 Running Research Agent...")
    output = run_research(problem_file)
    click.echo(f"✅ Output: {output}")


@cli.command()
@click.argument('project_dir', type=click.Path(exists=True))
def validate(project_dir):
    """Run Validation Agent on project directory"""
    
    click.echo(f"📊 Running Validation Agent...")
    output = run_validation(project_dir)
    click.echo(f"✅ Output: {output}")


@cli.command()
@click.argument('project_dir', type=click.Path(exists=True))
def architect(project_dir):
    """Run Architecture Agent on project directory"""
    
    click.echo(f"🏗️  Running Architecture Agent...")
    output = run_architecture(project_dir)
    click.echo(f"✅ Output: {output}")


@cli.command()
@click.argument('project_dir', type=click.Path(exists=True))
def summary(project_dir):
    """Generate executive summary for project"""
    
    click.echo(f"📄 Generating Executive Summary...")
    run_summary(project_dir)
    summary_path = os.path.join(project_dir, "summary.html")
    click.echo(f"✅ Summary generated: {summary_path}")
    click.echo(f"\nOpen in browser: open {summary_path}")


@cli.command()
@click.argument('project_dir', type=click.Path(exists=True))
def status(project_dir):
    """Show validation status"""
    
    state_file = os.path.join(project_dir, "state.json")
    
    if not os.path.exists(state_file):
        click.echo(f"No state found for {project_dir}")
        return
    
    with open(state_file, 'r') as f:
        state = json.load(f)
    
    click.echo(f"\nProject: {state['project_name']}")
    click.echo(f"Status: {state.get('status', 'in progress')}")
    click.echo(f"Started: {state['started_at']}")
    
    if state.get('completed_at'):
        click.echo(f"Completed: {state['completed_at']}")
    
    click.echo("\nAgent Status:")
    for agent_name, agent_state in state.get('agents', {}).items():
        status_emoji = "✅" if agent_state['status'] == 'complete' else "🔄"
        click.echo(f"  {status_emoji} {agent_name}: {agent_state['status']}")


@cli.command()
@click.option('--host', default='0.0.0.0', help='Host to bind to')
@click.option('--port', default=10000, type=int, help='Port to bind to')
def serve(host, port):
    """Run Hamal as a web service (Health Check only for now)"""
    try:
        from fastapi import FastAPI, BackgroundTasks, HTTPException
        from fastapi.responses import FileResponse, JSONResponse
        from fastapi.middleware.cors import CORSMiddleware
        from pydantic import BaseModel
        import uvicorn
    except ImportError:
        click.echo("FastAPI or Uvicorn not installed. Please run: pip install fastapi uvicorn", err=True)
        sys.exit(1)

    app = FastAPI(title="Hamal API", version="0.1.0")

    # Enable CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # For POC, allow all. In prod, strict whitelist.
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    class PipelineRequest(BaseModel):
        charter_text: str
        project_name: str | None = None

    @app.get("/health")
    def health_check():
        return {"status": "ok", "service": "hamal-backend"}
    
    @app.get("/")
    def root():
        return {"message": "Hamal Backend is running. Use CLI for active tasks."}

    @app.post("/api/pipeline/start")
    async def start_pipeline(request: PipelineRequest, background_tasks: BackgroundTasks):
        """Start the validation pipeline in the background"""
        project_name = request.project_name
        
        # If no project name, generate one from timestamp if basic heuristics fail
        if not project_name:
            project_name = f"project_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

        output_dir = f"outputs/{project_name}"
        os.makedirs(output_dir, exist_ok=True)

        # Save charter
        charter_path = os.path.join(output_dir, "charter.txt")
        with open(charter_path, "w") as f:
            f.write(request.charter_text)

        # Initialize state
        state = {
            "project_name": project_name,
            "started_at": datetime.now().isoformat(),
            "charter_file": charter_path,
            "status": "running",
            "agents": {},
            "errors": [],
            "warnings": []
        }
        save_state(state, output_dir)

        # Trigger background CLI execution (reuse existing CLI command logic via function call or subprocess)
        # Using subprocess to separate the worker process from API server for stability
        cmd = [
            sys.executable, 
            os.path.join(os.path.dirname(__file__), "hamal.py"), 
            "run", 
            charter_path, 
            "--project-name", project_name, 
            "--skip-on-error"
        ]
        
        # Log stdout/stderr to activity.log in detached mode
        # Since 'run' now also logs to file internally, we might double log if we redirect stdout here, 
        # BUT 'run' only logs to file *after* it sets up logging. Early startup logs (or crash logs) might be missed.
        # Let's redirect stdout/stderr to the log file to capture EVERYTHING.
        log_file = os.path.join(output_dir, "activity.log")
        with open(log_file, "a") as f:
            import subprocess
            subprocess.Popen(cmd, stdout=f, stderr=subprocess.STDOUT)

        return {"status": "started", "project_name": project_name}

    @app.get("/api/pipeline/{project_name}/status")
    def get_status(project_name: str):
        """Get current pipeline status"""
        state_file = f"outputs/{project_name}/state.json"
        if not os.path.exists(state_file):
            raise HTTPException(status_code=404, detail="Project not found")
        
        with open(state_file, "r") as f:
            try:
                state = json.load(f)
            except json.JSONDecodeError:
                # Handle race condition where file is being written
                return {"status": "unknown", "error": "reading_state"}
        
        return state

    @app.get("/api/pipeline/{project_name}/artifacts/{filename}")
    def get_artifact(project_name: str, filename: str):
        """Get generated artifact content"""
        # Security check: prevent directory traversal
        if ".." in filename or "/" in filename:
             raise HTTPException(status_code=400, detail="Invalid filename")

        file_path = f"outputs/{project_name}/{filename}"
        if not os.path.exists(file_path):
             raise HTTPException(status_code=404, detail="File not found")

        return FileResponse(file_path)

    click.echo(f"🚀 Starting Hamal Web Service on {host}:{port}")
    uvicorn.run(app, host=host, port=port)



def save_state(state: dict, output_dir: str):
    """Save state to state.json"""
    state_file = os.path.join(output_dir, "state.json")
    with open(state_file, 'w') as f:
        json.dump(state, f, indent=2)


if __name__ == '__main__':
    cli()
