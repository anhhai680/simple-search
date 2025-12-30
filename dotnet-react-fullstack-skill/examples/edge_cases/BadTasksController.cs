// BAD EXAMPLE - Business logic in controller
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using TaskManager.Infrastructure.Data;

namespace TaskManager.API.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class BadTasksController : ControllerBase
    {
        private readonly ApplicationDbContext _context;

        public BadTasksController(ApplicationDbContext context)
        {
            _context = context;
        }

        [HttpGet]
        public async Task<IActionResult> GetTasks()
        {
            // Direct database access in controller - violates Clean Architecture
            var tasks = await _context.Tasks.ToListAsync();
            return Ok(tasks);
        }

        [HttpPost]
        public async Task<IActionResult> CreateTask(Task task)
        {
            // Business logic and validation in controller - WRONG!
            if (string.IsNullOrEmpty(task.Title))
                return BadRequest("Title is required");

            if (task.Title.Length > 100)
                return BadRequest("Title too long");

            // Direct domain logic here
            task.CreatedAt = DateTime.UtcNow;

            _context.Tasks.Add(task);
            await _context.SaveChangesAsync();

            return Ok(task);
        }
    }
}