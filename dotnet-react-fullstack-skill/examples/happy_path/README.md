# Happy Path Example: Task Management App

This example demonstrates a complete fullstack application using the .NET React skill.

## Project Structure

```
TaskManager/
├── src/
│   ├── TaskManager.Domain/
│   │   ├── Entities/
│   │   │   └── Task.cs
│   │   └── Interfaces/
│   │       └── ITaskRepository.cs
│   ├── TaskManager.Application/
│   │   ├── Commands/
│   │   │   ├── CreateTaskCommand.cs
│   │   │   └── UpdateTaskCommand.cs
│   │   ├── Queries/
│   │   │   └── GetTasksQuery.cs
│   │   ├── Handlers/
│   │   │   ├── CreateTaskCommandHandler.cs
│   │   │   └── GetTasksQueryHandler.cs
│   │   └── DTOs/
│   │       └── TaskDto.cs
│   ├── TaskManager.Infrastructure/
│   │   ├── Data/
│   │   │   └── ApplicationDbContext.cs
│   │   └── Repositories/
│   │       └── TaskRepository.cs
│   └── TaskManager.API/
│       ├── Controllers/
│       │   └── TasksController.cs
│       └── Program.cs
├── ClientApp/
│   ├── src/
│   │   ├── components/
│   │   │   └── TaskList.tsx
│   │   ├── store/
│   │   │   └── slices/
│   │   │       └── taskSlice.ts
│   │   └── App.tsx
│   └── package.json
└── tests/
    ├── TaskManager.API.Tests/
    └── e2e/
        └── task-management.spec.ts
```

## Key Features Demonstrated

- Clean Architecture with proper layer separation
- CQRS pattern for commands and queries
- Entity Framework Core with PostgreSQL
- RESTful API with proper HTTP methods
- React 18 with TypeScript
- Redux Toolkit for state management
- Playwright for E2E testing
- Fluent Validation for input validation
- Refit for API client (if external APIs needed)

## How to Run

1. Set up PostgreSQL database
2. Update connection string in `appsettings.json`
3. Run EF migrations: `dotnet ef database update`
4. Start backend: `dotnet run --project src/TaskManager.API`
5. Start frontend: `cd ClientApp && npm start`
6. Run tests: `./scripts/run_tests.sh`