#!/bin/bash
# Run all tests for the fullstack application
# Usage: ./run_tests.sh [--backend-only] [--frontend-only]

set -e

BACKEND_ONLY=false
FRONTEND_ONLY=false

while [[ $# -gt 0 ]]; do
  case $1 in
    --backend-only)
      BACKEND_ONLY=true
      shift
      ;;
    --frontend-only)
      FRONTEND_ONLY=true
      shift
      ;;
    *)
      echo "Unknown option: $1"
      echo "Usage: $0 [--backend-only] [--frontend-only]"
      exit 1
      ;;
  esac
done

echo "Running tests..."

# Backend tests
if [ "$FRONTEND_ONLY" = false ]; then
    echo "Running backend tests..."
    if [ -f "*.sln" ] || [ -d "src" ]; then
        # .NET tests
        if command -v dotnet &> /dev/null; then
            dotnet test --verbosity normal
        else
            echo "Warning: dotnet CLI not found, skipping .NET tests"
        fi
    else
        echo "No .NET project found"
    fi
fi

# Frontend tests
if [ "$BACKEND_ONLY" = false ]; then
    echo "Running frontend tests..."
    if [ -f "package.json" ]; then
        if command -v npm &> /dev/null; then
            npm test
        elif command -v yarn &> /dev/null; then
            yarn test
        else
            echo "Warning: npm or yarn not found, skipping frontend tests"
        fi

        # Playwright tests
        if [ -f "playwright.config.ts" ] || [ -f "playwright.config.js" ]; then
            echo "Running Playwright tests..."
            npx playwright test
        fi
    else
        echo "No Node.js project found"
    fi
fi

echo "All tests completed successfully!"