class Task:
    def __init__(self, title, completed=False):
        self.title = title
        self.completed = completed
    
    def mark_complete(self):
        self.completed = True
    
    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.title}"

class User:
    def __init__(self, username):
        self.username = username
        self.tasks = []
    
    def add_task(self, title):
        task = Task(title)
        self.tasks.append(task)
        return f"Task '{title}' added for {self.username}"
    
    def complete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_complete()
            return f"Task '{self.tasks[task_index].title}' marked as complete"
        return f"Task index {task_index} not found"
    
    def list_tasks(self):
        if not self.tasks:
            return "No tasks found"
        return "\n".join([f"{i}: {task}" for i, task in enumerate(self.tasks)])

# Global user storage (simple demo)
users = {}

def get_or_create_user(username):
    if username not in users:
        users[username] = User(username)
    return users[username]