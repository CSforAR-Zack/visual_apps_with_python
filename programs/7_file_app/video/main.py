import tkinter as tk
from tkinter.font import Font
from tkinter import filedialog, messagebox, simpledialog
import os
import shutil

from send2trash import send2trash


def main():
    # Custom Variables
    padding: int = 20
    button_size_x: int = 40
    button_size_y: int = 3

    # Window setup
    root: tk.Tk = tk.Tk()
    root.title("File Manager")

    # Fonts
    font: Font = Font(size=30)

    # Main Frame
    main_frame: tk.Frame = tk.Frame(
        root,
        bg=Color.background_color,
        padx=padding,
        pady=padding,
    )
    main_frame.pack(fill="both", expand=True)
    
    # Label
    label: tk.Label = tk.Label(
        main_frame,
        text="File Manager",
        bg=Color.background_color,
        fg=Color.text_color,
        font=font,
    )
    label.pack()

    # Button
    copy_button: HoverButton = HoverButton(
        master=main_frame,
        text="Copy File",
        command=copy_file,
        width=button_size_x,
        height=button_size_y,
    )
    copy_button.pack()

    move_button: HoverButton = HoverButton(
        master=main_frame,
        text="Move File",
        command=move_file,
        width=button_size_x,
        height=button_size_y,
    )
    move_button.pack()
    
    rename_button: HoverButton = HoverButton(
        master=main_frame,
        text="Rename File",
        command=rename_file,
        width=button_size_x,
        height=button_size_y,
    )
    rename_button.pack()
    
    delete_button: HoverButton = HoverButton(
        master=main_frame,
        text="Delete File",
        command=delete_file,
        width=button_size_x,
        height=button_size_y,
    )
    delete_button.pack()

    # Mainloop
    root.mainloop()


# Button Command Functions
def copy_file() -> None:
    """Make a copy of a file."""

    file_to_copy: str = filedialog.askopenfilename()
    base_name: str = os.path.basename(file_to_copy)
    renamed_base_name: str = f"copy_of_{base_name}"
    destination_dir: str = filedialog.askdirectory()
    new_file: str = os.path.join(destination_dir, renamed_base_name)
    shutil.copy(file_to_copy, new_file)
    messagebox.showinfo("File Copied", f"File copied to {destination_dir}")


def move_file() -> None:
    """Move a file to a new directory"""

    file_to_move: str = filedialog.askopenfilename()
    file_dir: str = os.path.dirname(file_to_move)
    destination_dir: str = filedialog.askdirectory()
    if file_dir == destination_dir:
        messagebox.showerror("Error", "Cannot move file to the same directory.")
        return
    shutil.move(file_to_move, destination_dir)
    messagebox.showinfo("File Moved", f"File moved to {destination_dir}")


def rename_file() -> None:
    """Rename a file to a different name."""

    file_to_rename: str = filedialog.askopenfilename()
    old_base_name: str = os.path.basename(file_to_rename)
    base_dir: str = os.path.dirname(file_to_rename)
    new_file_name: str = simpledialog.askstring("Rename File", "Enter a new file name.")
    if old_base_name == new_file_name:
        messagebox.showerror("Error", "Cannot rename file to the same name.")
        return
    new_file_path: str = os.path.join(base_dir, new_file_name)
    os.rename(file_to_rename, new_file_path)
    messagebox.showinfo("File Renamed", f"File renamed to {new_file_path}")


def delete_file() -> None:
    """Delete a file."""

    file_to_delete: str = filedialog.askopenfilename()
    confirm: bool = messagebox.askyesno("Delete File", "Are you sure you want to delete this file?")
    if not confirm:
        messagebox.showinfo("File Not Deleted", "File not deleted!")
        return
    file_to_delete: str = os.path.abspath(file_to_delete)
    send2trash(file_to_delete)
    messagebox.showinfo("File Deleted", "File sent to trash.")


# CustomButton
class HoverButton(tk.Button):
    """A class to create a button with a hover effect."""

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

        self.config(bg=Color.base_color, fg=Color.button_text_base_color)
        self.bind("<Enter>", self.on_hover)
        self.bind("<Leave>", self.off_hover)

    def on_hover(self, event: tk.Event) -> None:
        """Change the color of the button when mouse is over it."""

        event.widget.config(
            bg=Color.hover_color,
            fg=Color.button_text_hover_color,
        )

    def off_hover(self, event: tk.Event) -> None:
        """Change the color of the button when mouse leaves it."""

        event.widget.config(
            bg=Color.base_color,
            fg=Color.button_text_base_color,
        )


# Colors
class Color:
    """A class to store colors for the GUI."""

    background_color: str = "black"
    text_color: str = "white"

    base_color: str = "grey"
    hover_color: str = "cyan"
    button_text_base_color: str = "white"
    button_text_hover_color: str = "black"


if __name__ == "__main__":
    main()