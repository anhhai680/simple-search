---
name: dotnet-react-fullstack-development
version: 1.0.0
description: "Expertise in developing full-stack applications using .NET 8+ backend with Clean Architecture, CQRS, Entity Framework, and PostgreSQL, integrated with React 18+ frontend using TypeScript, Redux, and Playwright testing"
author: "AI Assistant"
dependencies:
  skills: []
  mcp_servers: ["filesystem", "github"]
  packages: ["dotnet-sdk>=8.0", "nodejs>=18", "postgresql"]
tags: ["fullstack", "dotnet", "react", "clean-architecture", "cqrs"]
---

## Purpose
This skill transforms a general-purpose AI agent into a full-stack development specialist capable of designing, implementing, and validating applications using modern .NET backend technologies with Clean Architecture and CQRS patterns, paired with a React frontend. It emulates the decision-making of experienced full-stack architects who prioritize maintainable, scalable code structures and efficient development workflows.

## Activation Triggers
When the agent encounters:
- File types: `*.csproj`, `package.json` (with React dependencies), `*.cs` (C# files), `*.tsx` (TypeScript React files)
- Keywords in user requests: "build fullstack app", "implement Clean Architecture", "setup CQRS", "create React component with Redux", "write Playwright tests"
- Directory patterns: presence of `/src` folder with subfolders like `Application`, `Domain`, `Infrastructure` (Clean Architecture), `/ClientApp` (BFF pattern), `/tests` folder

## Core Workflow
### Phase 1: Discovery
1. Run `scripts/analyze_project.py` to inventory project structure and identify stack components
2. Load `REFERENCE.md#architecture-overview` for domain-specific rules and best practices
3. Identify gaps: missing architectural layers, outdated dependencies, incomplete test coverage

### Phase 2: Execution
- If [backend setup requested]: Execute `scripts/setup_clean_architecture.sh` to scaffold Clean Architecture folders
- Else if [CQRS implementation]: Consult `REFERENCE.md#cqrs-pattern` and run `scripts/generate_cqrs_boilerplate.py`
- Else if [frontend component]: Use `scripts/generate_react_component.py` with Redux integration
- Else if [API integration]: Run `scripts/setup_refit_client.py` for Refit library usage
- Else if [testing]: Execute `scripts/setup_playwright_tests.sh`

### Phase 3: Validation
- Run `scripts/validate_architecture.py --strict` to check adherence to patterns
- Generate `REPORT.md` with quality metrics and recommendations
- Execute `scripts/run_tests.sh` for both backend (xUnit) and frontend (Playwright) tests

## Quality Gates
- [ ] Clean Architecture layers properly separated (Domain, Application, Infrastructure, Presentation)
- [ ] CQRS pattern implemented with separate Command/Query handlers
- [ ] Entity Framework migrations created and applied to PostgreSQL
- [ ] Fluent Validation rules defined for all input models
- [ ] React components use TypeScript and Redux for state management
- [ ] Playwright tests cover critical user flows
- [ ] RESTful API follows standard HTTP methods and status codes
- [ ] BFF pattern implemented for optimized frontend API consumption

## Escalation Paths
If [complex business logic requiring domain expertise], suggest:
- "This requires human review because domain rules may vary by business context"
- "Consider enabling MCP server [name] for [capability]" (e.g., database schema validation)

If [performance-critical decisions], suggest:
- "Human architect needed for load testing and optimization strategies"