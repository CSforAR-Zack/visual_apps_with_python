import tkinter as tk
from tkinter.font import Font


def main():
    wn: tk.Tk = tk.Tk()
    wn.title("Calculator")

    font_style: Font = Font(family="Courier", size=20)
    font_style_large: Font = Font(family="Courier", size=50)

    entry_exp: tk.Entry = tk.Entry(wn, font=font_style)
    label_eq: tk.Label = tk.Label(wn, text=" = ", font=font_style)
    label_result: tk.Label = tk.Label(wn, text="0", font=font_style_large)
    button_calc: tk.Button = tk.Button(
        wn, 
        text="Calculate", 
        font=font_style,
        command=lambda : calculate(entry_exp, label_result),
    )

    entry_exp.grid(row=0, column=0)
    label_eq.grid(row=0, column=1)
    label_result.grid(row=1)
    button_calc.grid(row=2)

    wn.mainloop()


def calculate(entry_exp: tk.Entry, label_result: tk.Label) -> None:
    expression: str = entry_exp.get()
    result: str = eval(expression)
    label_result["text"] = result


main()