from model import TodoModel
from view import AppView
from controller import AppController


def main():
    model = TodoModel()
    view = AppView()
    controller = AppController(model, view)
    
    # 1. Observer Pattern: Tell Model to redraw the View when data changes
    model.add_observer(view.display_todos)
    
    # 2. Trigger the first database fetch to populate the screen on startup
    model.fetch_all()
    
    # 3. Start App
    view.mainloop()


if __name__ == "__main__":
    main()