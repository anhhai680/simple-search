using System;

namespace TaskManager.Domain.Entities
{
    public class Task
    {
        public int Id { get; set; }
        public string Title { get; set; }
        public string Description { get; set; }
        public bool IsCompleted { get; set; }
        public DateTime CreatedAt { get; set; }
        public DateTime? CompletedAt { get; set; }

        // Domain methods
        public void MarkAsCompleted()
        {
            IsCompleted = true;
            CompletedAt = DateTime.UtcNow;
        }

        public void UpdateDetails(string title, string description)
        {
            Title = title;
            Description = description;
        }
    }
}