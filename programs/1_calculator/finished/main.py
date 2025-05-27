import tkinter as tk
from tkinter.font import Font


def main():
    root: tk.Tk = tk.Tk()
    root.title("Calculator")

    font_style: Font = Font(family="Courier", size=20)
    font_style_large: Font = Font(family="Courier", size=50)

    exp_entry: tk.Entry = tk.Entry(root, font=font_style)
    eq_label: tk.Label = tk.Label(root, text=" = ", font=font_style)
    result_label: tk.Label = tk.Label(root, text="0", font=font_style_large)
    calc_button: tk.Button = tk.Button(
        root, 
        text="Calculate", 
        font=font_style,
        command=lambda : calculate(exp_entry, result_label),
    )

    exp_entry.grid(row=0, column=0)
    eq_label.grid(row=0, column=1)
    result_label.grid(row=1)
    calc_button.grid(row=2)

    root.mainloop()


def calculate(exp_entry: tk.Entry, label_result: tk.Label) -> None:
    expression: str = exp_entry.get()
    result: str = eval(expression)
    label_result["text"] = result


if __name__ == "__main__":
    main()