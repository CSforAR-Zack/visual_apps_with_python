import tkinter as tk

from random import randint
from time import sleep


def main():
    # This are the variables you can change
    number_of_bars: int = 40
    width: int = 10
    max_height: int = 500
    x_pad: int = 1
    y_pad: int = 5
    speed: float = .05
    colors: dict[str, str] = {
        'background': 'black',
        'unsorted': 'grey',
        'sorted': 'limegreen',
        'highlight': 'yellow',
        'best': 'red',
    }

    # Set up window
    root: tk.Tk = tk.Tk()
    root.title('Visual Sort')
    root.config(bg=colors['background'])

    # Create bars using frames with different heights
    bars: list[tk.Frame] = create_bars(
        root, number_of_bars, width, max_height, colors['unsorted'], x_pad, y_pad
    )

    bubble_sort(root, bars, colors, x_pad, y_pad, speed)
    # selection_sort(root, bars, colors, x_pad, y_pad, speed)
    # insertion_sort(root, bars, colors, x_pad, y_pad, speed)

    root.mainloop()


def create_bars(
        wn: tk.Tk,
        number_of_bars: int,
        width: int,
        max_height: int,
        color: str,
        x_pad: int,
        y_pad: int,
) -> list[tk.Frame]:
    """Create bars using tk.Frames with different heights"""
    
    bars: list[tk.Frame] = []

    for _ in range(number_of_bars):
        height: int = randint(1, max_height)
        bar: tk.Frame = tk.Frame(wn, width=width, height=height, bg=color)
        bars.append(bar)

    pack_bars(bars, x_pad, y_pad)

    return bars


def bubble_sort(
    wn: tk.Tk,
    bars: list[tk.Frame],
    colors: dict[str, str],
    x_pad: int,
    y_pad: int,
    speed: float,
) -> None:
    """Sort bars by height using bubble sort algorithm"""

    for i in range(len(bars)):
        for j in range(len(bars) - 1 - i):
            if bars[j].winfo_reqheight() > bars[j + 1].winfo_reqheight():
                swap_bars(bars, j, j + 1)
            bars[j].config(bg=colors['unsorted']) #### Color
            bars[j + 1].config(bg=colors['highlight']) #### Color
            update_bars(wn, bars, x_pad, y_pad, speed)
        bars[-i - 1].config(bg=colors['sorted']) #### Color


def selection_sort(
        wn: tk.Tk,
        bars: list[tk.Frame],
        colors: dict[str, str],
        x_pad: int,
        y_pad: int,
        speed: float,
) -> None:
    """Sort bars by height using selection sort algorithm"""   
    
    for k in range(len(bars)):
        best = k
        for q in range(k, len(bars)):
            bars[q].config(bg=colors['highlight']) #### Color
            update_bars(wn, bars, x_pad, y_pad, speed)
            if bars[q].winfo_reqheight() <= bars[best].winfo_reqheight():
                bars[best].config(bg=colors['unsorted']) #### Color
                bars[q].config(bg=colors['best']) #### Color
                best = q
            else:
                bars[q].config(bg=colors['unsorted']) #### Color        
        swap_bars(bars, k, best)
        bars[k].config(bg=colors['sorted']) #### Color  
        update_bars(wn, bars, x_pad, y_pad, speed)  
    update_bars(wn, bars, x_pad, y_pad, speed)


def insertion_sort(
        wn: tk.Tk,
        bars: list[tk.Frame],
        colors: dict[str, str],
        x_pad: int,
        y_pad: int,
        speed: float,
) -> None:
    """Sort bars by height using insertion sort algorithm"""

    bars[0].config(bg=colors['sorted'])
    for j in range(1, len(bars)):
        k = j - 1
        bars[j].config(bg=colors['highlight'])
        while k >= 0 and bars[k].winfo_reqheight() > bars[k + 1].winfo_reqheight():
            swap_bars(bars, k, k + 1)
            k -= 1
            update_bars(wn, bars, x_pad, y_pad, speed)
        bars[k + 1].config(bg=colors['sorted'])
        update_bars(wn, bars, x_pad, y_pad, speed)


def update_bars(
    wn: tk.Tk,
    bars: list[tk.Frame],
    x_pad: int,
    y_pad: int,
    speed: float,
) -> None:
    """Update the bars."""

    for bar in bars:
        bar.pack_forget()
    pack_bars(bars, x_pad, y_pad)
    wn.update()
    sleep(speed)


def swap_bars(bars: list[tk.Frame], i: int, j: int) -> None:
    """Swap two bars"""

    bars[i], bars[j] = bars[j], bars[i]


def pack_bars(bars: list, x_pad: int, y_pad: int) -> None:
    """Pack the bars into the window."""

    for bar in bars:
        bar.pack(anchor='s', side = 'left', padx=x_pad, pady=y_pad)


main()