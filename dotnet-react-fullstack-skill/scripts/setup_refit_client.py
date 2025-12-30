#!/usr/bin/env python3
"""
Generates Refit client interface for API consumption.
Usage: python setup_refit_client.py <api_name> <base_url> [--output-dir src/Infrastructure]
Exit codes: 0=success, 1=invalid args, 2=file exists
"""
import sys
from pathlib import Path

def generate_refit_client(api_name: str, base_url: str) -> str:
    """Generate Refit client interface."""
    client_name = f"I{api_name}ApiClient"

    return f"""using Refit;
using System.Threading.Tasks;

namespace Infrastructure.Clients
{{
    public interface {client_name}
    {{
        // Add API endpoints here
        [Get("/api/users")]
        Task<List<UserDto>> GetUsers();

        [Get("/api/users/{{id}}")]
        Task<UserDto> GetUser(int id);

        [Post("/api/users")]
        Task<UserDto> CreateUser([Body] CreateUserRequest request);

        [Put("/api/users/{{id}}")]
        Task UpdateUser(int id, [Body] UpdateUserRequest request);

        [Delete("/api/users/{{id}}")]
        Task DeleteUser(int id);
    }}

    // DTOs
    public class UserDto
    {{
        public int Id {{ get; set; }}
        public string Name {{ get; set; }}
        public string Email {{ get; set; }}
    }}

    public class CreateUserRequest
    {{
        public string Name {{ get; set; }}
        public string Email {{ get; set; }}
    }}

    public class UpdateUserRequest
    {{
        public string Name {{ get; set; }}
        public string Email {{ get; set; }}
    }}
}}
"""

def generate_service_registration(api_name: str, base_url: str) -> str:
    """Generate service registration code."""
    client_name = f"I{api_name}ApiClient"

    return f"""// In Program.cs or Startup.cs
builder.Services.AddRefitClient<{client_name}>()
    .ConfigureHttpClient(c => c.BaseAddress = new Uri("{base_url}"));

// Usage in service
public class {api_name}Service
{{
    private readonly {client_name} _client;

    public {api_name}Service({client_name} client)
    {{
        _client = client;
    }}

    public async Task<List<UserDto>> GetUsersAsync()
    {{
        return await _client.GetUsers();
    }}
}}
"""

def main():
    if len(sys.argv) < 3:
        print("Usage: python setup_refit_client.py <api_name> <base_url> [--output-dir src/Infrastructure]", file=sys.stderr)
        sys.exit(1)

    api_name = sys.argv[1]
    base_url = sys.argv[2]

    output_dir = "src/Infrastructure"
    if "--output-dir" in sys.argv:
        idx = sys.argv.index("--output-dir")
        if idx + 1 < len(sys.argv):
            output_dir = sys.argv[idx + 1]

    output_path = Path(output_dir) / "Clients"
    output_path.mkdir(parents=True, exist_ok=True)

    # Generate client interface
    client_file = output_path / f"{api_name}ApiClient.cs"
    if client_file.exists():
        print(f"Client file {client_file} already exists", file=sys.stderr)
        sys.exit(2)

    client_content = generate_refit_client(api_name, base_url)
    with open(client_file, 'w') as f:
        f.write(client_content)

    print(f"Generated Refit client: {client_file}")

    # Generate registration example
    registration_file = output_path / f"{api_name}ServiceRegistration.cs"
    if not registration_file.exists():
        registration_content = generate_service_registration(api_name, base_url)
        with open(registration_file, 'w') as f:
            f.write(registration_content)
        print(f"Generated service registration: {registration_file}")

    print("Refit client setup completed!")

if __name__ == "__main__":
    main()