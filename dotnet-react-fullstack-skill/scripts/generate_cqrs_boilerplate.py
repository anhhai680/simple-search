#!/usr/bin/env python3
"""
Generates CQRS boilerplate code for commands and queries.
Usage: python generate_cqrs_boilerplate.py <entity_name> <operation> [--output-dir src/Application]
Exit codes: 0=success, 1=invalid args, 2=file exists
"""
import sys
import os
from pathlib import Path
from typing import Optional

def generate_command(entity: str, operation: str) -> str:
    """Generate a command class."""
    class_name = f"{operation}{entity}Command"
    return f"""using MediatR;

namespace Application.Commands
{{
    public class {class_name} : IRequest<int>
    {{
        // Add properties here
        public string Name {{ get; set; }}
        // public int Id {{ get; set; }}
    }}
}}"""

def generate_command_handler(entity: str, operation: str) -> str:
    """Generate a command handler."""
    command_class = f"{operation}{entity}Command"
    handler_class = f"{command_class}Handler"
    return f"""using MediatR;
using Domain.Interfaces;

namespace Application.Handlers
{{
    public class {handler_class} : IRequestHandler<{command_class}, int>
    {{
        private readonly IRepository<{entity}> _repository;

        public {handler_class}(IRepository<{entity}> repository)
        {{
            _repository = repository;
        }}

        public async Task<int> Handle({command_class} request, CancellationToken cancellationToken)
        {{
            // Implement command logic here
            var entity = new {entity} {{ Name = request.Name }};
            await _repository.AddAsync(entity);
            await _repository.SaveChangesAsync();
            return entity.Id;
        }}
    }}
}}"""

def generate_query(entity: str, operation: str) -> str:
    """Generate a query class."""
    class_name = f"Get{entity}Query"
    return f"""using MediatR;

namespace Application.Queries
{{
    public class {class_name} : IRequest<{entity}Dto>
    {{
        public int Id {{ get; set; }}
    }}
}}"""

def generate_query_handler(entity: str, operation: str) -> str:
    """Generate a query handler."""
    query_class = f"Get{entity}Query"
    handler_class = f"{query_class}Handler"
    return f"""using MediatR;
using Domain.Interfaces;

namespace Application.Handlers
{{
    public class {handler_class} : IRequestHandler<{query_class}, {entity}Dto>
    {{
        private readonly IRepository<{entity}> _repository;

        public {handler_class}(IRepository<{entity}> repository)
        {{
            _repository = repository;
        }}

        public async Task<{entity}Dto> Handle({query_class} request, CancellationToken cancellationToken)
        {{
            var entity = await _repository.GetByIdAsync(request.Id);
            return new {entity}Dto
            {{
                Id = entity.Id,
                Name = entity.Name
            }};
        }}
    }}
}}"""

def generate_validator(entity: str, operation: str) -> str:
    """Generate Fluent Validation validator."""
    command_class = f"{operation}{entity}Command"
    validator_class = f"{command_class}Validator"
    return f"""using FluentValidation;

namespace Application.Validators
{{
    public class {validator_class} : AbstractValidator<{command_class}>
    {{
        public {validator_class}()
        {{
            RuleFor(x => x.Name).NotEmpty().MaximumLength(100);
        }}
    }}
}}"""

def generate_dto(entity: str) -> str:
    """Generate DTO class."""
    return f"""namespace Application.DTOs
{{
    public class {entity}Dto
    {{
        public int Id {{ get; set; }}
        public string Name {{ get; set; }}
    }}
}}"""

def main():
    if len(sys.argv) < 3:
        print("Usage: python generate_cqrs_boilerplate.py <entity_name> <operation> [--output-dir src/Application]", file=sys.stderr)
        sys.exit(1)

    entity = sys.argv[1]
    operation = sys.argv[2]

    output_dir = "src/Application"
    if "--output-dir" in sys.argv:
        idx = sys.argv.index("--output-dir")
        if idx + 1 < len(sys.argv):
            output_dir = sys.argv[idx + 1]

    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    # Generate files
    files_to_generate = [
        (f"{operation}{entity}Command.cs", generate_command(entity, operation)),
        (f"{operation}{entity}CommandHandler.cs", generate_command_handler(entity, operation)),
        (f"Get{entity}Query.cs", generate_query(entity, operation)),
        (f"Get{entity}QueryHandler.cs", generate_query_handler(entity, operation)),
        (f"{operation}{entity}CommandValidator.cs", generate_validator(entity, operation)),
        (f"{entity}Dto.cs", generate_dto(entity)),
    ]

    for filename, content in files_to_generate:
        file_path = output_path / filename
        if file_path.exists():
            print(f"File {file_path} already exists, skipping", file=sys.stderr)
            continue

        with open(file_path, 'w') as f:
            f.write(content)
        print(f"Generated {file_path}")

    print("CQRS boilerplate generated successfully!")

if __name__ == "__main__":
    main()