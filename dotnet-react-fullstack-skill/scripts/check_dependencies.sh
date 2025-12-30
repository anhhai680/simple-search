#!/bin/bash
# Check dependencies for .NET React fullstack development
# Usage: ./check_dependencies.sh

set -e

echo "Checking dependencies..."

ERRORS=0
WARNINGS=0

# Check .NET SDK
echo -n "Checking .NET SDK... "
if command -v dotnet &> /dev/null; then
    VERSION=$(dotnet --version)
    echo "✓ $VERSION"
    if [[ "$VERSION" =~ ^[6-7]\. ]]; then
        echo "⚠️  Warning: .NET version $VERSION detected. .NET 8+ recommended."
        WARNINGS=$((WARNINGS + 1))
    fi
else
    echo "✗ Not installed"
    ERRORS=$((ERRORS + 1))
fi

# Check Node.js
echo -n "Checking Node.js... "
if command -v node &> /dev/null; then
    VERSION=$(node --version)
    echo "✓ $VERSION"
    if [[ "$VERSION" =~ ^v1[0-7]\. ]]; then
        echo "⚠️  Warning: Node.js version $VERSION detected. Node.js 18+ recommended."
        WARNINGS=$((WARNINGS + 1))
    fi
else
    echo "✗ Not installed"
    ERRORS=$((ERRORS + 1))
fi

# Check npm
echo -n "Checking npm... "
if command -v npm &> /dev/null; then
    VERSION=$(npm --version)
    echo "✓ $VERSION"
else
    echo "✗ Not installed"
    ERRORS=$((ERRORS + 1))
fi

# Check PostgreSQL
echo -n "Checking PostgreSQL... "
if command -v psql &> /dev/null; then
    echo "✓ Installed"
else
    echo "⚠️  Not found in PATH (may be installed via Docker)"
    WARNINGS=$((WARNINGS + 1))
fi

# Check Git
echo -n "Checking Git... "
if command -v git &> /dev/null; then
    VERSION=$(git --version | cut -d' ' -f3)
    echo "✓ $VERSION"
else
    echo "✗ Not installed"
    ERRORS=$((ERRORS + 1))
fi

# Check if in correct project structure
echo -n "Checking project structure... "
if [ -f "package.json" ] && ([ -f "*.sln" ] || [ -d "src" ]); then
    echo "✓ Fullstack project detected"
elif [ -f "package.json" ]; then
    echo "✓ Frontend-only project detected"
elif [ -f "*.sln" ] || [ -d "src" ]; then
    echo "✓ Backend-only project detected"
else
    echo "⚠️  No project files detected"
    WARNINGS=$((WARNINGS + 1))
fi

echo ""
echo "Summary:"
echo "Errors: $ERRORS"
echo "Warnings: $WARNINGS"

if [ $ERRORS -gt 0 ]; then
    echo ""
    echo "❌ Some required dependencies are missing."
    echo "Please install them and run this script again."
    exit 1
elif [ $WARNINGS -gt 0 ]; then
    echo ""
    echo "⚠️  Some dependencies have version warnings."
    echo "Consider upgrading for best experience."
    exit 0
else
    echo ""
    echo "✅ All dependencies are properly installed!"
    exit 0
fi