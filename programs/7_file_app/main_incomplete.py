import tkinter as tk
from tkinter.font import Font


def main():
    # Custom Variables
    padding: int = 20
    button_size_x: int = 40
    button_size_y: int = 3

    # Window Setup
    wn: tk.Tk = tk.Tk()
    wn.title("File Manager")

    # Fonts
    label_font: Font = Font(size=30)

    frame: tk.Frame = tk.Frame(
        wn,
        bg=Colors.background_color,
        padx=padding,
        pady=padding,
    )
    frame.pack()

    # Label
    label: tk.Label = tk.Label(
        frame,
        text="File Manager",
        font=label_font,
        bg=Colors.background_color,
        fg=Colors.text_color,
    )
    label.pack()

    # Buttons
    copy_button: HoverButton = HoverButton(
        master=frame,
        text="Copy File",
        command=copy_file,
        width=button_size_x,
        height=button_size_y,
    )
    copy_button.pack()

    
    move_button: HoverButton = HoverButton(
        master=frame,
        text="Move File",
        command=move_file,
        width=button_size_x,
        height=button_size_y,
    )
    move_button.pack()

    
    rename_button: HoverButton = HoverButton(
        master=frame,
        text="Rename File",
        command=rename_file,
        width=button_size_x,
        height=button_size_y,
    )
    rename_button.pack()

    
    delete_button: HoverButton = HoverButton(
        master=frame,
        text="Delete File",
        command=delete_file,
        width=button_size_x,
        height=button_size_y,
    )
    delete_button.pack()

    # Mainloop
    wn.mainloop()


# Button Functions: Commands
def copy_file() -> None:
    """Make a copy of a file."""

    print("Copying File...") # REMOVE THIS

    # Ask user for file to copy
    # Get the base name of the file and rename it to "copy_of_{base_name}"
    # Ask user for destination directory
    # Create a new file with the renamed base name in the destination directory
    # Show a message box that the file has been copied


def move_file() -> None:
    """Move a file to a new directory."""

    print("Moving File...") # REMOVE THIS

    # Ask user for file to move
    # Ask user for destination directory
    # Check if the file is being moved to the same directory
    # If the file is being moved to the same directory, show an error message and exit the function
    # Else, move the file to the destination directory
    # Show a message box that the file has been moved


def rename_file() -> None:
    """Rename a file."""

    print("Renaming File...") # REMOVE THIS

    # Ask user for file to rename
    # Ask user for new file name
    # Check if the new file name is the same as the old file name
    # If the new file name is the same as the old file name, show an error message and exit the function
    # Else, rename the file and place it into the same directory as the original
    # Show a message box that the file has been renamed


def delete_file() -> None:
    """Delete a file."""

    print("Deleting File...") # REMOVE THIS

    # Ask user for file to delete
    # Confirm with the user if they want to delete the file with a pop-up message
    # If the user confirms, delete the file else exit the function    
    # Use send2trash to send the file to the trash
    # send2trash(file) only works with paths that have backslashes on Windows
    # hint: use os.path.abspath to get the absolute path of the file to work with send2trash
    # Show a message box that the file has been deleted


# CustomButton
class HoverButton(tk.Button):
    """A class to create a button with hover effects."""

    def __init__(self, **kw_args) -> None:
        super().__init__(**kw_args)

        self.config(bg=Colors.base_color, fg=Colors.button_text_base_color)
        self.bind("<Enter>", self.on_hover)
        self.bind("<Leave>", self.off_hover)

    def on_hover(self, event: tk.Event) -> None:
        """Change the color of the button when mouse is over it."""

        event.widget.config(
            bg=Colors.hover_color,
            fg=Colors.button_text_hover_color,
        )

    def off_hover(self, event: tk.Event) -> None:
        """Change the color of the button when mouse leaves it."""

        event.widget.config(
            bg=Colors.base_color,
            fg=Colors.button_text_base_color,
        )


# Color
class Colors:
    """A class to store colors for the GUI."""

    background_color: str = "black"
    text_color: str = "white"

    base_color: str = "gray"
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