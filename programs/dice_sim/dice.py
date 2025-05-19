import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
import tkinter.ttk as ttk
import random as rm


class Die:
    """Die class with a number of sides and a roll method."""

    def __init__(self, sides: int) -> None:
        """Create a die with n-sides."""

        self.sides: int = sides

    def roll(self) -> int:
        """Roll the die and return result."""

        return rm.randint(1, self.sides)
    
    def __str__(self) -> str:
        """Return string for printing."""

        return f"A {self.sides}-sided die."
    

class DiceRoller:
    """Class to roll two dice and return the results."""

    def __init__(
        self,
        die1: ttk.Entry,
        die2: ttk.Entry,
        number_of_rolls: ttk.Entry,
        ax: plt.Axes,
        canvas: FigureCanvasTkAgg,
    ) -> None:
        """Create a DiceRoller with two dice."""

        self.die1: ttk.Entry = die1
        self.die2: ttk.Entry = die2
        self.number_of_rolls: ttk.Entry = number_of_rolls
        self.ax: plt.Axes = ax
        self.canvas: FigureCanvasTkAgg = canvas

    def roll_dice(self, number_of_rolls: int, die1: Die, die2: Die) -> dict:
        """Roll two dice and return the results."""

        results: list[int] = []

        for roll in range(number_of_rolls):
            result: int = die1.roll() + die2.roll()
            results.append(result)

        counts: dict = {}
        max_result: int = die1.sides + die2.sides

        for sum_value in range(2, max_result + 1):
            counts[sum_value] = results.count(sum_value)

        return counts


    def create_figure(
        self,
    ) -> None:
        """Create a figure and display it in the Tkinter window."""

        self.ax.clear()

        try:
            die1: Die = Die(int(self.die1.get()))
            die2: Die = Die(int(self.die2.get()))
            number_of_rolls: int = int(self.number_of_rolls.get())

            counts: dict = self.roll_dice(number_of_rolls, die1, die2)

            x_values: list[int] = list(counts.keys())
            y_values: list[int] = list(counts.values())
            
            self.ax.bar(x_values, y_values)        
            self.ax.set_title(
                f"D{die1.sides} and D{die2.sides} - {number_of_rolls} times"
            )

        except ValueError:
            self.ax.set_title("Invalid input")

        self.ax.set_xlabel("Sum of two dice")
        self.ax.set_ylabel("Frequency of sum")
        
        self.canvas.draw()


if __name__ == "__main__":
    print("This is a module...")