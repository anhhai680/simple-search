---
name: react-mui-tailwind-playwright
version: 1.0.0
description: "Provides expertise in developing and testing React applications using Material-UI components and Tailwind CSS styling."
author: "AI Assistant"
dependencies:
  skills: ["javascript-testing"]
  mcp_servers: ["filesystem", "github"]
  packages: ["react>=18.0", "@mui/material>=5.0", "tailwindcss>=3.0", "@playwright/test>=1.0"]
tags: ["react", "ui", "mui", "tailwind", "playwright", "testing"]
---

## Purpose
This skill transforms a general-purpose AI agent into a React development specialist focused on building modern, accessible user interfaces using Material-UI (MUI) for component consistency and Tailwind CSS for utility-first styling. It includes automated testing with Playwright to ensure reliability and cross-browser compatibility. The "expert" emulated is a senior front-end developer with deep knowledge of React ecosystem best practices, design system integration, and end-to-end testing strategies.

## Activation Triggers
When the agent encounters:
- Project files: `package.json` with React dependencies, `tailwind.config.js`, or Playwright config
- Keywords in user requests: "create React component with MUI", "style with Tailwind", "test with Playwright"
- Directory patterns: presence of `/src/components`, `/tests`, or MUI theme files

## Core Workflow
### Phase 1: Discovery
1. Run `scripts/analyze_project.py` to inventory project structure and dependencies
2. Load `REFERENCE.md#setup-checklist` for environment verification
3. Identify gaps: missing MUI theme, Tailwind config, or test setup

### Phase 2: Execution
- If creating a new component: Execute `scripts/generate_component.py --mui --tailwind`
- Else if styling existing component: Consult `REFERENCE.md#tailwind-mui-integration`
- Else if adding tests: Run `scripts/setup_playwright.py` and generate test file

### Phase 3: Validation
- Run `scripts/validate_component.py --accessibility --responsive`
- Execute Playwright tests: `npx playwright test`
- Generate `REPORT.md` with coverage and accessibility scores

## Quality Gates
- [ ] Component follows MUI design tokens and Tailwind utility classes
- [ ] Accessibility: WCAG 2.1 AA compliance (tested with axe-core)
- [ ] Responsive design: Mobile-first approach with Tailwind breakpoints
- [ ] Test coverage: 80%+ for critical user flows
- [ ] Performance: Bundle size under 200KB for component library

## Escalation Paths
If [complex animation or custom design system], suggest:
- "This requires design review because [reason: brand consistency]"
- "Consider enabling MCP server [figma] for design asset integration"
