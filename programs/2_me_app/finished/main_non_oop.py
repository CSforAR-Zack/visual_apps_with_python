import tkinter as tk


def main():
    root = tk.Tk()
    root.title("My App")
    root.geometry("800x620")

    main_frame = create_main_frame(root)
    content_frame = create_content_frame(main_frame)    
    navigator_frame = create_navigator(main_frame)
    create_buttons(navigator_frame, content_frame)
    
    # Load the initial page
    about_page(content_frame)

    root.mainloop()


def create_main_frame(root: tk.Tk) -> tk.Frame:
    """Create the main frame."""

    main_frame: tk.Frame = tk.Frame(root, bg=Color.COLOR1)
    main_frame.pack(fill=tk.BOTH, expand=True)
    return main_frame


def create_content_frame(main_frame: tk.Frame) -> tk.Frame:
    """Create the content frame."""

    content_frame: tk.Frame = tk.Frame(main_frame, bg=Color.COLOR1)
    content_frame.pack(fill=tk.BOTH, expand=True)
    return content_frame


def create_navigator(main_frame: tk.Frame) -> tk.Frame:
    """Create the navigator frame."""

    navigator_frame: tk.Frame = tk.Frame(main_frame, bg=Color.COLOR1)
    navigator_frame.pack(fill=tk.X, side=tk.BOTTOM)
    return navigator_frame


def create_buttons(navigator_frame: tk.Frame, content_frame: tk.Frame) -> None:
    """Create buttons for the navigator frame."""

    about_button: tk.Button = tk.Button(
        navigator_frame,
        text="About",
        command=lambda: about_page(content_frame),
        bg=Color.COLOR2,
        fg=Color.COLOR3,
    )
    about_button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    hobby_button: tk.Button = tk.Button(
        navigator_frame,
        text="Hobby",
        command=lambda: hobby_page(content_frame),
        bg=Color.COLOR2,
        fg=Color.COLOR3,
    )
    hobby_button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    work_button: tk.Button = tk.Button(
        navigator_frame,
        text="Work",
        command=lambda: work_page(content_frame),
        bg=Color.COLOR2,
        fg=Color.COLOR3,
    )
    work_button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)


def clear_frame(frame: tk.Frame) -> None:
    """Clear the frame of all widgets."""

    for child in frame.winfo_children():
        child.destroy()


def about_page(content_frame: tk.Frame) -> None:
    """Display the about page."""

    clear_frame(content_frame)

    title: tk.Label = tk.Label(
        content_frame,
        text="About me!",
        background=Color.COLOR1,
        foreground=Color.COLOR3,
        font=Font.TITLE,
    )
    title.pack()

    self_image: tk.PhotoImage = tk.PhotoImage(master=content_frame, file="self.png")
    self_image = self_image.subsample(2)
    self_label: tk.Label = tk.Label(
        content_frame,
        image=self_image,
        background=Color.COLOR1,
    )
    self_label.pack()        
    self_label.image = self_image

    content: tk.Label = tk.Label(
        content_frame,
        text="This is me! Let's get to know each other!",
        background=Color.COLOR1,
        foreground=Color.COLOR3,
        font=Font.TEXT,
    )
    content.pack()


def hobby_page(content_frame: tk.Frame) -> None:
    """Display the hobby page."""

    clear_frame(content_frame)

    title: tk.Label = tk.Label(
        content_frame,
        text="Gaming!",
        background=Color.COLOR1,
        foreground=Color.COLOR3,
        font=Font.TITLE,
    )
    title.pack()

    self_image: tk.PhotoImage = tk.PhotoImage(master=content_frame, file="hobby.png")
    self_image = self_image.subsample(2)
    self_label: tk.Label = tk.Label(
        content_frame,
        image=self_image,
        background=Color.COLOR1,
    )
    self_label.pack()       
    self_label.image = self_image

    content: tk.Label = tk.Label(
        content_frame,
        text="I like to play games! Let's play together!",
        background=Color.COLOR1,
        foreground=Color.COLOR3,
        font=Font.TEXT,
    )
    content.pack()


def work_page(content_frame: tk.Frame) -> None:
    """Display the work page."""

    clear_frame(content_frame)

    title: tk.Label = tk.Label(
        content_frame,
        text="Robot High!",
        background=Color.COLOR1,
        foreground=Color.COLOR3,
        font=Font.TITLE,
    )
    title.pack()

    self_image: tk.PhotoImage = tk.PhotoImage(master=content_frame, file="work.png")
    self_image = self_image.subsample(2)
    self_label: tk.Label = tk.Label(
        content_frame,
        image=self_image,
        background=Color.COLOR1,
    )
    self_label.pack()      
    self_label.image = self_image

    content: tk.Label = tk.Label(
        content_frame,
        text="This is my work! Let's work together!",
        background=Color.COLOR1,
        foreground=Color.COLOR3,
        font=Font.TEXT,
    )
    content.pack()


# Enums
class Color:
    """Color class to hold color values."""

    COLOR1: str = "#2E2E2E"
    COLOR2: str = "#3E3E3E"
    COLOR3: str = "#FFFFFF"


class Font:
    """Font class to hold font values."""

    TITLE: str = ("Arial", 24, "bold")
    TEXT: str = ("Arial", 12, "normal")


if __name__ == "__main__":
    main()