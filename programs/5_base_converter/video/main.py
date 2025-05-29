import tkinter as tk
from tkinter.font import Font


def main():
    root: tk.Tk = tk.Tk()
    root.title("Base Converter")
    root.configure(bg=Colors.COLOR1)
    font_style: Font = Font(family="Consolas", size=30)

    number_entry: tk.Entry = tk.Entry(
        root,
        font=font_style,
        bg=Colors.COLOR2,
        fg=Colors.TEXT,
        insertbackground=Colors.TEXT,
    )

    choices: tuple = ("Binary", "Octal", "Decimal", "Hexadecimal")
    base_input_sbox: tk.Spinbox = tk.Spinbox(
        root,
        font=font_style,
        values=choices,
        state="readonly",
        readonlybackground=Colors.COLOR2,
        buttonbackground=Colors.COLOR2,
        fg=Colors.TEXT,
    )

    base_output_sbox: tk.Spinbox = tk.Spinbox(
        root,
        font=font_style,
        values=choices,
        state="readonly",
        readonlybackground=Colors.COLOR2,
        buttonbackground=Colors.COLOR2,
        fg=Colors.TEXT,
    )

    result_label: tk.Label = tk.Label(
        root,
        text="-",
        font=font_style,
        bg=Colors.COLOR1,
        fg=Colors.TEXT,
    )

    command_center: CommandCenter = CommandCenter(
        number_entry,
        base_input_sbox,
        base_output_sbox,
        result_label,
    )

    convert_button: tk.Button = tk.Button(
        root,
        text="Convert",
        command=command_center.convert,
        font=font_style,
        bg=Colors.COLOR1,
        fg=Colors.TEXT,
        activebackground=Colors.TEXT,
        activeforeground=Colors.COLOR1,
    )

    logo: tk.PhotoImage = tk.PhotoImage(master=root, file="logo.png")
    logo = logo.subsample(2)
    logo_label: tk.Label = tk.Label(root, image=logo, bg=Colors.COLOR1)

    px: int = 10
    py: int = 5
    number_entry.pack(fill="x", padx=10, pady=5)
    base_input_sbox.pack(fill="x", padx=10, pady=5)
    base_output_sbox.pack(fill="x", padx=10, pady=5)
    convert_button.pack(fill="x", padx=10, pady=5)
    result_label.pack(fill="x", padx=10, pady=5)
    logo_label.pack()

    root.mainloop()


class CommandCenter:
    """Handles button commands."""

    def __init__(
        self,
        entry: tk.Entry,
        input_base: tk.Spinbox,
        output_base: tk.Spinbox,
        output: tk.Label,
    ) -> None:
        """Setup the CommandCenter."""

        self.entry: tk.Entry = entry
        self.input_base: tk.Spinbox = input_base
        self.output_base: tk.Spinbox = output_base
        self.output: tk.Label = output

    def convert(self) -> None:
        """Convert input number from input base to output base and display."""

        number_input: str = self.entry.get()
        input_base: str = self.input_base.get()
        output_base: str = self.output_base.get()

        try:
            if input_base == "Binary":
                number: int = int(number_input, 2)
            elif input_base == "Octal":
                number: int = int(number_input, 8)
            elif input_base == "Decimal":
                number: int = int(number_input, 10)
            elif input_base == "Hexadecimal":
                number: int = int(number_input, 16)
        except ValueError:
            self.output.configure(text="Invalid Number")
            return

        if output_base == "Binary":
            number_output: str = bin(number)[2:]
        elif output_base == "Octal":
            number_output: str = oct(number)[2:]
        elif output_base == "Decimal":
            number_output: str = str(number)
        elif output_base == "Hexadecimal":
            number_output: str = hex(number)[2:].upper()

        self.output.configure(text=number_output)


class Colors:
    """Color class for storing the colors."""

    COLOR1: str = "#222222"
    COLOR2: str = "#444444"
    TEXT: str = "#f59342"


if __name__ == "__main__":
    main()