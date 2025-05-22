import tkinter as tk

from random import randint
from time import sleep


def main():
    # This are the variables you can change
    number_of_bars: int = 40
    width: int = 10
    max_height: int = 500
    spacing: int = 1
    speed: float = .05

    # Set up window
    root: tk.Tk = tk.Tk()
    root.title('Visual Sort')
    root.config(bg=Color.BACKGROUND)

    bars: Bars = Bars(root, spacing, speed)
    bars.create_bars(number_of_bars, width, max_height, Color.UNSORTED)

    # bars.bubble_sort()
    # bars.selection_sort()
    bars.insertion_sort()

    root.mainloop()


class Bars:
    """Bars class with a list of bars and methods to word on the bars."""

    def __init__(self, wn: tk.Tk, spacing: int, speed: float) -> None:
        """Create a new set of bars."""
        self.wn: tk.Tk = wn
        self.spacing: int = spacing
        self.speed: float = speed
        self.bars: list[Bar] = []

    def create_bars(
        self,
        number_of_bars: int,
        width: int,
        max_height: int,
        color: str,
    ) -> None:
        """Create bars using tk.Frames with different heights"""

        for _ in range(number_of_bars):
            height: int = randint(1, max_height)
            bar: Bar = Bar(height, width, color, self.wn)
            self.bars.append(bar)
        self.pack_bars()

    def update_bars(self) -> None:
        """Update the bars in the window."""

        for bar in self.bars:
            bar.frame.pack_forget()
        self.pack_bars()
        self.wn.update()
        sleep(self.speed)

    def pack_bars(self) -> None:
        """Pack the bars into the window."""

        for bar in self.bars:
            bar.frame.pack(anchor="s", side = "left", padx=self.spacing, pady=self.spacing)

    def swap_bars(self, first: int, second: int) -> None:
        """Swap first with second in self.bars"""

        self.bars[first], self.bars[second] = self.bars[second], self.bars[first]

    def bubble_sort(self) -> None:
        """Sort bars by height using bubble sort algorithm."""

        for i in range(len(self.bars)):
            for j in range(len(self.bars) - 1 - i):
                if self.bars[j] > self.bars[j + 1]:
                    self.swap_bars(j, j+1)
                self.bars[j].color(Color.UNSORTED)
                self.bars[j + 1].color(Color.HIGHLIGHT)
                self.update_bars()
            self.bars[-i - 1].color(Color.SORTED)

    def selection_sort(self) -> None:
        """Sort the bars using the insertion sort algorithm."""

        for k in range((len(self.bars))):
            best = k
            for q in range(k, len(self.bars)):
                self.bars[q].color(Color.HIGHLIGHT)
                self.update_bars()
                if self.bars[q] < self.bars[best]:
                    self.bars[best].color(Color.UNSORTED)
                    self.bars[q].color(Color.BEST)
                    best = q
                else:
                    self.bars[q].color(Color.UNSORTED)
            self.swap_bars(k, best)
            self.bars[k].color(Color.SORTED)
            self.update_bars()
        self.update_bars()

    def insertion_sort(self) -> None:
        """Sort the bars using the insertion sort algorithm."""

        self.bars[0].color(Color.SORTED)
        for j in range(1, len(self.bars)):
            k: int = j - 1
            self.bars[j].color(Color.HIGHLIGHT)
            while k >= 0 and self.bars[k] > self.bars[k+1]:
                self.swap_bars(k, k+1)
                k -= 1
                self.update_bars()
            self.bars[k+1].color(Color.SORTED)
            self.update_bars()


class Bar:
    """Bar class with a height and color."""

    def __init__(self, height: int, width: int, color: str, wn: tk.Tk) -> None:
        """Create a bar."""

        self.height: int = height
        self.frame: tk.Frame = tk.Frame(wn, width=width, height=height, bg=color)

    def color(self, color: str) -> None:
        """Change the color of a bar."""

        self.frame.config(bg=color)

    def __gt__(self, other: object) -> bool:
        """Return true if greater than other, false otherwise."""

        return self.height > other.height
    
    def __lt__(self, other: object) -> bool:
        """Return true if less than other, false otherwise."""

        return self.height < other.height
    
    def __le__(self, other: object) -> bool:
        """Return true if less than or equal to other, false otherwise."""

        return self.height <= other.height


# Color: Change to your colors, don't use mine!
class Color:
    """A class to store colors."""
    
    BACKGROUND: str = "black"
    UNSORTED: str = 'grey'
    SORTED: str = 'limegreen'
    HIGHLIGHT: str = 'yellow'
    BEST: str = 'red'


if __name__ == "__main__":
    main()