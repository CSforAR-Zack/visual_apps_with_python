from model import TodoModel
from view import AppView
from controller import AppController


def main():
    model = TodoModel()
    view = AppView()
    controller = AppController(model, view)
    
    controller.refresh_view()  # Load initial data into the view   
    view.mainloop()


if __name__ == "__main__":
    main()