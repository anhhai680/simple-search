# Skill Dependencies

## Required MCP Servers
### @modelcontextprotocol/server-filesystem
- Purpose: Read/write project files for state management and code generation
- Setup: npx -y @modelcontextprotocol/create-server filesystem --allowed-directory /project

### @modelcontextprotocol/server-github
- Purpose: Version control and repository management
- Setup: Standard GitHub MCP server configuration

## Other Agent Skills
- git-workflow v2.3+: For commit message generation and branching
- code-review v1.0+: For static analysis and code quality checks

## Environment Requirements
- .NET 8.0+ SDK (for C# development and CLI tools)
- Node.js 18+ (for React and npm/yarn)
- PostgreSQL 13+ (for database operations)
- Git (for version control)
- Docker (optional, for containerized development)

## Package Dependencies
- Microsoft.EntityFrameworkCore 8.0+
- Npgsql.EntityFrameworkCore.PostgreSQL 8.0+
- MediatR 12.0+
- FluentValidation 11.0+
- Refit 7.0+
- React 18+
- TypeScript 5.0+
- Redux Toolkit 2.0+
- Playwright 1.40+

## Installation Verification
```bash
# Run this to test all dependencies
./scripts/check_dependencies.sh
```

This script checks:
- .NET SDK version
- Node.js version
- PostgreSQL connection
- Required NuGet packages
- npm packages
- MCP server availability