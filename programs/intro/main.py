import tkinter as tk


def main():
    root: tk.Tk = tk.Tk()
    root.title("HELLO")

    welcome_frame = welcome_page(root)
    welcome_frame.pack(fill="both", expand=True)

    # self_image: tk.PhotoImage = tk.PhotoImage(master=root, file="intro/self.png")
    # self_image = self_image.subsample(2)
    # self_label: tk.Label = tk.Label(root, image=self_image)

    # self_label.pack(fill="x", padx=10, pady=5)

    root.mainloop()


def welcome_page(root: tk.Tk) -> tk.Frame:
    """Shows picture of me and buttons to navigate to: hobby, food, school."""

    welcome_frame: tk.Frame = tk.Frame(root)
    self_image: tk.PhotoImage = tk.PhotoImage(master=welcome_frame, file="intro/self.png")
    self_image = self_image.subsample(2)
    self_label: tk.Label = tk.Label(welcome_frame, image=self_image)

    self_label.pack(fill="x", padx=10, pady=5)

    return welcome_frame



if __name__ == "__main__":
    main()