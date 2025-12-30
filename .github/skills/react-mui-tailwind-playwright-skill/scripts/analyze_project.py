#!/usr/bin/env python3
"""
Analyzes React project structure for MUI, Tailwind, and Playwright setup.
Usage: python analyze_project.py <project_path>
Output: JSON with project status
"""
import sys
import json
import os
from pathlib import Path

def analyze_project(project_path: str) -> dict:
    path = Path(project_path)
    status = {
        "react": False,
        "mui": False,
        "tailwind": False,
        "playwright": False,
        "structure": {}
    }

    # Check package.json
    package_json = path / "package.json"
    if package_json.exists():
        with open(package_json) as f:
            pkg = json.load(f)
            deps = pkg.get("dependencies", {})
            dev_deps = pkg.get("devDependencies", {})

            status["react"] = "react" in deps
            status["mui"] = "@mui/material" in deps
            status["tailwind"] = "tailwindcss" in deps or "tailwindcss" in dev_deps
            status["playwright"] = "@playwright/test" in dev_deps

    # Check config files
    status["structure"] = {
        "tailwind_config": (path / "tailwind.config.js").exists(),
        "playwright_config": (path / "playwright.config.js").exists(),
        "src_dir": (path / "src").exists(),
        "components_dir": (path / "src" / "components").exists(),
        "tests_dir": (path / "tests").exists()
    }

    return status

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python analyze_project.py <project_path>")
        sys.exit(1)

    result = analyze_project(sys.argv[1])
    print(json.dumps(result, indent=2))