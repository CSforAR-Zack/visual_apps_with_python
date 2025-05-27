import tkinter as tk
from tkinter.font import Font

from mod import Stack


class Boxes:
    """A class that works with the boxes in the visualization."""

    def __init__(
        self,
        struct: Stack,
        frame: tk.Frame,
        entry: tk.Entry,
        output: tk.Label,
        wn: tk.Tk,
        font: Font
    ) -> None:
        """Create a Boxes instance for a data structure
        with a frame, text box, and output box"""

        self.struct: Stack[Box] = struct
        self.frame: tk.Frame = frame
        self.entry: tk.Entry = entry
        self.output: tk.Label = output
        self.wn: tk.Tk = wn
        self.font: Font = font
    
    def add_box(self) -> None:
        """Add a Box to the data structure"""

        value = self.entry.get()
        box: Box = Box(self.frame, value, self.font)

        self.struct.enter_value(box)
        self.output.config(text="")

        self.entry.delete(0, tk.END)        
        self.update_window()

    def get_box(self) -> None:
        """Remove a Box from the data structure and display it"""

        if self.struct.is_empty():
            self.output.config(text="Empty")
            return
        
        value: Box = self.struct.get_value()
        value.label.pack_forget()
        self.output.config(text=value)
        self.update_window()

    def peek_box(self) -> None:
        """Peek at the next Box from the data structure"""

        if self.struct.is_empty():
            self.output.config(text="Empty")
            return
        
        box: Box = self.struct.view_next()
        self.output.config(text=box.text)


    def update_window(self) -> None:
        """Update the canvas with the stack"""

        for box in self.struct.items:
            box.label.pack_forget()
        for box in self.struct.items:
            box.label.pack(
                expand=True, fill="both", padx=1, pady=1, anchor="n", side="top"
            )

        self.wn.update()
    

class Box:
    """A class that represents a box"""

    def __init__(
        self,
        parent: tk.Frame,
        text: str,
        font: Font,
        bg_color: str="black",
        fg_color: str="white"
    ) -> None:
        """Create a new box to represent a value in the data structure"""

        self.text: str = text
        self.label: tk.Label = tk.Label(
            parent,
            text=self.text, 
            font=font, 
            bg=bg_color, 
            fg=fg_color,
        )

    def __str__(self) -> str:
        return self.text