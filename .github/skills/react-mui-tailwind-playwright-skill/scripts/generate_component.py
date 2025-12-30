#!/usr/bin/env python3
"""
Generates a React component with MUI and Tailwind integration.
Usage: python generate_component.py --name <ComponentName> --mui --tailwind
Output: JSX component file
"""
import sys
import argparse
from pathlib import Path

def generate_component(name: str, use_mui: bool, use_tailwind: bool) -> str:
    imports = ["import React from 'react';"]
    if use_mui:
        imports.append("import { Button } from '@mui/material';")
    if use_tailwind:
        imports.append("// Tailwind classes will be applied via className")

    component = f"""
{chr(10).join(imports)}

function {name}() {{
  return (
    <div className="p-4">
      {f'<Button variant="contained" className="bg-blue-500 hover:bg-blue-700">Hello from {name}</Button>' if use_mui and use_tailwind else '<div>Hello from ' + name + '</div>'}
    </div>
  );
}}

export default {name};
"""

    return component.strip()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate React component")
    parser.add_argument("--name", required=True, help="Component name")
    parser.add_argument("--mui", action="store_true", help="Include MUI")
    parser.add_argument("--tailwind", action="store_true", help="Include Tailwind")

    args = parser.parse_args()

    component_code = generate_component(args.name, args.mui, args.tailwind)
    print(component_code)