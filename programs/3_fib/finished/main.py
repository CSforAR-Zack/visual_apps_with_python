import tkinter as tk
from time import sleep


def main():
    """Main function to run the Fibonacci program"""

    # fib_linear()
    # fib_recursive()
    fib_braid()


# Fibonacci using linear pattern
def fib_linear():
    """Hardcoded colors of Fibonacci numbers using tkinter """

    colors: list = ["red", "orange", "green", "blue", "darkblue", "purple"]

    count: int = 12

    root: tk.Tk = tk.Tk()
    root.title("Fibonacci")
    root.config(bg="black")
    
    a: int = 0
    b: int = 1

    for i in range(count):
        c: int = a + b
        a = b
        b = c

        bar: tk.Frame = tk.Frame(root, width=c, height=c, bg=colors[i % len(colors)])
        bar.pack(side="left", anchor="s")
        sleep(0.5)
        root.update()

    root.mainloop()


# Fibonacci using recursion
def fib_recursive() -> None:
    """Hardcoded colors of Fibonacci numbers using tkinter using recursion"""

    colors: list = ["red", "orange", "green", "blue", "darkblue", "purple"]

    count: int = 12

    wn: tk.Tk = tk.Tk()
    wn.title("Fibonacci")
    wn.config(bg="black")

    for i in range(count):
        c: int = get_fib(i)

        if c == 0:
            continue
        
        square: tk.Frame = tk.Frame(wn, width=c, height=c, bg=colors[i % len(colors)])
        square.pack(side="left", anchor="s")
        
        sleep(0.5)
        wn.update()

    wn.mainloop()


def get_fib(num: int) -> int:
    """Recursive Fibonacci function"""

    if num <= 0:
        return 0
    elif num == 1:
        return 1
    else:
        return get_fib(num - 1) + get_fib(num - 2)


def fib_braid():
    """Hardcoded colors of Fibonacci numbers using tkinter using a braid pattern"""

    colors: list = ["red", "orange", "green", "blue", "darkblue", "purple"]

    count: int = 12
    row: int = 0
    col: int = 0

    root: tk.Tk = tk.Tk()
    root.title("Fibonacci")
    root.config(bg="black")
    
    a: int = 0
    b: int = 1

    for i in range(count):
        c: int = a + b
        a = b
        b = c

        row, col = get_row_col(i, c)

        square: tk.Frame = tk.Frame(root, width=c, height=c, bg=colors[i % len(colors)])
        square.grid(row=row, column=col, columnspan=c, rowspan=c)
        
        sleep(0.5)
        root.update()

    root.mainloop()


def get_row_col(i: int, c: int) -> tuple:
    """Get the row and column for the Fibonacci square"""

    if i % 2 == 0:
        col = c
        row = 0
    else:
        row = c
        col = 0

    return row,col


if __name__ == "__main__":
    main()