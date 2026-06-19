import sqlite3
from typing import List, Callable
from config import TodoItem


class TodoModel:
    """Handles the SQLite database connection and operations."""
    
    def __init__(self):
        # Connect to the DB (creates the file if it doesn't exist)
        self.conn = sqlite3.connect("todos.db", check_same_thread=False)
        self._create_table()
        
        # Observer pattern setup
        self._observers: List[Callable[[List[TodoItem]], None]] = []

    def _create_table(self):
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS todos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    task TEXT NOT NULL,
                    is_completed BOOLEAN NOT NULL CHECK (is_completed IN (0, 1))
                )
            """)

    def add_observer(self, callback: Callable[[List[TodoItem]], None]) -> None:
        self._observers.append(callback)

    def fetch_all(self) -> None:
        """Grabs all todos from the database and broadcasts them."""
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, task, is_completed FROM todos")
        rows = cursor.fetchall()
        
        # Convert raw SQL tuples into nice TodoItem objects
        todos = [TodoItem(id=row[0], task=row[1], is_completed=bool(row[2])) for row in rows]
        self._notify_observers(todos)

    def add_task(self, task_text: str) -> None:
        """Inserts a new task and triggers an update."""
        with self.conn:
            self.conn.execute("INSERT INTO todos (task, is_completed) VALUES (?, 0)", (task_text,))
        self.fetch_all() # Update the UI

    def toggle_task(self, task_id: int, is_completed: bool) -> None:
        """Updates a task's status and triggers an update."""
        with self.conn:
            self.conn.execute("UPDATE todos SET is_completed = ? WHERE id = ?", (int(is_completed), task_id))
        self.fetch_all() # Update the UI

    def delete_task(self, task_id: int) -> None:
        """Deletes a task from the database and triggers an update."""
        with self.conn:
            self.conn.execute("DELETE FROM todos WHERE id = ?", (task_id,))
        self.fetch_all() # Update the UI

    def edit_task(self, task_id: int, new_text: str) -> None:
        """Updates a task's text and triggers an update."""
        with self.conn:
            self.conn.execute("UPDATE todos SET task = ? WHERE id = ?", (new_text, task_id))
        self.fetch_all() # Update the UI

    def _notify_observers(self, todos: List[TodoItem]) -> None:
        for observer in self._observers:
            observer(todos)