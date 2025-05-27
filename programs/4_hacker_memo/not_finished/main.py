import tkinter as tk


def main():
    width: int = 500
    height: int = 300
    widgets_width: int = 40

    # You can change font and colors
    app_font: tuple = ("Consolas", 20)

    colors: dict = {
        "console_bg": "black",
        "console_text": "lime green",
        "app_bg": "dark grey",
        "app_text": "white",
    }

    wn: tk.Tk = tk.Tk()
    wn.title("Hacker's Memo")
    wn.geometry(f"{width}x{height}")
    wn.minsize(width, height)
    wn.maxsize(width, height)
    wn.config(bg=colors["app_bg"])

    label: tk.Label = tk.Label(
        wn,
        text="Hacker's Memo",
        font=app_font,
        bg=colors["app_bg"],
        fg=colors["app_text"],
    )
    label.pack()

    entry_text: tk.Text = tk.Text(wn, height=10, width=widgets_width)
    entry_text.config(
        fg=colors["console_text"],
        bg=colors["console_bg"],
        insertbackground=colors["console_text"],
    )
    entry_text.pack()

    add_button: tk.Button = tk.Button(
        wn,
        text="Add",
        width=widgets_width + 5,
        bg=colors["app_bg"],
        fg=colors["app_text"],
        command=lambda : add_to_file(entry_text),
    )
    add_button.pack()

    clear_screen_button: tk.Button = tk.Button(
        wn,
        text="Clear Screen",
        width=widgets_width + 5,
        bg=colors["app_bg"],
        fg=colors["app_text"],
        command=lambda : clear_screen(entry_text),
    )
    clear_screen_button.pack()

    clear_file_button: tk.Button = tk.Button(
        wn,
        text="Clear File",
        width=widgets_width + 5,
        bg=colors["app_bg"],
        fg=colors["app_text"],
        command=lambda : clear_file(entry_text),
    )
    clear_file_button.pack()    

    wn.mainloop()


def add_to_file(entry_text: tk.Text) -> None:
    print("Adding to file....DELETE THIS")
    # Add the text from entry_text to the memo.txt file.
    # Use with open() when working with files.
    # Reference "useful methods" in the assignment guidelines.


def clear_screen(entry_text: tk.Text) -> None:
    print("Clearing screen....DELETE THIS")
    # Clear the entry_text widget.
    # Reference "useful methods" in the assignment guidelines.


def clear_file(entry_text: tk.Text) -> None:
    print("Clearing file....DELETE THIS")
    # Clear the memo.txt file and update the entry_text widget.
    # Use with open() when working with files.
    # Consider the file mode for write operations.
    # Reference "useful methods" in the assignment guidelines.


main()