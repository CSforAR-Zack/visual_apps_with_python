import tkinter as tk


class MyApp(tk.Frame):

    def __init__(self, root: tk.Tk):

        self.current_page_index: int = 0
        self.pages: list = [self.about_page, self.hobby_page, self.work_page]

        self.color1: str = "#222448"
        self.color2: str = "#54527E"
        self.color3: str = "#FFFFFF"

        self.title_font: tuple = ("Arial", 18)
        self.content_font: tuple = ("Arial", 12)

        super().__init__(root, bg=self.color1)

        self.main_frame = self
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.rowconfigure(0, weight=1)

        self.load_main_widgets()

    def load_main_widgets(self):
        self.create_page_container()
        self.create_navigator()
        self.pages[self.current_page_index]()

    def create_page_container(self) -> None:        
        self.page_container = tk.Frame(self.main_frame, bg=self.color1)
        self.page_container.grid(column=0, row=0, sticky=tk.NSEW)
        self.page_container.columnconfigure(0, weight=1)
        self.page_container.rowconfigure(0, weight=1)

    def create_navigator(self) -> None:
        self.navigator = tk.Frame(self.main_frame, bg=self.color2)
        self.navigator.grid(column=0, row=1, sticky=tk.NSEW)
        self.navigator.columnconfigure(0, weight=1)
        self.navigator.columnconfigure(1, weight=1)
        self.navigator.columnconfigure(2, weight=1)

        about_button: tk.Button = tk.Button(
            self.navigator,
            text="About",
            bg=self.color2,
            fg=self.color3,
            command=self.nav_to_about,
        )
        about_button.grid(column=0, row=0, sticky="nsew")

        hobby_button: tk.Button = tk.Button(
            self.navigator,
            text="Hobby",
            bg=self.color2,
            fg=self.color3,
            command=self.nav_to_hobby,
        )
        hobby_button.grid(column=1, row=0, sticky="nsew")

        work_button: tk.Button = tk.Button(
            self.navigator,
            text="Work",
            bg=self.color2,
            fg=self.color3,
            command=self.nav_to_work,
        )
        work_button.grid(column=2, row=0, sticky="nsew")

    def clear_frame(self, frame: tk.Frame) -> None:
        for child in frame.winfo_children():
            child.destroy()

    def nav_to_about(self) -> None:
        self.clear_frame(self.page_container)
        self.current_page_index = 0
        self.pages[self.current_page_index]()

    def nav_to_hobby(self) -> None:
        self.clear_frame(self.page_container)
        self.current_page_index = 1
        self.pages[self.current_page_index]()

    def nav_to_work(self) -> None:
        self.clear_frame(self.page_container)
        self.current_page_index = 2
        self.pages[self.current_page_index]()

    def about_page(self) -> None:
        title: tk.Label = tk.Label(
            self.page_container,
            background=self.color1,
            foreground=self.color3,
            text="About me!",
            font=self.title_font,
        )

        title.grid(column=0, row=0)

        self_image: tk.PhotoImage = tk.PhotoImage(master=self.page_container, file="self.png")
        self_image = self_image.subsample(2)
        self_label: tk.Label = tk.Label(
            self.page_container,
            image=self_image,
            background=self.color1,
        )
        self_label.grid(column=0, row=1, sticky=tk.NSEW)        
        self_label.image = self_image

        title: tk.Label = tk.Label(
            self.page_container,
            background=self.color1,
            foreground=self.color3,
            text="This is me! Let's get to know each other!",
            font=self.content_font,
        )

        title.grid(column=0, row=2)

    def hobby_page(self) -> None:
        title: tk.Label = tk.Label(
            self.page_container,
            background=self.color1,
            foreground=self.color3,
            text="Gaming!",
            font=self.title_font,
        )

        title.grid(column=0, row=0)

        self_image: tk.PhotoImage = tk.PhotoImage(master=self.page_container, file="hobby.png")
        self_image = self_image.subsample(2)
        self_label: tk.Label = tk.Label(
            self.page_container,
            image=self_image,
            background=self.color1,
        )
        self_label.grid(column=0, row=1, sticky=tk.NSEW)        
        self_label.image = self_image

        title: tk.Label = tk.Label(
            self.page_container,
            background=self.color1,
            foreground=self.color3,
            text="I like to play games! Let's play together!",
            font=self.content_font,
        )

        title.grid(column=0, row=2)

    def work_page(self) -> None:
        title: tk.Label = tk.Label(
            self.page_container,
            background=self.color1,
            foreground=self.color3,
            text="Robot High!",
            font=self.title_font,
        )

        title.grid(column=0, row=0)

        self_image: tk.PhotoImage = tk.PhotoImage(master=self.page_container, file="work.png")
        self_image = self_image.subsample(2)
        self_label: tk.Label = tk.Label(
            self.page_container,
            image=self_image,
            background=self.color1,
        )
        self_label.grid(column=0, row=1, sticky=tk.NSEW)        
        self_label.image = self_image

        title: tk.Label = tk.Label(
            self.page_container,
            background=self.color1,
            foreground=self.color3,
            text="This is my work! Let's work together!",
            font=self.content_font,
        )

        title.grid(column=0, row=2)


if __name__ == "__main__":
    root: tk.Tk = tk.Tk()
    root.geometry("800x600")
    root.title("My Application")
    root.resizable(False, False)
    app = MyApp(root)
    root.mainloop()