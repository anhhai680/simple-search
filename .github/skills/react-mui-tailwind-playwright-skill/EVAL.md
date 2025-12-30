# Evaluation Criteria

## Success Metrics
| Dimension | Target | Measurement |
|-----------|--------|-------------|
| Accuracy  | 95%    | Generated components match MUI/Tailwind best practices |
| Speed     | <60s   | Time to generate component and tests |
| Completeness | 100% | All quality gates passed, tests run successfully |

## Test Cases
### Case 1: Happy Path - Generate MUI Button with Tailwind
**Input**: "Create a primary button component with MUI and Tailwind styling"
**Expected Output**:
- Generated files: `src/components/Button.jsx`, `tests/Button.spec.js`
- Exit code: 0
- Content includes: MUI Button import, Tailwind classes, Playwright test

### Case 2: Edge Case - Accessibility Violation
**Input**: Component with missing alt text or color contrast issues
**Expected Behavior**:
- Agent detects violation
- Provides structured error: `{"error": "accessibility_violation", "suggestion": "Add alt text or adjust colors"}`
- Does NOT generate invalid code

## Regression Tests
- `tests/fixtures/`: Sample React projects with MUI and Tailwind
- Run: `npm test -- --skill-mode`

## Human-in-the-Loop Scenarios
When to require manual approval:
- [ ] Custom design system integration
- [ ] Complex animations or interactions
- [ ] Third-party library conflicts
