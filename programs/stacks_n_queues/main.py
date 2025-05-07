import tkinter as tk
from tkinter.font import Font

from mod import Stack, Queue
from helpers import Boxes


def main():
    # Create a window
    window = tk.Tk()
    window.title("Visualizer")
    font = Font(family="Helvetica", size=14)

    # Frames
    left: tk.Frame = tk.Frame(window)
    right: tk.Frame = tk.Frame(window)
    left.pack(side="left", expand=True, fill="both")
    right.pack(side="right", expand=True, fill="both")

    # Create Stack Section
    s: Stack = Stack()
    s_items: tk.Frame  = tk.Frame(left)
    s_label: tk.Label = tk.Label(left, text="Stack", font=font)
    s_output: tk.Label = tk.Label(left, text="-", font=font)
    s_entry: tk.Label = tk.Entry(left, font=font)

    s_center: Boxes = Boxes(
        s, s_items, s_entry, s_output, window, font
    )

    s_buttons: tk.Frame = tk.Frame(left)
    s_push: tk.Button = tk.Button(
        s_buttons, text="Push", command=s_center.add_box, font=font
    )
    s_pop: tk.Button  = tk.Button(
        s_buttons, text="Pop", command=s_center.get_box, font=font
    )
    s_peek: tk.Button  = tk.Button(
        s_buttons, text="Peek", command=s_center.peek_box, font=font
    )
    
    s_label.pack()
    s_output.pack()
    s_entry.pack()
    s_buttons.pack()
    s_push.pack(side="left")
    s_pop.pack(side="left")
    s_peek.pack(side="left")
    s_items.pack(fill="x")

    # Create Queue Section
    q: Queue = Queue()
    q_items: tk.Frame = tk.Frame(right)
    q_label: tk.Label = tk.Label(right, text="Queue", font=font)
    q_output: tk.Label = tk.Label(right, text="-", font=font)
    q_entry: tk.Entry = tk.Entry(right, font=font)

    q_center = Boxes(q, q_items, q_entry, q_output, window, font)

    q_buttons: tk.Frame = tk.Frame(right)
    add_button: tk.Button  = tk.Button(
        q_buttons, text="Add", command=q_center.add_box, font=font
    )
    remove_button: tk.Button  = tk.Button(
        q_buttons, text="Remove", command=q_center.get_box, font=font
    )
    q_peek_button: tk.Button  = tk.Button(
        q_buttons, text="Peek", command=q_center.peek_box, font=font
    )

    q_label.pack()
    q_output.pack()
    q_entry.pack()

    q_buttons.pack()
    add_button.pack(side="left")
    remove_button.pack(side="left")
    q_peek_button.pack(side="left")
    q_items.pack(fill="x")

    # Last thing in main...
    window.mainloop()


def update_window(items: Boxes, wn: tk.Tk) -> None:
    """Update the canvas with the stack"""

    for box in items:
        box.label.pack_forget()
    for box in items:
        box.label.pack(expand=True, fill="both", padx=1, pady=1, anchor="n", side="top")

    wn.update()


if __name__ == "__main__":
    main()