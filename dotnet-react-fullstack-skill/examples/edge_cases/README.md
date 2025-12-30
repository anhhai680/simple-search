# Edge Cases and Common Mistakes

This directory contains examples of problematic implementations that violate best practices.

## Common Issues

### 1. Business Logic in Controllers
**Problem**: Controllers contain business logic instead of delegating to application layer.

**Bad Example**:
```csharp
[HttpPost]
public async Task<IActionResult> CreateTask(CreateTaskRequest request)
{
    // Business logic in controller - WRONG!
    if (string.IsNullOrEmpty(request.Title))
        return BadRequest("Title is required");

    var task = new Task { Title = request.Title };
    _context.Tasks.Add(task);
    await _context.SaveChangesAsync();

    return Ok(task);
}
```

**Why it's wrong**: Violates Clean Architecture, mixes concerns, hard to test.

### 2. Missing CQRS Separation
**Problem**: Same model used for both read and write operations.

**Bad Example**:
```csharp
public class TaskModel
{
    public int Id { get; set; }
    public string Title { get; set; }
    // 50+ properties used in all contexts
}
```

**Why it's wrong**: Read models often need different data than write models.

### 3. Tight Coupling in React Components
**Problem**: Components directly call APIs and manage complex state.

**Bad Example**:
```tsx
const TaskList = () => {
  const [tasks, setTasks] = useState([]);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    fetch('/api/tasks')
      .then(res => res.json())
      .then(setTasks)
      .finally(() => setLoading(false));
  }, []);

  // Complex state logic here...
};
```

**Why it's wrong**: Hard to test, business logic in UI, no error handling.

### 4. Missing Validation
**Problem**: No input validation on API endpoints.

**Bad Example**:
```csharp
[HttpPost]
public async Task<IActionResult> CreateTask(Task task)
{
    _context.Tasks.Add(task);
    await _context.SaveChangesAsync();
    return Ok(task);
}
```

**Why it's wrong**: Allows invalid data, security risks.

## How the Skill Handles These

The validation script (`validate_architecture.py`) will detect these issues and provide specific recommendations for fixes. The generation scripts create proper implementations following best practices.