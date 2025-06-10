import tkinter as tk

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from dice import Die


class Color:
    """A class to hold color codes for the simulation."""

    color1: "Color" = "#00FFFF"
    color2: "Color" = "#00AAAA"
    color3: "Color" = "#005555"
    color4: "Color" = "#000000"


class Simulator:
    """Class to roll two dice n times and
    create a figure from the results.
    """

    def __init__(
        self,
        die1: tk.Entry,
        die2: tk.Entry,
        number_of_rolls: tk.Entry,
        ax: plt.Axes,
        canvas: FigureCanvasTkAgg,
    ) -> None:
        """Create a Simulator for running the simulation."""

        self.die1: tk.Entry = die1
        self.die2: tk.Entry = die2
        self.number_of_rolls: tk.Entry = number_of_rolls
        self.ax: plt.Axes = ax
        self.canvas: FigureCanvasTkAgg = canvas

    def create_figure(self) -> None:
        """Create a figure and display it by running simulation."""

        self.ax.clear()

        try:
            die1: Die = Die(int(self.die1.get()))
            die2: Die = Die(int(self.die2.get()))
            number_of_rolls: int = int(self.number_of_rolls.get())

            counts: dict = self.roll_dice(number_of_rolls, die1, die2)
            
            x_values: list = list(counts.keys())
            y_values: list = list(counts.values())
            self.ax.bar(x_values, y_values, color=Color.color1, edgecolor=Color.color2)
            self.ax.set_title(
                f"D{die1.sides} and D{die2.sides} - {number_of_rolls} Times", fontsize=16, color=Color.color1
            )

        except ValueError:
            self.ax.set_title("Invalid Input", fontsize=16, color=Color.color1)

        self.ax.set_xlabel("Sum of Two Dice", fontsize=14, color=Color.color1)
        self.ax.set_ylabel("Frequency of Sum", fontsize=14, color=Color.color1)
        self.canvas.draw()

    def roll_dice(self, number_of_rolls: int, die1: Die, die2: Die) -> dict:
        """Roll two dice n times and return the results."""

        results: list = []

        for roll in range(number_of_rolls):
            result: int = die1.roll() + die2.roll()
            results.append(result)
        
        counts: dict = {}
        max_result: int = die1.sides + die2.sides

        for sum_value in range(2, max_result + 1):
            counts[sum_value] = results.count(sum_value)

        return counts