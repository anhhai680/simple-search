#!/bin/bash
# Checks if all required dependencies are installed

echo "Checking dependencies..."

# Check Node.js
if ! command -v node &> /dev/null; then
    echo "❌ Node.js not installed"
    exit 1
fi

# Check npm
if ! command -v npm &> /dev/null; then
    echo "❌ npm not installed"
    exit 1
fi

# Check if packages are installed (assuming in project dir)
if [ -f "package.json" ]; then
    if ! npm list react &> /dev/null; then
        echo "❌ React not installed"
        exit 1
    fi
    if ! npm list @mui/material &> /dev/null; then
        echo "❌ MUI not installed"
        exit 1
    fi
    if ! npm list tailwindcss &> /dev/null; then
        echo "❌ Tailwind CSS not installed"
        exit 1
    fi
    if ! npm list @playwright/test &> /dev/null; then
        echo "❌ Playwright not installed"
        exit 1
    fi
else
    echo "❌ package.json not found"
    exit 1
fi

echo "✅ All dependencies installed"
exit 0