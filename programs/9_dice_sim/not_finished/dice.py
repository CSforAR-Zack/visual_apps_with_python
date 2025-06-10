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
        """return string for printing."""

        return f"A {self.sides}-sided die."


if __name__ == "__main__":
    die1 = Die(6)
    print(die1)
    print(die1.roll())