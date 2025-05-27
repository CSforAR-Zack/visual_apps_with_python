import tkinter as tk
from tkinter.font import Font
import os
import shutil
from tkinter import filedialog, messagebox, simpledialog

from send2trash import send2trash


def main():
    # Custom Variables
    padding: int = 20
    button_size_x: int = 40
    button_size_y: int = 3

    # Window Setup
    root: tk.Tk = tk.Tk()
    root.title("File Manager")

    # Fonts
    label_font: Font = Font(size=30)

    main_frame: tk.Frame = tk.Frame(
        root,
        bg=Colors.background_color,
        padx=padding,
        pady=padding,
    )
    main_frame.pack()

    # Label
    title_label: tk.Label = tk.Label(
        main_frame,
        text="File Manager",
        font=label_font,
        bg=Colors.background_color,
        fg=Colors.text_color,
    )
    title_label.pack()

    # Buttons
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


# Button Functions: Commands
def copy_file() -> None:
    """Make a copy of a file."""

    # Ask user for file to copy
    file_to_copy = filedialog.askopenfilename()
    # Get the base name of the file and rename it to "copy_of_{base_name}"
    base_name = os.path.basename(file_to_copy)
    renamed_base_name = f"copy_of_{base_name}"

    # Ask user for destination directory
    destination_directory = filedialog.askdirectory()

    # Create a new file with the renamed base name in the destination directory
    new_file = os.path.join(destination_directory, renamed_base_name)
    shutil.copy(file_to_copy, new_file)

    # Show a message box that the file has been copied message.showinfo(title, message)
    messagebox.showinfo("File Copied", f"File copied to {destination_directory}")



def move_file() -> None:
    """Move a file to a new directory."""

    # Ask user for file to move
    file_to_move: str = filedialog.askopenfilename()
    file_directory: str = os.path.dirname(file_to_move)

    # Ask user for destination directory
    destination_directory: str = filedialog.askdirectory()

    # Check if the file is being moved to the same directory
    # Show an error message if it is using messagebox.showerror(title, message)
    if file_directory == destination_directory:
        messagebox.showerror("Error", "Cannot move file to the same directory")
        return
    
    # Move the file to the destination directory
    shutil.move(file_to_move, destination_directory)

    # Show a message box that the file has been moved message.showinfo(title, message)
    messagebox.showinfo("File Moved", f"File moved to {destination_directory}")



def rename_file() -> None:
    """Rename a file."""

    # Ask user for file to rename
    file_to_rename: str = filedialog.askopenfilename()
    base_name: str = os.path.basename(file_to_rename)
    base_dir: str = os.path.dirname(file_to_rename)

    # Ask user for new file name using simpledialog.askstring(title, message)
    new_file_name: str = simpledialog.askstring("Rename File", "Enter new file name")

    # Check if the new file name is the same as the old file name
    # Show an error message if it is using messagebox.showerror(title, message)
    if base_name == new_file_name:
        messagebox.showerror("Error", "Cannot rename file to the same name")
        return

    # Create a new file path with the base directory and the new file name
    # Rename the file to the new file path
    new_file_path: str = os.path.join(base_dir, new_file_name)
    os.rename(file_to_rename, new_file_path)

    # Show a message box that the file has been renamed messagebox.showinfo(title, message)
    messagebox.showinfo("File Renamed", f"File renamed to {new_file_path}")



def delete_file() -> None:
    """Delete a file."""

    # Ask user for file to delete
    file_to_delete: str = filedialog.askopenfilename()

    # Confirm with the user if they want to delete the file
    # hint: can use confirm = messagebox.askyesno(title, message)
    confirm: bool = messagebox.askyesno("Delete File", "Are you sure you want to delete this file?")
    if not confirm:
        messagebox.showinfo("File Not Deleted", "File not deleted")
        return
    
    # Delete the file
    # send2trash(file) only works with paths that have backslashes on Windows
    # hint: use os.path.abspath to get the absolute path of the file to work with send2trash
    file_to_delete: str = os.path.abspath(file_to_delete)
    send2trash(file_to_delete)

    # Show a message box that the file has been deleted message.showinfo(title, message)
    messagebox.showinfo("File Deleted", f"File sent to trash")


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