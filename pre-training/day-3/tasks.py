import json
import sys
import os
from datetime import datetime

TASKS_FILE = os.path.join(os.path.dirname(__file__), "tasks.json")


class TaskManager:
    def __init__(self):
        self.tasks = self._load_tasks()

    def _load_tasks(self):
        if not os.path.exists(TASKS_FILE):
            return []
        try:
            with open(TASKS_FILE, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            print("Warning: tasks.json is corrupt or unreadable. Starting fresh.")
            return []

    def _save_tasks(self):
        with open(TASKS_FILE, "w") as f:
            json.dump(self.tasks, f, indent=2)

    def _next_id(self):
        if not self.tasks:
            return 1
        return max(task["id"] for task in self.tasks) + 1

    def add_task(self, title):
        task = {
            "id": self._next_id(),
            "title": title,
            "status": "todo",
            "created_at": datetime.now().isoformat(),
        }
        self.tasks.append(task)
        self._save_tasks()
        print(f"Task added: [{task['id']}] {task['title']}")

    def complete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["status"] = "done"
                self._save_tasks()
                print(f"✔  Task {task_id} marked as done: {task['title']}")
                return
        print(f"Error: No task found with id {task_id}")

    def list_tasks(self, filter=None):
        filtered = self.tasks
        if filter:
            filtered = [t for t in self.tasks if t["status"] == filter]

        if not filtered:
            print("No tasks found.")
            return

        print(f"\n{'ID':<5} {'Status':<8} {'Created':<22} Title")
        print("-" * 60)
        for task in filtered:
            created = task["created_at"][:16].replace("T", " ")
            status = task["status"]
            print(f"{task['id']:<5} {status:<8} {created:<22} {task['title']}")
        print()

    def delete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                self.tasks.remove(task)
                self._save_tasks()
                print(f"Task {task_id} deleted: {task['title']}")
                return
        print(f"Error: No task found with id {task_id}")


def print_usage():
    print("""
Usage:
  python tasks.py add '<title>'       Add a new task
  python tasks.py done <id>           Mark task as done
  python tasks.py delete <id>         Delete a task
  python tasks.py list                List all tasks
  python tasks.py list --filter done  List only done tasks
  python tasks.py list --filter todo  List only todo tasks
""")


def main():
    manager = TaskManager()
    args = sys.argv[1:]

    if not args:
        print("Error: No command provided.")
        print_usage()
        return

    command = args[0]

    if command == "add":
        if len(args) < 2:
            print("Error: Please provide a task title. e.g. python tasks.py add 'Fix bug'")
            return
        manager.add_task(args[1])

    elif command == "done":
        if len(args) < 2:
            print("Error: Please provide a task id. e.g. python tasks.py done 3")
            return
        try:
            manager.complete_task(int(args[1]))
        except ValueError:
            print("Error: Task id must be a number.")

    elif command == "delete":
        if len(args) < 2:
            print("Error: Please provide a task id. e.g. python tasks.py delete 3")
            return
        try:
            manager.delete_task(int(args[1]))
        except ValueError:
            print("Error: Task id must be a number.")

    elif command == "list":
        filter_value = None
        if "--filter" in args:
            idx = args.index("--filter")
            if idx + 1 < len(args):
                filter_value = args[idx + 1]
                if filter_value not in ("todo", "done"):
                    print("Error: --filter must be 'todo' or 'done'")
                    return
            else:
                print("Error: --filter requires a value: 'todo' or 'done'")
                return
        manager.list_tasks(filter=filter_value)

    else:
        print(f"Unknown command: '{command}'")
        print_usage()


if __name__ == "__main__":
    main()
