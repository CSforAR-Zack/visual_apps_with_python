import tkinter as tk


def main():
    width: int = 500
    height: int = 300
    widgets_width: int = 40
    
    ### Customization Section ###
    colors: dict = {
        "console_bg": "black",
        "console_text": "lime green",
        "app_bg": "dark gray",
        "app_text": "white",
    }

    app_font: tuple = ("Consolas", 20)

    root: tk.Tk = tk.Tk()
    root.title("Hacker's Memo")
    root.geometry(f"{width}x{height}")
    root.minsize(width, height)
    root.maxsize(width, height)
    root.config(bg=colors["app_bg"])

    title_label: tk.Label = tk.Label(
        root,
        text="Hacker's Memo",
        fg=colors["app_text"],
        bg=colors["app_bg"],
        font=app_font,
    )
    title_label.pack()

    text_entry: tk.Text = tk.Text(root, height=10, width=widgets_width)
    text_entry.config(
        fg=colors["console_text"],
        bg=colors["console_bg"],
        insertbackground=colors["console_text"],
    )
    text_entry.pack()

    add_button: tk.Button = tk.Button(
        root,
        text="Add",
        width=widgets_width+5,
        fg=colors["app_text"],
        bg=colors["app_bg"],
        command=lambda: add_to_file(text_entry)
    )
    add_button.pack(pady=1)

    clear_screen_button: tk.Button = tk.Button(
        root,
        text="Clear Screen",
        width=widgets_width+5,
        fg=colors["app_text"],
        bg=colors["app_bg"],
        command=lambda: clear_screen(text_entry)
    )
    clear_screen_button.pack(pady=1)

    clear_file_button: tk.Button = tk.Button(
        root,
        text="Clear File",
        width=widgets_width+5,
        fg=colors["app_text"],
        bg=colors["app_bg"],
        command=lambda: clear_file(text_entry)
    )
    clear_file_button.pack(pady=1)

    root.mainloop()


def add_to_file(entry_text: tk.Text):
    """Add the text from the entry box to the memo file."""

    with open("memo.txt", "a") as f:
        f.write(entry_text.get("1.0", "end"))
    entry_text.delete("1.0", "end")


def clear_screen(entry_text: tk.Text):
    """Clear the text from the entry box."""

    entry_text.delete("1.0", "end")


def clear_file(entry_text: tk.Text):
    """Clear the memo file."""
    
    with open("memo.txt", "w") as f:
        f.write("")
    entry_text.delete("1.0", "end")
    entry_text.insert("1.0", "File Cleared!")


main()