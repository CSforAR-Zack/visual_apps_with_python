import tkinter as tk

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from helpers import Color, Simulator


def main():
    # Font
    font: tuple = ("Consolas", 20)

    # Root Window
    root: tk.Tk = tk.Tk()
    root.title("Dice Roller")
    root.config(bg=Color.color4)

    # Main Frame
    main_frame: tk.Frame = tk.Frame(root, bg=Color.color4)
    main_frame.pack(fill="both", expand=True, padx=10, pady=10)

    # Widgets: Labels and Entry
    die1_label: tk.Label = tk.Label(
        main_frame, text="Die 1 Sides:", font=font, anchor="w", bg=Color.color4, fg=Color.color1
    )
    die1_label.pack(fill="x", expand=True)
    die1_entry: tk.Entry = tk.Entry(
        main_frame, font=font, bg=Color.color4, fg=Color.color1, insertbackground=Color.color1
    )
    die1_entry.pack(fill="x", expand=True)

    die2_label: tk.Label = tk.Label(
        main_frame, text="Die 2 Sides:", font=font, anchor="w", bg=Color.color4, fg=Color.color1
    )
    die2_label.pack(fill="x", expand=True)
    die2_entry: tk.Entry = tk.Entry(
        main_frame, font=font, bg=Color.color4, fg=Color.color1, insertbackground=Color.color1
    )
    die2_entry.pack(fill="x", expand=True)
    
    num_rolls_label: tk.Label = tk.Label(
        main_frame, text="Number of Rolls:", font=font, anchor="w", bg=Color.color4, fg=Color.color1
    )
    num_rolls_label.pack(fill="x", expand=True)
    num_rolls_entry: tk.Entry = tk.Entry(
        main_frame, font=font, bg=Color.color4, fg=Color.color1, insertbackground=Color.color1
    )
    num_rolls_entry.pack(fill="x", expand=True)

    # Figure and Canvas
    fig, ax = plt.subplots()

    ax.set_title("Results of Rolling Two Dice", fontsize=16, color=Color.color1)
    ax.set_xlabel("Sum of Two Dice", fontsize=14, color=Color.color1)
    ax.set_ylabel("Frequency of Sum", fontsize=14, color=Color.color1)

    fig.patch.set_facecolor(Color.color4)
    ax.set_facecolor(Color.color4)
    ax.spines["bottom"].set_color(Color.color1)
    ax.spines["top"].set_color(Color.color1)
    ax.spines["left"].set_color(Color.color1)
    ax.spines["right"].set_color(Color.color1)
    ax.tick_params(axis="x", colors=Color.color1)
    ax.tick_params(axis="y", colors=Color.color1)

    canvas: FigureCanvasTkAgg = FigureCanvasTkAgg(fig, master=main_frame)
    canvas_widget: tk.Widget = canvas.get_tk_widget()
    canvas_widget.pack(pady=5)

    dice_simulator: Simulator = Simulator(
        die1_entry,
        die2_entry,
        num_rolls_entry,
        ax,
        canvas,
    )

    # Button
    roll_button: tk.Button = tk.Button(
        main_frame,
        text="Roll Dice",
        command=dice_simulator.create_figure,
        font=font,
        bg=Color.color2,
        fg=Color.color1,
        activebackground=Color.color3,
    )
    roll_button.pack(fill="x", expand=True)

    # Root Window Loop and Closing
    root.protocol("WM_DELETE_WINDOW", lambda: on_closing(root))
    root.mainloop()


def on_closing(root: tk.Tk) -> None:
    """Handle the window closing all tk windows."""

    root.quit()
    root.destroy()


if __name__ == "__main__":
    main()