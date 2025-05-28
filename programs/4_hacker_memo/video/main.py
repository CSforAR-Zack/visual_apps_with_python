import tkinter as tk


def main():
    width: int = 500
    height: int = 300
    widgets_width: int = 40

    app_font: tuple = ("Consolas", 20)

    colors: dict = {
        "app_bg": "dark grey",
        "app_text": "white",
        "console_text": "lime green",
        "console_bg": "black",
    }

    root: tk.Tk = tk.Tk()
    root.title("Hacker's Memo")
    root.geometry(f"{width}x{height}")
    root.minsize(width, height)
    root.maxsize(width, height)
    root.config(bg=colors["app_bg"])

    label: tk.Label = tk.Label(
        root,
        text="Hacker's Memo",
        bg=colors["app_bg"],
        fg=colors["app_text"],
        font=app_font,
    )
    label.pack()

    entry_text: tk.Text = tk.Text(root, height=10, width=widgets_width)
    entry_text.config(
        fg=colors["console_text"],
        bg=colors["console_bg"],
        insertbackground=colors["console_text"],
    )
    entry_text.pack()

    add_button: tk.Button = tk.Button(
        root,
        text="Add",
        bg=colors["app_bg"],
        fg=colors["app_text"],
        width=widgets_width+5,
        command=lambda: add_to_file(entry_text),
    )
    add_button.pack()

    clear_screen_button: tk.Button = tk.Button(
        root,
        text="Clear Screen",
        bg=colors["app_bg"],
        fg=colors["app_text"],
        width=widgets_width+5,
        command=lambda: clear_screen(entry_text),
    )
    clear_screen_button.pack()

    clear_file_button: tk.Button = tk.Button(
        root,
        text="Clear File",
        bg=colors["app_bg"],
        fg=colors["app_text"],
        width=widgets_width+5,
        command=lambda: clear_file(entry_text),
    )
    clear_file_button.pack()

    root.mainloop()


def add_to_file(entry_text: tk.Text) -> None:
    """Add text to file."""
    
    with open("memo.txt", "a") as f:
        f.write(entry_text.get("1.0", "end"))
    entry_text.delete("1.0", "end")


def clear_screen(entry_text: tk.Text) -> None:
    """Clear the screen of the text wdiget."""
    
    entry_text.delete("1.0", "end")


def clear_file(entry_text: tk.Text) -> None:
    """Clear contents of file."""
    
    with open("memo.txt", "w") as f:
        f.write("")
    entry_text.delete("1.0", "end")
    entry_text.insert("1.0", "File Cleared!")


if __name__ == "__main__":
    main()


# Useful methods for the Text widget to consider:

# entry_text.get(start, end):
# Retrieves text from the entry_text widget. 
# start and end define the range of text to retrieve. 
# "1.0" represents the first character ("1.0") of the first line ("1.0"),
# and "end" represents the end of the entire text.
# For example, entry_text.get("1.0", "end") gets all the text in the widget.

# entry_text.delete(start, end):
# Deletes text from the entry_text widget.
# start and end define the range of text to retrieve.
# "1.0" represents the first character ("1.0") of the first line ("1.0"),
# and "end" represents the end of the entire text.
# For example, entry_text.delete("1.0", "end") clears all the text in the widget.

# entry_text.insert(index, text):
# Inserts text into the entry_text widget at the specified index.
# "1.0" represents the first character ("1.0") of the first line ("1.0").
# For example, entry_text.insert("1.0", "Hello!") inserts "Hello!" at the beginning of the widget.
