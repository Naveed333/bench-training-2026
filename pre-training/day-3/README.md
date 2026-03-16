## Usage Examples

```bash
# Add a task
python tasks.py add 'Fix login bug'

# Mark a task as done (by id)
python tasks.py done 1

# List all tasks
python tasks.py list

# List only completed tasks
python tasks.py list --filter done

# List only pending tasks
python tasks.py list --filter todo

# Delete a task (by id)
python tasks.py delete 2
```

## Why a class instead of just functions?

I used a `TaskManager` class because the task list needs to be loaded once and then shared across multiple operations in the same run. If I used plain functions, I'd have to pass the task list in and out of every single function, or reload the JSON file on every call.

With a class, `self.tasks` lives in one place, loaded once in `__init__`, used by all methods, and saved only when something changes. It keeps the state and the logic that operates on that state bundled together, which makes the code cleaner and easier.
