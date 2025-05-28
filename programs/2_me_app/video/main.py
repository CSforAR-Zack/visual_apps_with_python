import tkinter as tk


def main():
    app: MyApp = MyApp()
    app.mainloop()


class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("My App")
        self.geometry("800x620")

        self.create_main_frame()
        self.create_content_frame()
        self.create_navigator_frame()

        self.about_page()

    def create_main_frame(self) -> None:
        """Create the main frame."""

        self.main: tk.Frame = tk.Frame(self, bg=Color.COLOR1)
        self.main.pack(fill=tk.BOTH, expand=True)

    def create_content_frame(self) -> None:
        """Create the content frame."""

        self.content: tk.Frame = tk.Frame(self.main, bg=Color.COLOR1)
        self.content.pack(fill=tk.BOTH, expand=True)

    def create_navigator_frame(self) -> None:
        """Create the navigator frame."""

        self.navigator: tk.Frame = tk.Frame(self.main, bg=Color.COLOR3)
        self.navigator.pack(fill=tk.X, side=tk.BOTTOM)

        self.create_buttons()

    def create_buttons(self) -> None:
        """Create buttons for the navigator frame."""

        about_button: tk.Button = tk.Button(
           self.navigator,
           text="About",
           command=self.about_page,
           bg=Color.COLOR2,
           fg=Color.COLOR3,
        )
        about_button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        hobby_button: tk.Button = tk.Button(
           self.navigator,
           text="Hobby",
           command=self.hobby_page,
           bg=Color.COLOR2,
           fg=Color.COLOR3,
        )
        hobby_button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        work_button: tk.Button = tk.Button(
           self.navigator,
           text="Work",
           command=self.work_page,
           bg=Color.COLOR2,
           fg=Color.COLOR3,
        )
        work_button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    def clear_frame(self, frame: tk.Frame) -> None:
        """Clear the frame of all widgets."""

        for child in frame.winfo_children():
            child.destroy()

    def about_page(self) -> None:
        """Display the about page."""

        self.clear_frame(self.content)

        title: tk.Label = tk.Label(
            self.content,
            text="About me!",
            background=Color.COLOR1,
            foreground=Color.COLOR3,
            font=Font.TITLE,
        )
        title.pack()

        my_image: tk.PhotoImage = tk.PhotoImage(
            master=self.content, file="images/self.png"
        )
        my_image = my_image.subsample(2)
        my_label: tk.Label = tk.Label(
            self.content,
            image=my_image,
            background=Color.COLOR1,
        )
        my_label.pack()
        my_label.image = my_image

        content: tk.Label = tk.Label(
            self.content,
            text="This is me! Let's get to know each other!",
            background=Color.COLOR1,
            foreground=Color.COLOR3,
            font=Font.CONTENT,
        )
        content.pack()

    def hobby_page(self) -> None:
        """Display the hobby page."""

        self.clear_frame(self.content)

        title: tk.Label = tk.Label(
            self.content,
            text="Gaming!",
            background=Color.COLOR1,
            foreground=Color.COLOR3,
            font=Font.TITLE,
        )
        title.pack()

        my_image: tk.PhotoImage = tk.PhotoImage(
            master=self.content, file="images/hobby.png"
        )
        my_image = my_image.subsample(2)
        my_label: tk.Label = tk.Label(
            self.content,
            image=my_image,
            background=Color.COLOR1,
        )
        my_label.pack()
        my_label.image = my_image

        content: tk.Label = tk.Label(
            self.content,
            text="I like to play games! Let's play together!",
            background=Color.COLOR1,
            foreground=Color.COLOR3,
            font=Font.CONTENT,
        )
        content.pack()

    def work_page(self) -> None:
        """Display the about page."""

        self.clear_frame(self.content)

        title: tk.Label = tk.Label(
            self.content,
            text="Robot High!",
            background=Color.COLOR1,
            foreground=Color.COLOR3,
            font=Font.TITLE,
        )
        title.pack()

        my_image: tk.PhotoImage = tk.PhotoImage(
            master=self.content, file="images/work.png"
        )
        my_image = my_image.subsample(2)
        my_label: tk.Label = tk.Label(
            self.content,
            image=my_image,
            background=Color.COLOR1,
        )
        my_label.pack()
        my_label.image = my_image

        content: tk.Label = tk.Label(
            self.content,
            text="This is my work! Let's work together!",
            background=Color.COLOR1,
            foreground=Color.COLOR3,
            font=Font.CONTENT,
        )
        content.pack()


#Enums
class Color:
    """Color class to hold color values."""

    COLOR1: str = "#2E2E2E"
    COLOR2: str = "#3E3E3E"
    COLOR3: str = "#FFFFFF"


class Font:
    """Font class to hold font values."""

    TITLE: tuple = ("Arial", 24, "bold")
    CONTENT: tuple = ("Arial", 12, "normal")


if __name__ == "__main__":
    main()