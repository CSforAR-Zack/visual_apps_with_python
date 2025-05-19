import tkinter as tk
from time import sleep


def fib_linear():
    """Hardcoded colors of Fibonacci numbers using tkinter """

    colors: list = ["red", "orange", "green", "blue", "darkblue", "purple"]

    count: int = 12

    wn: tk.Tk = tk.Tk()
    wn.title("Fibonacci")
    wn.config(bg="black")
    
    a: int = 0
    b: int = 1

    for i in range(count):
        c: int = a + b
        a = b
        b = c

        bar: tk.Frame = tk.Frame(wn, width=c, height=c, bg=colors[i % len(colors)])
        bar.pack(side="left", anchor="s")
        sleep(0.5)
        wn.update()

    wn.mainloop()


def fib_linear_gradient():
    """Color gradient of Fibonacci numbers using tkinter """
    red: int = 0
    green: int = 255
    blue: int = 255
    count: int = 12

    wn: tk.Tk = tk.Tk()
    wn.title("Fibonacci")
    wn.config(bg="black")

    r_step: int = 0 // count
    g_step: int = 255 // count
    b_step: int = 255 // count
    
    a: int = 0
    b: int = 1

    for i in range(count):
        c: int = a + b
        a = b
        b = c

        red = (red + r_step) % 256
        green = (green + g_step) % 256
        blue = (blue + b_step) % 256

        bar: tk.Frame = tk.Frame(wn, width=c, height=c, bg=f"#{red:02x}{green:02x}{blue:02x}")
        bar.pack(side="left", anchor="s")
        sleep(0.5)
        wn.update()

    wn.mainloop()


def fib_braid():
    """Hardcoded colors of Fibonacci numbers using tkinter using a braid pattern"""

    colors: list = ["red", "orange", "green", "blue", "darkblue", "purple"]

    count: int = 15
    row: int = 0
    col: int = 0

    wn: tk.Tk = tk.Tk()
    wn.title("Fibonacci")
    wn.config(bg="black")
    
    a: int = 0
    b: int = 1

    square: tk.Frame = tk.Frame(wn, width=b, height=b, bg=colors[-1])
    square.grid(row=row, column=col)
    col += 1

    for i in range(count):
        c: int = a + b
        a = b
        b = c

        row, col = get_row_col(i, c)

        square: tk.Frame = tk.Frame(wn, width=c, height=c, bg=colors[i % len(colors)])
        square.grid(row=row, column=col, columnspan=c, rowspan=c)
        
        sleep(0.5)
        wn.update()

    wn.mainloop()


def fib_braid_gradient():
    """Color gradient of Fibonacci numbers using tkinter using a braid pattern"""

    red: int = 0
    green: int = 255
    blue: int = 255
    count: int = 12

    count: int = 15
    row: int = 0
    col: int = 0

    wn: tk.Tk = tk.Tk()
    wn.title("Fibonacci")
    wn.config(bg="black")

    r_step: int = 0 // count
    g_step: int = 255 // count
    b_step: int = 255 // count
    
    a: int = 0
    b: int = 1

    square: tk.Frame = tk.Frame(wn, width=b, height=b, bg=f"#{red:02x}{green:02x}{blue:02x}")
    square.grid(row=row, column=col)
    col += 1

    for i in range(count):
        c: int = a + b
        a = b
        b = c

        red = (red + r_step) % 256
        green = (green + g_step) % 256
        blue = (blue + b_step) % 256

        row, col = get_row_col(i, c)

        square: tk.Frame = tk.Frame(wn, width=c, height=c, bg=f"#{red:02x}{green:02x}{blue:02x}")
        square.grid(row=row, column=col, columnspan=c, rowspan=c)
        sleep(0.5)
        wn.update()

    wn.mainloop()


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
    fib_linear()
    # fib_linear_gradient()
    # fib_braid()
    # fib_braid_gradient()