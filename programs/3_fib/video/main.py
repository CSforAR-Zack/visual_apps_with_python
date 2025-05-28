import tkinter as tk
from time import sleep


def main():
    fib_linear()
    # fib_braid()


def fib_linear() -> None:
    """A linear animation of the fib sequence."""

    colors: list = ["red", "orange", "green", "blue", "darkblue", "purple"]
    
    count: int = 12
    scale: int = 3

    root: tk.Tk = tk.Tk()
    root.title("Fibonacci Animation")
    root.config(bg="black")

    for i in range(1, count + 1):
        # fib_number: int = get_fib_iter(i)
        fib_number: int = get_fib_recur(i)
        
        bar: tk.Frame = tk.Frame(
            root,
            width=fib_number*scale,
            height=fib_number*scale,
            bg=colors[i%len(colors)]
        )
        bar.pack(side="left", anchor="s")
        sleep(.5)
        root.update()

    root.mainloop()


def get_fib_iter(num: int) -> int:
    """Iterative fibonacci function."""
    
    if num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        a: int = 0
        b: int = 1

        for _ in range(2, num):
            c: int = a + b
            a = b
            b = c
        
        return c
    

def get_fib_recur(num: int) -> int:
    """Recursive Fibonacci function."""

    if num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        return get_fib_recur(num-1) + get_fib_recur(num-2)


def fib_braid() -> None:
    """A braid animation of the fib sequence."""

    colors: list = ["red", "orange", "green", "blue", "darkblue", "purple"]
    
    count: int = 13
    scale: int = 3

    root: tk.Tk = tk.Tk()
    root.title("Fibonacci Animation")
    root.config(bg="black")

    for i in range(1, count + 1):
        if i == 1:
            continue

        # fib_number: int = get_fib_iter(i)
        fib_number: int = get_fib_recur(i)

        if i == 2:
            row, col = 0, 0
        else:
            row, col = get_row_col(i, fib_number, scale)
        
        bar: tk.Frame = tk.Frame(
            root,
            width=fib_number*scale,
            height=fib_number*scale,
            bg=colors[i%len(colors)]
        )
        bar.grid(
            row=row,
            column=col,
            columnspan=fib_number*scale,
            rowspan=fib_number*scale,
        )
        sleep(.5)
        root.update()

    root.mainloop()


def get_row_col(i: int, c: int, scale: int) -> tuple:
    """Get the row and column for the fib bar."""

    if i % 2 == 1:
        col = c * scale
        row = 0
    else:
        col = 0
        row = c * scale

    return row, col


if __name__ == "__main__":
    main()