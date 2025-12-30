#!/usr/bin/env python3
"""
Analyzes project structure to identify .NET React fullstack components.
Usage: python analyze_project.py <project_root> [--output json|markdown]
Exit codes: 0=success, 1=invalid path, 2=missing dependencies
"""
import sys
import json
import os
from pathlib import Path
from typing import Dict, List, Any

def analyze_project(root_path: Path) -> Dict[str, Any]:
    """Analyze project structure and return findings."""
    findings = {
        "backend": {
            "dotnet_version": None,
            "clean_architecture": False,
            "cqrs": False,
            "entity_framework": False,
            "fluent_validation": False,
            "refit": False,
            "layers": []
        },
        "frontend": {
            "react_version": None,
            "typescript": False,
            "redux": False,
            "playwright": False
        },
        "database": {
            "postgresql": False
        },
        "issues": []
    }

    # Check backend
    csproj_files = list(root_path.rglob("*.csproj"))
    if csproj_files:
        # Check for .NET version (simplified)
        findings["backend"]["dotnet_version"] = "8.0+"  # Assume for this skill

        # Check for Clean Architecture layers
        src_dir = root_path / "src"
        if src_dir.exists():
            layers = [d.name for d in src_dir.iterdir() if d.is_dir()]
            findings["backend"]["layers"] = layers
            expected_layers = ["Domain", "Application", "Infrastructure", "Presentation", "API"]
            if any(layer in layers for layer in expected_layers):
                findings["backend"]["clean_architecture"] = True

        # Check for CQRS (look for Commands, Queries folders or MediatR usage)
        if any("Command" in str(f) for f in root_path.rglob("*.cs")):
            findings["backend"]["cqrs"] = True

        # Check packages (simplified - look for using statements)
        cs_files = list(root_path.rglob("*.cs"))
        for cs_file in cs_files[:10]:  # Check first 10 files
            try:
                content = cs_file.read_text()
                if "EntityFrameworkCore" in content:
                    findings["backend"]["entity_framework"] = True
                if "FluentValidation" in content:
                    findings["backend"]["fluent_validation"] = True
                if "Refit" in content:
                    findings["backend"]["refit"] = True
            except:
                pass

    # Check frontend
    package_json = root_path / "package.json"
    if package_json.exists():
        try:
            with open(package_json) as f:
                pkg = json.load(f)
                deps = pkg.get("dependencies", {})
                dev_deps = pkg.get("devDependencies", {})

                if "react" in deps:
                    findings["frontend"]["react_version"] = deps["react"]
                if "typescript" in deps or "typescript" in dev_deps:
                    findings["frontend"]["typescript"] = True
                if "redux" in deps or "@reduxjs/toolkit" in deps:
                    findings["frontend"]["redux"] = True
                if "playwright" in dev_deps:
                    findings["frontend"]["playwright"] = True
        except:
            findings["issues"].append("Invalid package.json")

    # Check for PostgreSQL (look for connection strings or Npgsql)
    if any("Npgsql" in str(f) for f in root_path.rglob("*.cs")):
        findings["database"]["postgresql"] = True

    return findings

def main():
    if len(sys.argv) < 2:
        print("Usage: python analyze_project.py <project_root> [--output json|markdown]", file=sys.stderr)
        sys.exit(1)

    project_root = Path(sys.argv[1])
    if not project_root.exists():
        print(f"Project root {project_root} does not exist", file=sys.stderr)
        sys.exit(1)

    output_format = "json"
    if len(sys.argv) > 2 and sys.argv[2] == "--output":
        output_format = sys.argv[3] if len(sys.argv) > 3 else "json"

    findings = analyze_project(project_root)

    if output_format == "json":
        print(json.dumps(findings, indent=2))
    else:
        # Markdown output
        print("# Project Analysis Report")
        print("\n## Backend")
        for key, value in findings["backend"].items():
            print(f"- {key}: {value}")

        print("\n## Frontend")
        for key, value in findings["frontend"].items():
            print(f"- {key}: {value}")

        print("\n## Database")
        for key, value in findings["database"].items():
            print(f"- {key}: {value}")

        if findings["issues"]:
            print("\n## Issues")
            for issue in findings["issues"]:
                print(f"- {issue}")

if __name__ == "__main__":
    main()