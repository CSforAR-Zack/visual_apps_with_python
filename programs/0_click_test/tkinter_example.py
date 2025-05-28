import tkinter as tk


def on_button_click(label_count):
    current_count = int(label_count['text'].split(': ')[1])
    new_count = current_count + 1
    label_count['text'] = f"Click Count: {new_count}"
    

def create_window():
    window = tk.Tk()
    window.title("Simple Tkinter Example")

    font = ("Arial", 24, "bold")
    window.option_add("*Font", font)
    window.geometry("400x200")
    
    label = tk.Label(window, text="Hello, Tkinter!")
    label.pack(pady=10)
    
    button = tk.Button(window, text="Click Me", command=lambda: on_button_click(label_count))
    button.pack(pady=5)

    label_count = tk.Label(window, text="Click Count: 0")
    label_count.pack(pady=5)
    
    window.mainloop()

if __name__ == "__main__":
    create_window()