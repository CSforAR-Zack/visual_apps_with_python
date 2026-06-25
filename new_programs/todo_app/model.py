import sqlite3
from typing import List, Callable
from config import TodoItem


class TodoModel:
    """Handles the SQLite database connection using a Singleton pattern."""
    
    # This is a class-level variable to hold the single instance of TodoModel
    _instance = None 

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(TodoModel, cls).__new__(cls)            
            cls._instance._is_initialized = False 
            
        return cls._instance
    
    def __init__(self, db_name: str = "todos.db"):
        # Check if the instance has already been initialized to avoid re-initialization
        if self._is_initialized:
            return
            
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self._create_table()
        
        self._observers: List[Callable[[List[TodoItem]], None]] = []
        
        self._is_initialized = True # Mark the instance as initialized

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