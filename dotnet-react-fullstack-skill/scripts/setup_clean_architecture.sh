#!/bin/bash
# Setup Clean Architecture folder structure
# Usage: ./setup_clean_architecture.sh <project_name>

set -e

if [ $# -eq 0 ]; then
    echo "Usage: $0 <project_name>" >&2
    exit 1
fi

PROJECT_NAME=$1
BASE_DIR="src"

echo "Setting up Clean Architecture for $PROJECT_NAME..."

# Create main directories
mkdir -p "$BASE_DIR/$PROJECT_NAME.Domain"
mkdir -p "$BASE_DIR/$PROJECT_NAME.Application"
mkdir -p "$BASE_DIR/$PROJECT_NAME.Infrastructure"
mkdir -p "$BASE_DIR/$PROJECT_NAME.Presentation"
mkdir -p "$BASE_DIR/$PROJECT_NAME.API"

# Domain layer
mkdir -p "$BASE_DIR/$PROJECT_NAME.Domain/Entities"
mkdir -p "$BASE_DIR/$PROJECT_NAME.Domain/ValueObjects"
mkdir -p "$BASE_DIR/$PROJECT_NAME.Domain/Interfaces"
mkdir -p "$BASE_DIR/$PROJECT_NAME.Domain/Services"

# Application layer
mkdir -p "$BASE_DIR/$PROJECT_NAME.Application/Commands"
mkdir -p "$BASE_DIR/$PROJECT_NAME.Application/Queries"
mkdir -p "$BASE_DIR/$PROJECT_NAME.Application/Handlers"
mkdir -p "$BASE_DIR/$PROJECT_NAME.Application/DTOs"
mkdir -p "$BASE_DIR/$PROJECT_NAME.Application/Interfaces"

# Infrastructure layer
mkdir -p "$BASE_DIR/$PROJECT_NAME.Infrastructure/Data"
mkdir -p "$BASE_DIR/$PROJECT_NAME.Infrastructure/Repositories"
mkdir -p "$BASE_DIR/$PROJECT_NAME.Infrastructure/Services"
mkdir -p "$BASE_DIR/$PROJECT_NAME.Infrastructure/Migrations"

# Presentation layer
mkdir -p "$BASE_DIR/$PROJECT_NAME.Presentation/Controllers"
mkdir -p "$BASE_DIR/$PROJECT_NAME.Presentation/Middleware"
mkdir -p "$BASE_DIR/$PROJECT_NAME.Presentation/Filters"

# API layer
mkdir -p "$BASE_DIR/$PROJECT_NAME.API/Controllers"
mkdir -p "$BASE_DIR/$PROJECT_NAME.API/Program.cs"
mkdir -p "$BASE_DIR/$PROJECT_NAME.API/appsettings.json"

# Tests
mkdir -p "tests/$PROJECT_NAME.Domain.Tests"
mkdir -p "tests/$PROJECT_NAME.Application.Tests"
mkdir -p "tests/$PROJECT_NAME.Infrastructure.Tests"
mkdir -p "tests/$PROJECT_NAME.API.Tests"

echo "Clean Architecture structure created successfully!"
echo "Next steps:"
echo "1. Create .csproj files for each project"
echo "2. Set up dependency injection"
echo "3. Implement domain entities and interfaces"
echo "4. Run 'dotnet restore' to install packages"