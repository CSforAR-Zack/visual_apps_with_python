import tkinter as tk

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from dice import DiceRoller


def main():
    pack_style: dict = {"fill":"both", "expand":True}    
    font: tuple = ("Consolas", 20)

    # Create a window
    root: tk.Tk = tk.Tk()
    root.title("TKINTER IS WORKING")

    main_frame: tk.Frame = tk.Frame(root)
    main_frame.pack(padx=10, pady=10)

    die1_label: tk.Label = tk.Label(
        main_frame, text="Die 1 Sides:", font=font, anchor="w"
    )
    die1_label.pack(pack_style)   
    die1_entry: tk.Entry = tk.Entry(main_frame, font=font)
    die1_entry.pack(pack_style)

    die2_label: tk.Label = tk.Label(
        main_frame, text="Die 2 Sides:", font=font, anchor="w"
    )
    die2_label.pack(pack_style)   
    die2_entry: tk.Entry = tk.Entry(main_frame, font=font)
    die2_entry.pack(pack_style)   

    num_rolls_label: tk.Label = tk.Label(
        main_frame, text="Number of Rolls:", font=font, anchor="w"
    )
    num_rolls_label.pack(pack_style)
    num_rolls_entry: tk.Entry = tk.Entry(main_frame, font=font)
    num_rolls_entry.pack(pack_style)
    fig, ax = plt.subplots()
    
    ax.set_title(f"Results of rolling two dice.")
    ax.set_xlabel("Sum of two dice")
    ax.set_ylabel("Frequency of sum")

    canvas: FigureCanvasTkAgg = FigureCanvasTkAgg(fig, master=main_frame)

    dice_roller: DiceRoller = DiceRoller(
        die1_entry,
        die2_entry,
        num_rolls_entry,
        ax,
        canvas,
    )
    
    canvas_widget: tk.Widget = canvas.get_tk_widget()

    plt.tight_layout()

    canvas_widget.pack(padx=5, pady=5)

    roll_button: tk.Button = tk.Button(
        main_frame,
        text="Roll Dice",
        command=dice_roller.create_figure, 
        font=font,       
    )
    roll_button.pack(pack_style)

    root.protocol("WM_DELETE_WINDOW", lambda: on_closing(root))
    root.mainloop()


def on_closing(root: tk.Tk) -> None:
    """Handle the window closing event.
    This function is called when the window is closed.
    Matplotlib will not close the window automatically and is
    blocking the main thread with its event loop.
    """

    root.quit()
    root.destroy()

if __name__ == "__main__":
    main()