# Skill Dependencies

## Required MCP Servers
### `@modelcontextprotocol/server-filesystem`
- **Purpose**: Read/write React project files for component generation and testing
- **Setup**: `npx -y @modelcontextprotocol/create-server filesystem --allowed-directory /project`

### `@modelcontextprotocol/server-github`
- **Purpose**: Manage code repositories and pull requests for React projects
- **Config**: Requires GitHub token in environment

## Other Agent Skills
- **`javascript-testing` v1.0+**: For general JS testing utilities
- **`web-development` v2.0+**: For HTML/CSS/JS best practices

## Environment Requirements
- Node.js 18+ (for React 18 features)
- npm 8+ or yarn 1.22+
- Browser for Playwright testing (Chrome, Firefox, Safari)

## Package Dependencies
- `react`: ^18.0.0
- `@mui/material`: ^5.14.0
- `@emotion/react`: ^11.11.0
- `@emotion/styled`: ^11.11.0
- `tailwindcss`: ^3.3.0
- `@playwright/test`: ^1.40.0
- `axe-core`: ^4.8.0 (for accessibility testing)

## Installation Verification
```bash
# Run this to test all dependencies
./scripts/check_dependencies.sh
```
