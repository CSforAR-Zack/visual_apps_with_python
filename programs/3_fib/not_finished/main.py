import tkinter as tk
from time import sleep


def main():
    """Main function to run the Fibonacci program"""

    fib_linear()


# Fibonacci using linear pattern
def fib_linear() -> None:
    """Hardcoded colors of Fibonacci numbers using tkinter """

    colors: list = ["red", "orange", "green", "blue", "darkblue", "purple"]

    count: int = 12
    scale: int = 3

    root: tk.Tk = tk.Tk()
    root.title("Fibonacci")
    root.config(bg="black")

    for i in range(1, count + 1):
        fib_number: int = get_fib_iter(i)
        # fib_number: int = get_fib_recur(i)

        bar: tk.Frame = tk.Frame(
            root,
            width=fib_number*scale,
            height=fib_number*scale,
            bg=colors[i % len(colors)],
        )
        bar.pack(side="left", anchor="s")
        sleep(0.5)
        root.update()

    root.mainloop()


def get_fib_iter(num: int) -> int:
    """Iterative Fibonacci function"""
    
    if num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        a: int = 0
        b: int = 1

        for i in range(2, num + 1):
            c: int = a + b
            a = b
            b = c

        return c


def get_fib_recur(num: int) -> int:
    """Recursive Fibonacci function"""

    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return get_fib_recur(num - 1) + get_fib_recur(num - 2)