import os

ROOT = "echo-product-workspace"

# Define the structure (Folders and Files)
structure = {
    ".agentic": ["agents.yaml"],
    ".agentic/prompts": [],
    "directives": ["product_spec.md"],
    "directives/architecture_decisions": [],
    "research": [],
    "research/market_validation": [],
    "research/hardware_specs": [],
    "prototypes": [],
    "prototypes/voice_capture_poc": [],
    "prototypes/obsidian_plugin": [],
    "inspiration": ["brand_narrative.md"],
    "logs": ["week_01_log.md", "decisions.md"],
    "": [ # Root files
        "master_critique_prompt_ready_to_use.md",
        "project_naming_and_structure.md",
        "echo_project_launch_guide.md",
        "README.md"
    ]
}

def scaffold():
    if not os.path.exists(ROOT):
        os.makedirs(ROOT)
        print(f"📂 Created root: {ROOT}")

    for folder, files in structure.items():
        # Create Folder
        dir_path = os.path.join(ROOT, folder)
        os.makedirs(dir_path, exist_ok=True)
        
        # Create Empty Files
        for file in files:
            file_path = os.path.join(dir_path, file)
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(f"# {file} (Paste content here)\n")
            print(f"  📄 Created file: {file}")

    print("\n✅ Scaffolding complete. You can now paste the content into the files.")

if __name__ == "__main__":
    scaffold()