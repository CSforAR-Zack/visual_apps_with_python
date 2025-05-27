import tkinter as tk
from tkinter import filedialog
import re


def main():
    # Colors and font    
    font: tuple = ("Consolas", 30)
    colors: dict = {
        "bg": "black",
        "text": "white",
        "flag_text": "limegreen"
    }

    root: tk.Tk = tk.Tk()
    root.title("Capture the Flag")
    root.geometry("700x150")
    root.configure(bg=colors["bg"])

    top_frame: tk.Frame = tk.Frame(root)
    top_frame.pack(
        side="top",
        anchor="w",
        padx=10,
        pady=10,
    )

    flag_label: tk.Label = tk.Label(
        top_frame,
        text="Flag:",
        font=font,
        fg=colors["text"],
        bg=colors["bg"],
    )
    flag_label.pack(side="left")

    flag_value_label: tk.Label = tk.Label(
        top_frame,
        text="",
        font=font,
        fg=colors["flag_text"],
        bg=colors["bg"],
    )
    flag_value_label.pack(side="left")


    bottom_frame: tk.Frame = tk.Frame(root)
    bottom_frame.pack(
        side="bottom",
        fill="both",
        padx=10,
        pady=10,
    )

    search_button: tk.Button = tk.Button(
        bottom_frame,
        text="FIND",
        font = font,
        command = lambda: find_flag(flag_value_label),
    )
    search_button.pack(fill="both")

    root.mainloop()


def find_flag(result_label: tk.Label) -> None:
    """Find flag in file and update Label with result"""

    filename = filedialog.askopenfilename()

    with open(filename, "r") as file:
        text = file.read()

    pattern: str = r"FLAG"
    results: re.Match = re.search(pattern, text)
    
    if results:
        value: str = results.group()
        result_label.config(text=value)
    else:
        result_label.config(text="No Flag Found!")


if __name__ == "__main__":
    main()