import tkinter as tk
from tkinter.font import Font


def main():
    wn: tk.Tk = tk.Tk()
    wn.title("Base Converter")
    wn.configure(bg=Colors.background)
    font_style: Font = Font(family="Consolas", size=20)

    number_entry: tk.Entry = tk.Entry(
        wn,
        font=font_style,
        bg=Colors.forground,
        fg=Colors.text,
    )

    choices: tuple = ("Binary", "Octal", "Decimal", "Hexidecimal")
    base_input_sbox: tk.Spinbox = tk.Spinbox(
        wn,
        font=font_style,
        values=choices,
        state="readonly",
        readonlybackground=Colors.forground,
        buttonbackground=Colors.forground,
        fg=Colors.text,
    )

    base_output_sbox: tk.Spinbox = tk.Spinbox(
        wn,
        font=font_style,
        values=choices,
        state="readonly",
        readonlybackground=Colors.forground,
        buttonbackground=Colors.forground,
        fg=Colors.text,
    )

    result_label: tk.Label = tk.Label(
        wn,
        text="-",
        font=font_style,
        bg=Colors.background,
        fg=Colors.text,
    )

    command_center: CommandCenter = CommandCenter(
        number_entry,
        base_input_sbox,
        base_output_sbox,
        result_label,
    )

    convert_button: tk.Button = tk.Button(
        wn,
        text="Convert",
        command=command_center.convert,
        font=font_style,
        bg=Colors.background,
        fg=Colors.text,
        activebackground=Colors.text,
        activeforeground=Colors.background,
    )

    logo: tk.PhotoImage = tk.PhotoImage(master=wn, file="base_converter/logo.png")
    logo = logo.subsample(2)
    logo_label: tk.Label = tk.Label(wn, image=logo, bg=Colors.background)

    # Packing area
    px: int = 10
    py: int = 5
    number_entry.pack(fill="x", padx=px, pady=py)
    base_input_sbox.pack(fill="x", padx=px, pady=py)
    base_output_sbox.pack(fill="x", padx=px, pady=py)
    convert_button.pack(fill="x", padx=px, pady=py)
    result_label.pack(fill="x", padx=px, pady=py)
    logo_label.pack(fill="x", padx=px, pady=py)

    wn.mainloop()


class CommandCenter:
    """Handles button commands."""

    def __init__(
        self,
        entry: tk.Entry,
        input_base: tk.Spinbox,
        output_base: tk.Spinbox,
        output: tk.Label,
    ) -> None:
        """Setup a CommandCenter."""

        self.entry: tk.Entry = entry
        self.input_base: tk.Spinbox = input_base
        self.output_base: tk.Spinbox = output_base
        self.output: tk.Label = output

    def convert(self) -> None:
        """Convert input number from input base to output base and display."""

        number_input: str = self.entry.get()
        input_base: str = self.input_base.get()
        output_base: str = self.output_base.get()

        # Convert input base to decimal number
        try:
            if input_base == "Binary":
                number: int = int(number_input, 2)
            elif input_base == "Octal":
                number: int = int(number_input, 8)
            elif input_base == "Decimal":
                number: int = int(number_input, 10)
            elif input_base == "Hexidecimal":
                number: int = int(number_input, 16)
        except ValueError:
            self.output.config(text="Invalid Number")
            return

        # Convert decimal number to output base
        if output_base == "Binary":
            number_output: str = bin(number)[2:]
        elif output_base == "Octal":
            number_output: str = oct(number)[2:]
        elif output_base == "Decimal":
            number_output: str = str(number)
        elif output_base == "Hexidecimal":
            number_output: str = hex(number)[2:]

        self.output.config(text=number_output)


class Colors:
    """Color class for storing the colors."""

    background: str = "#222222"
    forground: str = "#444444"
    text: str = "#f59342"


if __name__ == "__main__":
    main()