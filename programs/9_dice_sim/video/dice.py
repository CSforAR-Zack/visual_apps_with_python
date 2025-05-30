import tkinter as tk
import random as rm

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Die:
    """Die class with a number of sides and a roll method."""

    def __init__(self, sides: int) -> None:
        """Create a die with n-sides."""

        self.sides: int = sides

    def roll(self) -> int:
        """Roll the die and return the result."""

        return rm.randint(1, self.sides)
    
    def __str__(self) -> str:
        """String representation."""

        return f"A {self.sides}-side die."


class DiceRoller:
    """Class to roll two dice and create a figure."""

    def __init__(
        self,
        die1: tk.Entry,
        die2: tk.Entry,
        number_of_rolls: tk.Entry,
        ax: plt.Axes,
        canvas: FigureCanvasTkAgg,
    ) -> None:
        """Create a dice roller."""

        self.die1: tk.Entry = die1
        self.die2: tk.Entry = die2
        self.number_of_rolls: tk.Entry = number_of_rolls
        self.ax: plt.Axes = ax
        self.canvas: FigureCanvasTkAgg = canvas
    
    def create_figure(self) -> None:
        """Create a figure and display it in the Tkinter window."""

        die1: Die = Die(int(self.die1.get()))
        die2: Die = Die(int(self.die2.get()))
        number_of_rolls: int = int(self.number_of_rolls.get())

        counts: dict = self.roll_dice(die1, die2, number_of_rolls)

        x_values: list = list(counts.keys())
        

    def roll_dice(
        self, die1: int, die2: int, number_of_rolls: int
    ) -> dict:
        """Roll the dice and return the results."""

        counts: dict = {}

        for roll in range(number_of_rolls):
            result: int = die1.roll() + die2.roll()
            counts[result] = counts.get(result, 0) + 1

        return counts


if __name__ == "__main__":
    die: Die = Die(6)
    print(die.roll())