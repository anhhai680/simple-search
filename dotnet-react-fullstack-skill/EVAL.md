# Evaluation Criteria

## Success Metrics
| Dimension | Target | Measurement |
|-----------|--------|-------------|
| Accuracy  | 95%    | Generated code compiles and runs without errors |
| Speed     | <30s   | Time to generate complete feature implementation |
| Completeness | 100% | All architectural patterns and quality gates satisfied |
| Test Coverage | 80% | Automated tests cover critical paths |

## Test Cases
### Case 1: Happy Path - Fullstack CRUD Application
**Input**: "Build a task management app with .NET backend and React frontend"
**Expected Output**:
- Generated files: Clean Architecture layers, CQRS commands/queries, React components with Redux, Playwright tests
- Exit code: 0
- Content includes: Proper separation of concerns, validation, state management, UI tests
- Database: PostgreSQL schema created via EF migrations
- API: RESTful endpoints with BFF optimization

### Case 2: Edge Case - CQRS Implementation
**Input**: "Implement CQRS for product catalog with complex queries"
**Expected Behavior**:
- Agent generates separate command and query handlers
- Uses MediatR for dispatching
- Implements read models for optimized queries
- Validates with Fluent Validation

### Case 3: Edge Case - React Component with Redux
**Input**: "Create a user profile component with form validation"
**Expected Behavior**:
- Generates TypeScript React component
- Implements Redux slice for state management
- Uses form validation library
- Includes error handling and loading states

### Case 4: Error Handling - Invalid Project Structure
**Input**: Project with mixed architecture layers
**Expected Behavior**:
- Agent detects violations
- Provides structured error: `{"error": "Architecture violation", "details": "Business logic in controller", "fix": "Move to Application layer"}`
- Does NOT generate additional invalid code

## Regression Tests
- `tests/fixtures/happy_path/`: Complete sample application
- `tests/fixtures/edge_cases/`: Projects with intentional violations
- Run: `python -m pytest tests/ --skill-mode`

## Human-in-the-Loop Scenarios
When to require manual approval:
- [ ] Complex business domain logic requiring expert knowledge
- [ ] Security-sensitive features (authentication, authorization)
- [ ] Performance-critical code paths
- [ ] Integration with external APIs or services
- [ ] Database schema changes affecting production data
- [ ] UI/UX design decisions
- [ ] Regulatory compliance requirements