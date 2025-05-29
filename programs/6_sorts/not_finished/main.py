import tkinter as tk
from random import randint
from time import sleep


def main():
    # These are the variables we can change
    number_of_bars: int = 40
    width: int = 20
    max_height: int = 500
    spacing: int = 1
    speed: float = .5
    
    
    # Setup Window
    root: tk.Tk = tk.Tk()
    root.title("Visual Sort")
    root.configure(bg=Color.BACKGROUND)

    bars: Bars = Bars(root, spacing, speed)
    bars.create_bars(number_of_bars, width, max_height, Color.UNSORTED)

    # bars.bubble_sort()
    # bars.selection_sort()
    bars.insertion_sort()

    root.mainloop()


class Bars:
    """Bars class with al its of bars and methods to work on the bars."""
    
    def __init__(self, wn: tk.Tk, spacing: int, speed: float) -> None:
        """Create a bar manager."""

        self.wn: tk.Tk = wn
        self.spacing: int = spacing
        self.speed: float = speed

        self.bars: list = []

    def create_bars(
        self,
        number_of_bars: int,
        width: int,
        max_height: int,
        color: "Color",
    ) -> None:
        
        for _ in range(number_of_bars):
            height: int = randint(1, max_height)
            bar: Bar = Bar(height, width, color, self.wn)
            self.bars.append(bar)
        self.pack_bars()
        self.update_bars()

    def pack_bars(self) -> None:
        """Pack the bars into the window."""

        for bar in self.bars:
            bar.frame.pack(side="left", anchor="s", padx=self.spacing)

    def update_bars(self) -> None:
        """Update the bars in the window."""

        for bar in self.bars:
            bar.frame.pack_forget()
        self.pack_bars()
        self.wn.update()
        sleep(self.speed)

    def swap_bars(self, first: int, second: int) -> None:
        """Swap bars at first and second index."""

        self.bars[first], self.bars[second] = self.bars[second], self.bars[first]

    def bubble_sort(self) -> None:
        """Perform bubble sort on bars."""

        for i in range(len(self.bars)):
            for j in range(len(self.bars)-1-i):
                if self.bars[j] > self.bars[j+1]:
                    self.swap_bars(j, j+1)
                self.bars[j].color(Color.UNSORTED)
                self.bars[j+1].color(Color.HIGHLIGHT)
                self.update_bars()
            self.bars[-1-i].color(Color.SORTED)

    def selection_sort(self) -> None:
        """Perform selection sort on bars."""

        for spot in range(len(self.bars)):
            best = spot
            for looker in range(spot, len(self.bars)):
                self.update_bars()
                if self.bars[looker] < self.bars[best]:
                    best = looker
            self.swap_bars(spot, best)
            self.update_bars()
        self.update_bars()

    def insertion_sort(self) -> None:
        """Peform an insertion sort on bars."""

        for j in range(1, len(self.bars)):
            k: int = j - 1
            while k >= 0 and self.bars[k] > self.bars[k+1]:
                self.swap_bars(k, k+1)
                k -= 1
                self.update_bars()
            self.update_bars()
        self.update_bars()

class Bar:
    """Bar class with a height and color. Uses a Frame."""
    
    def __init__(
        self,
        height: int,
        width: int,
        color: "Color",
        wn: tk.Tk,
    ) -> None:
        
        self.height = height
        self.frame: tk.Frame = tk.Frame(wn, width=width, height=height, bg=color)

    def color(self, color: "Color") -> None:
        """Change the color of the bar."""

        self.frame.configure(bg=color)

    def __repr__(self) -> str:
        """How to show a bar."""

        return str(self.height)
    
    def __gt__(self, other: "Bar") -> bool:
        """Return true if greater than other, false otherwise."""

        return self.height > other.height
    
    def __lt__(self, other: "Bar") -> bool:
        """Return true if less than other, false otherwise."""

        return self.height < other.height


class Color:
    """A class to store colors."""

    BACKGROUND: str = "black"
    UNSORTED: str = "grey"
    SORTED: str = "limegreen"
    HIGHLIGHT: str = "yellow"
    BEST: str = "red"


if __name__ == "__main__":
    main()