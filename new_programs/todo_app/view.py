import tkinter as tk
from tkinter import simpledialog
from typing import List, Callable
from config import Theme, TodoItem
from pathlib import Path


class AppView(tk.Tk):
    """Handles UI layout and widgets."""
    
    def __init__(self):
        super().__init__()
        self.title(Theme.TITLE)
        self.geometry(f"{Theme.WIDTH}x{Theme.HEIGHT}")
        self.configure(bg=Theme.BG)

        # UI Callbacks to be set by the Controller
        self.add_cmd: Callable[[str], None] = None
        self.toggle_cmd: Callable[[int, bool], None] = None
        self.delete_cmd: Callable[[int], None] = None
        self.edit_cmd: Callable[[int, str], None] = None

        self._setup_ui()

    def _setup_ui(self) -> None:
        
        logo_path = Path(Theme.LOGO_FILE)
        if logo_path.is_file():
            try:
                # Load the image
                self.logo_image = tk.PhotoImage(file=str(logo_path))
                # Optional: Subsample makes it smaller (e.g., half size). Adjust as needed!
                self.logo_image = self.logo_image.subsample(Theme.LOGO_SUBSAMPLE) 
                
                self.logo_label = tk.Label(self, image=self.logo_image, bg=Theme.BG)
                self.logo_label.pack(pady=(20, 0)) # Add some padding at the top
            except tk.TclError:
                print("Warning: Could not load logo image format. (Use .png or .gif)")
        
        # Header
        tk.Label(self, text="My Tasks", bg=Theme.BG, fg=Theme.FG, font=Theme.FONT_TITLE).pack(pady=20)

        # Input Frame
        self.input_frame = tk.Frame(self, bg=Theme.BG)
        self.input_frame.pack(fill=tk.X, padx=20, pady=10)

        self.entry_var = tk.StringVar()
        self.entry = tk.Entry(
            self.input_frame,
            textvariable=self.entry_var,
            font=Theme.FONT_TEXT,
            width=25,
        )
        self.entry.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10))

        self.add_btn = tk.Button(
            self.input_frame,
            text="Add Task",
            bg=Theme.ACCENT,
            fg=Theme.FG,
            command=self._on_add_click,
        )
        self.add_btn.pack(side=tk.RIGHT)

        # List Frame (Where the To-Dos will live)
        self.list_frame = tk.Frame(self, bg=Theme.LIST_BG)
        self.list_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

    def bind_commands(
            self,
            add_cmd: Callable,
            toggle_cmd: Callable,
            delete_cmd: Callable,
            edit_cmd: Callable,
    ) -> None:
        """Allows the controller to wire up the logic."""
        self.add_cmd = add_cmd
        self.toggle_cmd = toggle_cmd
        self.delete_cmd = delete_cmd
        self.edit_cmd = edit_cmd

    def _prompt_edit(self, task_id: int, current_text: str) -> None:
        """Helper to open a dialog and pass the result to the controller."""
        # Open a popup asking for the new text, pre-filled with the current text
        new_text = simpledialog.askstring(
            "Edit Task", 
            "Update your task:", 
            initialvalue=current_text, 
            parent=self
        )
        
        # Only send the command if the user actually typed something and didn't hit 'Cancel'
        if new_text is not None and new_text.strip():
            if self.edit_cmd:
                self.edit_cmd(task_id, new_text.strip())

    def _on_add_click(self) -> None:
        """Triggered when the Add button is clicked."""
        task_text = self.entry_var.get().strip()
        if task_text and self.add_cmd:
            self.add_cmd(task_text)
            self.entry_var.set("") # Clear entry after adding

    def display_todos(self, todos: List[TodoItem]) -> None:
        """Wipes the current list and redraws it based on DB data."""
        # Clear existing widgets
        for widget in self.list_frame.winfo_children():
            widget.destroy()

        # Draw the new list
        for todo in todos:
            row = tk.Frame(self.list_frame, bg=Theme.LIST_BG)
            row.pack(fill=tk.X, pady=2)

            var = tk.BooleanVar(value=todo.is_completed)
            
            # Draw a checkbox for each item
            chk = tk.Checkbutton(
                row,
                text=todo.task,
                variable=var,
                bg=Theme.LIST_BG,
                fg=Theme.FG,
                selectcolor=Theme.BG,
                font=Theme.FONT_TEXT,
                anchor="w",
                # Pass the task ID and the new boolean state to the Controller
                # We use a lambda to capture the current todo's ID and the checkbox's variable
                # We use t_id and v as default arguments to avoid late binding issues in the loop
                command=lambda t_id=todo.id, v=var: self.toggle_cmd(t_id, v.get()),
            )
            
            # Strike-through effect if completed
            if todo.is_completed:
                chk.configure(
                    fg="#888888",
                    font=(Theme.FONT_TEXT[0], Theme.FONT_TEXT[1], "overstrike"),
                )
                
            chk.pack(side=tk.LEFT, fill=tk.X, expand=True)

            del_btn = tk.Button(
                row,
                text="X", 
                bg=Theme.DANGER, 
                fg=Theme.FG, 
                font=Theme.FONT_TEXT,
                borderwidth=0,
                # Pass the specific task ID back to the Controller
                # We use a lambda to capture the current todo's ID
                # We must create t_id as a default argument to avoid late binding issues in the loop
                command=lambda t_id=todo.id: self.delete_cmd(t_id) 
            )
            del_btn.pack(side=tk.RIGHT, padx=5)

            edit_btn = tk.Button(
                row,
                text="Edit", 
                bg=Theme.EDIT, 
                fg=Theme.FG, 
                font=Theme.FONT_TEXT,
                borderwidth=0,
                # Open the edit dialog with the current task text
                # We have to use a lambda to capture the current todo's ID and text
                # We must create t_id and t_text as default arguments to avoid late binding issues in the loop
                command=lambda t_id=todo.id, t_text=todo.task: self._prompt_edit(t_id, t_text)
            )
            edit_btn.pack(side=tk.RIGHT, padx=5)