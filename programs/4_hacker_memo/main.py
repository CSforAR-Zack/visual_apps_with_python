import tkinter as tk


def main():
    width: int = 500
    height: int = 300
    widgets_width: int = 40
    
    ### Customization Section ###
    # You can customize the colors
    colors: dict = {
        "console_bg": "black",
        "console_text": "lime green",
        "app_bg": "dark gray",
        "app_text": "white",
    }

    # You can customize your font family
    app_font: tuple = ("Consolas", 20)

    wn: tk.Tk = tk.Tk()
    wn.title("Hacker's Memo")
    wn.geometry(f"{width}x{height}")
    wn.minsize(width, height)
    wn.maxsize(width, height)
    wn.config(bg=colors["app_bg"])

    label: tk.Label = tk.Label(
        wn,
        text="Hacker's Memo",
        fg=colors["app_text"],
        bg=colors["app_bg"],
        font=app_font,
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
        width=widgets_width+5,
        fg=colors["app_text"],
        bg=colors["app_bg"],
        command=lambda: add_to_file(entry_text)
    )
    add_button.pack(pady=1)

    clear_screen_button: tk.Button = tk.Button(
        wn,
        text="Clear Screen",
        width=widgets_width+5,
        fg=colors["app_text"],
        bg=colors["app_bg"],
        command=lambda: clear_screen(entry_text)
    )
    clear_screen_button.pack(pady=1)

    clear_file_button: tk.Button = tk.Button(
        wn,
        text="Clear File",
        width=widgets_width+5,
        fg=colors["app_text"],
        bg=colors["app_bg"],
        command=lambda: clear_file(entry_text)
    )
    clear_file_button.pack(pady=1)

    wn.mainloop()


def add_to_file(entry_text: tk.Text):
    with open("memo.txt", "a") as f:
        f.write(entry_text.get("1.0", "end"))
    entry_text.delete("1.0", "end")


def clear_screen(entry_text: tk.Text):
    entry_text.delete("1.0", "end")


def clear_file(entry_text: tk.Text):
    with open("memo.txt", "w") as f:
        f.write("")
    entry_text.delete("1.0", "end")
    entry_text.insert("1.0", "File Cleared!")


main()