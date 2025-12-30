#!/usr/bin/env python3
"""
Validates project architecture against Clean Architecture and CQRS patterns.
Usage: python validate_architecture.py <project_root> [--strict] [--output json|markdown]
Exit codes: 0=valid, 1=violations found, 2=missing dependencies
"""
import sys
import json
import os
from pathlib import Path
from typing import Dict, List, Any, Tuple

def validate_architecture(root_path: Path, strict: bool = False) -> Tuple[bool, Dict[str, Any]]:
    """Validate architecture and return (is_valid, details)."""
    details = {
        "valid": True,
        "violations": [],
        "warnings": [],
        "recommendations": []
    }

    # Check Clean Architecture layers
    src_dir = root_path / "src"
    if src_dir.exists():
        layers = [d.name for d in src_dir.iterdir() if d.is_dir()]
        expected_layers = ["Domain", "Application", "Infrastructure", "Presentation", "API"]

        missing_layers = [layer for layer in expected_layers if layer not in layers]
        if missing_layers:
            details["violations"].append(f"Missing Clean Architecture layers: {missing_layers}")
            details["valid"] = False

        # Check for improper dependencies
        for layer_dir in src_dir.iterdir():
            if not layer_dir.is_dir():
                continue

            layer_name = layer_dir.name
            cs_files = list(layer_dir.rglob("*.cs"))

            for cs_file in cs_files:
                try:
                    content = cs_file.read_text()

                    # Domain should not depend on outer layers
                    if layer_name == "Domain":
                        if any(outer in content for outer in ["Infrastructure", "Application", "Presentation"]):
                            details["violations"].append(f"Domain layer depends on outer layer in {cs_file}")
                            details["valid"] = False

                    # Application should not depend on Infrastructure directly (use interfaces)
                    if layer_name == "Application":
                        if "Infrastructure" in content and "using Infrastructure" in content:
                            details["warnings"].append(f"Application layer directly references Infrastructure in {cs_file}")

                except:
                    pass

    # Check CQRS implementation
    commands_dir = root_path / "src" / "Application" / "Commands"
    queries_dir = root_path / "src" / "Application" / "Queries"

    if commands_dir.exists() and queries_dir.exists():
        # Check for proper separation
        command_files = list(commands_dir.rglob("*.cs"))
        query_files = list(queries_dir.rglob("*.cs"))

        if not command_files:
            details["warnings"].append("CQRS Commands directory exists but no command files found")

        if not query_files:
            details["warnings"].append("CQRS Queries directory exists but no query files found")

        # Check for MediatR usage
        has_mediatR = any("IMediator" in str(f) for f in (command_files + query_files)[:5])
        if not has_mediatR:
            details["recommendations"].append("Consider using MediatR for CQRS dispatching")

    # Check Entity Framework setup
    ef_files = list(root_path.rglob("*Context.cs"))
    if ef_files:
        for ef_file in ef_files[:3]:
            try:
                content = ef_file.read_text()
                if "DbSet" not in content:
                    details["warnings"].append(f"EF Context {ef_file} has no DbSets defined")
            except:
                pass

    # Check React structure
    frontend_dir = root_path / "ClientApp"  # BFF pattern
    if frontend_dir.exists():
        # Check for Redux structure
        store_dir = frontend_dir / "src" / "store"
        if store_dir.exists():
            slices = list(store_dir.glob("*Slice.ts*"))
            if not slices:
                details["warnings"].append("Redux store exists but no slices found")

        # Check TypeScript usage
        ts_files = list(frontend_dir.rglob("*.ts*"))
        js_files = list(frontend_dir.rglob("*.js*"))
        if len(js_files) > len(ts_files):
            details["recommendations"].append("Consider migrating to TypeScript for better type safety")

    return details["valid"], details

def main():
    if len(sys.argv) < 2:
        print("Usage: python validate_architecture.py <project_root> [--strict] [--output json|markdown]", file=sys.stderr)
        sys.exit(1)

    project_root = Path(sys.argv[1])
    if not project_root.exists():
        print(f"Project root {project_root} does not exist", file=sys.stderr)
        sys.exit(1)

    strict = "--strict" in sys.argv
    output_format = "json"

    args = sys.argv[1:]
    if "--output" in args:
        idx = args.index("--output")
        if idx + 1 < len(args):
            output_format = args[idx + 1]

    is_valid, details = validate_architecture(project_root, strict)

    if output_format == "json":
        print(json.dumps(details, indent=2))
    else:
        # Markdown output
        print("# Architecture Validation Report")
        print(f"\n**Overall Status:** {'✅ Valid' if is_valid else '❌ Invalid'}")

        if details["violations"]:
            print("\n## Violations")
            for v in details["violations"]:
                print(f"- {v}")

        if details["warnings"]:
            print("\n## Warnings")
            for w in details["warnings"]:
                print(f"- {w}")

        if details["recommendations"]:
            print("\n## Recommendations")
            for r in details["recommendations"]:
                print(f"- {r}")

    sys.exit(0 if is_valid else 1)

if __name__ == "__main__":
    main()