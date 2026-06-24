import tkinter as tk
import json
from pathlib import Path


# --- Constants & Themes ---
PREF_FILE = Path("user_pref.json")
MEMO_FILE = Path("memo.txt")


THEMES = {
    "dark": {
        "app_bg": "dark grey",
        "app_text": "white",
        "console_text": "lime green",
        "console_bg": "black",
    },
    "light": {
        "app_bg": "white",
        "app_text": "black",
        "console_text": "black",
        "console_bg": "light grey",
    }
}


class HackersMemoApp:
    """Main application class for Hacker's Memo.
    
    Handles UI creation, theme management, and user preferences.
    """
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Hacker's Memo")
        
        width, height = 500, 350
        self.root.geometry(f"{width}x{height}")
        self.root.minsize(width, height)
        self.root.maxsize(width, height)

        self.widgets_width = 40
        self.app_font = ("Consolas", 20)

        # Load preferences
        self.prefs = self.load_prefs()
        self.current_theme = tk.StringVar(value=self.prefs.get("theme", "dark"))

        # Build UI
        self.create_widgets()
        
        # Apply initial theme
        self.apply_theme()

    # --- Setup & UI ---
    def create_widgets(self):
        """Initializes and packs all UI elements."""
        self.label = tk.Label(self.root, text="Hacker's Memo", font=self.app_font)
        self.label.pack(pady=(10, 0))

        self.entry_text = tk.Text(self.root, height=10, width=self.widgets_width)
        self.entry_text.pack(pady=5)

        self.add_button = tk.Button(
            self.root, text="Add", width=self.widgets_width+5, 
            command=self.add_to_file
        )
        self.add_button.pack()

        self.clear_screen_button = tk.Button(
            self.root, text="Clear Screen", width=self.widgets_width+5, 
            command=self.clear_screen
        )
        self.clear_screen_button.pack()

        self.clear_file_button = tk.Button(
            self.root, text="Clear File", width=self.widgets_width+5, 
            command=self.clear_file
        )
        self.clear_file_button.pack()

        self.theme_button = tk.Button(
            self.root, width=self.widgets_width+5, command=self.toggle_theme
        )
        self.theme_button.pack(pady=(10, 0))

    # --- Preference Handling ---
    def load_prefs(self) -> dict:
        """Load user preferences from JSON file."""
        if PREF_FILE.exists():
            with PREF_FILE.open("r") as f:
                return json.load(f)
        return {"theme": "light"}

    def save_prefs(self) -> None:
        """Save user preferences to JSON file."""
        with PREF_FILE.open("w") as f:
            json.dump({"theme": self.current_theme.get()}, f)

    # --- Theme Logic ---
    def apply_theme(self) -> None:
        """Apply the currently selected theme colors to all widgets."""
        theme = self.current_theme.get()
        colors = THEMES[theme]

        # Apply Theme to all widgets
        self.root.config(bg=colors["app_bg"])
        self.label.config(bg=colors["app_bg"], fg=colors["app_text"])
        
        self.entry_text.config(
            fg=colors["console_text"],
            bg=colors["console_bg"],
            insertbackground=colors["console_text"]
        )
        
        self.add_button.config(bg=colors["app_bg"], fg=colors["app_text"])
        self.clear_screen_button.config(bg=colors["app_bg"], fg=colors["app_text"])
        self.clear_file_button.config(bg=colors["app_bg"], fg=colors["app_text"])
        
        button_text = "Switch to Light Mode" if theme == "dark" else "Switch to Dark Mode"
        self.theme_button.config(
            text=button_text, bg=colors["app_bg"], fg=colors["app_text"]
        )

    def toggle_theme(self) -> None:
        """Switch the theme, update the UI, and save to JSON."""
        if self.current_theme.get() == "dark":
            new_theme = "light"
        else:
            new_theme = "dark"

        self.current_theme.set(new_theme)
        self.save_prefs()
        self.apply_theme()

    # --- File Operations ---
    def add_to_file(self) -> None:
        """Add text to file using pathlib."""
        with MEMO_FILE.open("a") as f:
            f.write(self.entry_text.get("1.0", "end"))
        self.entry_text.delete("1.0", "end")

    def clear_screen(self) -> None:
        """Clear the screen of the text widget."""
        self.entry_text.delete("1.0", "end")

    def clear_file(self) -> None:
        """Clear contents of file using pathlib."""
        with MEMO_FILE.open("w") as f:
            f.write("")
        self.entry_text.delete("1.0", "end")
        self.entry_text.insert("1.0", "File Cleared!")


def main():
    root = tk.Tk()
    app = HackersMemoApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()