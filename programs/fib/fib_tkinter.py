import tkinter as tk
from time import sleep


def main():
    colors: list = ["red", "orange", "green", "blue", "darkblue", "purple"]
    line_color: str = "white"
    sides: str = ["top", "left", "bottom", "right"]

    wn: tk.Tk = tk.Tk()

    count: int = 12
    
    a: int = 0
    b: int = 1
    bar: tk.Frame = tk.Frame(wn, width=b, height=b, bg=colors[1])
    bar.pack(anchor="w")

    for i in range(count):
        c: int = a + b
        a = b
        b = c

        bar: tk.Frame = tk.Frame(wn, width=c, height=c, bg=colors[i % len(colors)])
        bar.pack(side=sides[i % len(sides)])
        sleep(0.5)
        wn.update()

    wn.mainloop()



main()