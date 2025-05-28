import tkinter as tk
from tkinter.font import Font


def main():
    root: tk.Tk = tk.Tk()
    root.title("Calculator")

    font_style: Font = Font(family="Courier", size=40)
    font_style_large: Font = Font(family="Courier", size=60)

    exp_entry: tk.Entry = tk.Entry(root, font=font_style)
    eq_label: tk.Label = tk.Label(root, text=" = ", font=font_style)
    result_label: tk.Label = tk.Label(root, text="0", font=font_style_large)
    calc_button: tk.Button = tk.Button(
        root,
        text="Calculate",
        font=font_style,
        command=lambda: calculate(exp_entry, result_label),
    )

    exp_entry.grid(column=0, row=0)
    eq_label.grid(column=1, row=0)
    result_label.grid(row=1, columnspan=3)
    calc_button.grid(row=2, columnspan=3)

    root.mainloop()


def calculate(exp_entry: tk.Entry, result_label: tk.Label) -> None:
    """Calculate the expression."""

    expression: str = exp_entry.get()
    result: str = eval(expression)
    result_label["text"] = result


if __name__ == "__main__":
    main()