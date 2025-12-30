# .NET React Fullstack Development Skill

This skill enables AI agents to develop production-ready full-stack applications using .NET 8+ backend with Clean Architecture and React 18+ frontend.

## Overview

The skill covers the complete stack:
- **Backend**: .NET 8+, Entity Framework Core, PostgreSQL, Clean Architecture, CQRS, MediatR, Fluent Validation, Refit
- **Frontend**: React 18+, TypeScript, Redux Toolkit, Playwright testing
- **Architecture**: RESTful APIs, Backend for Frontend pattern

## Quick Start

1. **Check Dependencies**: `./scripts/check_dependencies.sh`
2. **Analyze Project**: `python scripts/analyze_project.py /path/to/project`
3. **Setup Architecture**: `./scripts/setup_clean_architecture.sh MyProject`
4. **Generate Code**: `python scripts/generate_cqrs_boilerplate.py User Create`
5. **Validate**: `python scripts/validate_architecture.py /path/to/project`
6. **Run Tests**: `./scripts/run_tests.sh`

## File Structure

- `SKILL.md` - Contract and activation triggers
- `REFERENCE.md` - Deep technical knowledge and decision trees
- `DEPENDENCIES.md` - Required tools and packages
- `EVAL.md` - Test cases and success metrics
- `scripts/` - Automation tools
- `examples/` - Sample implementations
- `tests/fixtures/` - Test data

## Key Features

### Architecture Enforcement
- Validates Clean Architecture layer separation
- Ensures CQRS pattern implementation
- Checks for proper dependency injection

### Code Generation
- CQRS command/query boilerplate
- React components with Redux integration
- Refit API client interfaces
- Playwright test setup

### Quality Assurance
- Automated validation scripts
- Test execution across stack
- Dependency verification

## Examples

See `examples/happy_path/` for a complete task management application and `examples/edge_cases/` for common mistakes to avoid.

## Contributing

This skill follows the Agent Skill specification. Updates should maintain backward compatibility and include comprehensive test cases.