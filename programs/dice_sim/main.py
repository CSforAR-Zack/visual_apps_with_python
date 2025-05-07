import pygal as pg
from pygal.style import Style

from dice import Die


def main():
    # Create dice
    die1: Die = Die(20)
    die2: Die = Die(20)

    # Simulate rolling and add the results.
    number_of_rolls: int = 100000

    results: list[int] = []

    for roll in range(number_of_rolls):
        result: int = die1.roll() + die2.roll()
        results.append(result)

    # Analyze the results from the rolls
    counts: dict = {}
    max_result: int = die1.sides + die2.sides

    for sum_value in range(2, max_result + 1):
        counts[sum_value] = results.count(sum_value)

    # Create a graph to show the results.
    # Change the colors of the graph
    # Can't use my colors
    my_style: Style = Style(
        colors=("cyan",),
        background="black",
        plot_background="black",
        foreground="white",
        foreground_strong="white",
        guide_stroke_color="grey",
        major_guide_stroke_color="grey",
    )

    graph: pg.Bar = pg.Bar(style=my_style)
    graph.title = "Dice Roll Results"

    graph.x_title = "Results"
    graph.x_labels = counts.keys()

    graph.y_title = "Frequency"
    graph.add("Sum", counts.values())

    graph.render_to_file("dice_sim.svg")


if __name__ == "__main__":
    main()