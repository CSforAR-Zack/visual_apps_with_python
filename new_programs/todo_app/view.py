import tkinter as tk
from tkinter import simpledialog
from typing import Callable
from config import Theme
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

    def display_todos(self, todos: list) -> None:
        """Wipes the current list and redraws it based on DB data."""
        # Clear existing widgets
        for widget in self.list_frame.winfo_children():
            widget.destroy()

        # Draw the new list
        for todo in todos:
            TaskRow(
                parent=self.list_frame,
                todo=todo,
                toggle_cb=self.toggle_cmd,
                delete_cb=self.delete_cmd,
                edit_cb=self._prompt_edit,
            )


class TaskRow(tk.Frame):
    """A custom widget representing a single task in the UI."""
    
    def __init__(self, parent, todo, toggle_cb, delete_cb, edit_cb):
        super().__init__(parent, bg=Theme.LIST_BG)
        self.todo = todo
        
        # Callbacks passed down from AppView
        self.toggle_cb = toggle_cb
        self.delete_cb = delete_cb
        self.edit_cb = edit_cb

        self._setup_ui()

    def _setup_ui(self):
        self.pack(fill=tk.X, pady=2)

        self.var = tk.BooleanVar(value=self.todo.is_completed)
        
        # Checkbox
        self.chk = tk.Checkbutton(
            self,
            text=self.todo.task,
            variable=self.var,
            bg=Theme.LIST_BG,
            fg=Theme.FG,
            selectcolor=Theme.BG,
            font=Theme.FONT_TEXT,
            anchor="w",
            command=self._on_toggle,
        )
        
        if self.todo.is_completed:
            self.chk.configure(
                fg="#888888",
                font=(Theme.FONT_TEXT[0], Theme.FONT_TEXT[1], "overstrike"),
            )
            
        self.chk.pack(side=tk.LEFT, fill=tk.X, expand=True)

        # Delete Button
        del_btn = tk.Button(
            self,
            text="X",
            bg=Theme.DANGER,
            fg=Theme.FG,
            font=Theme.FONT_TEXT,
            borderwidth=0,
            command=self._on_delete,
        )
        del_btn.pack(side=tk.RIGHT, padx=5)

        # Edit Button
        edit_btn = tk.Button(
            self,
            text="Edit",
            bg=Theme.EDIT,
            fg=Theme.FG, 
            font=Theme.FONT_TEXT,
            borderwidth=0,
            command=self._on_edit,
        )
        edit_btn.pack(side=tk.RIGHT, padx=5)

    # --- Clean Click Handlers ---
    def _on_toggle(self):
        self.toggle_cb(self.todo.id, self.var.get())

    def _on_delete(self):
        self.delete_cb(self.todo.id)

    def _on_edit(self):
        self.edit_cb(self.todo.id, self.todo.task)