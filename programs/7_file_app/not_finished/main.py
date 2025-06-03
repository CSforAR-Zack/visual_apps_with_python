import tkinter as tk
from tkinter.font import Font
from tkinter import filedialog, messagebox, simpledialog
import os
import shutil


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

    print("Copying file...") # REMOVE THIS

    # Ask user for file to copy
    # Get the base name of the file and rename it to "copy_of_{base_name}"
    # Ask user for destination directory
    # Create a new file with the renamed base name in the destination directory
    # Show a message box that the file has been copied


def move_file() -> None:
    """Move a file to a new directory"""

    print("Moving file...") # REMOVE THIS

    # Ask user for file to move
    # Ask user for destination directory
    # Check if the file is being moved to the same directory
    # If the file is being moved to the same directory, show an error message and exit the function
    # Else, move the file to the destination directory
    # Show a message box that the file has been moved


def rename_file() -> None:
    """Rename a file to a different name."""

    print("Renaming file...") # REMOVE THIS

    # Ask user for file to rename
    # Ask user for new file name
    # Check if the new file name is the same as the old file name
    # If the new file name is the same as the old file name, show an error message and exit the function
    # Else, rename the file and place it into the same directory as the original
    # Show a message box that the file has been renamed


def delete_file() -> None:
    """Delete a file."""

    print("Deleting file...") # REMOVE THIS

    # Ask user for file to delete
    # Confirm with the user if they want to delete the file with a pop-up message
    # If the user confirms, delete the file else exit the function    
    # Use send2trash to send the file to the trash
    # send2trash(file) only works with paths that have backslashes on Windows
    # hint: use os.path.abspath to get the absolute path of the file to work with send2trash
    # Show a message box that the file has been deleted



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

# DON'T ADD THESE COMMENTS
# Functions to consider when implementing the copy_file, move_file, rename_file, and delete_file functions
#   os.rename(file_to_rename, new_file_path)
#   shutil.copy(file_to_copy, new_file_path)
#   shutil.move(file_to_move, new_file_path)
#   send2trash(file_to_delete)
#   os.path.abspath(file_to_delete)
#   tk.messagebox.showinfo(title, message)
#   tk.messagebox.askyesno(title, message)
#   filedialog.askopenfilename()
#   filedialog.askdirectory()
#   os.path.basename(file_path)
#   os.path.dirname(file_path)
#   os.path.join(directory, file_name)
#   os.path.exists(file_path)
#   os.path.isdir(directory)
#   os.path.isfile(file_path)
#   os.path.split(file_path)