#!/usr/bin/env python3
"""
Validates React component for MUI/Tailwind best practices.
Usage: python validate_component.py <component_file> --accessibility --responsive
Output: JSON validation results
"""
import sys
import json
import re
from pathlib import Path

def validate_component(file_path: str, check_accessibility: bool, check_responsive: bool) -> dict:
    path = Path(file_path)
    if not path.exists():
        return {"error": "File not found"}

    with open(path) as f:
        content = f.read()

    results = {
        "accessibility": [],
        "responsive": [],
        "mui_usage": [],
        "tailwind_usage": []
    }

    if check_accessibility:
        # Check for alt text in images
        if "<img" in content and 'alt=' not in content:
            results["accessibility"].append("Missing alt text for images")

        # Check for semantic HTML
        if "<div" in content and "button" in content.lower() and "<button" not in content:
            results["accessibility"].append("Use <button> instead of div for clickable elements")

    if check_responsive:
        # Check for responsive Tailwind classes
        responsive_classes = ['sm:', 'md:', 'lg:', 'xl:']
        has_responsive = any(cls in content for cls in responsive_classes)
        if not has_responsive:
            results["responsive"].append("Consider adding responsive classes")

    # Check MUI usage
    if "@mui/material" in content:
        results["mui_usage"].append("MUI import detected")

    # Check Tailwind usage
    if "className=" in content and re.search(r'className="[^"]*\b\w+-\w+', content):
        results["tailwind_usage"].append("Tailwind classes detected")

    return results

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python validate_component.py <file> [--accessibility] [--responsive]")
        sys.exit(1)

    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="Component file path")
    parser.add_argument("--accessibility", action="store_true")
    parser.add_argument("--responsive", action="store_true")

    args = parser.parse_args()

    result = validate_component(args.file, args.accessibility, args.responsive)
    print(json.dumps(result, indent=2))