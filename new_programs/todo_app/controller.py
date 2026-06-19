from model import TodoModel
from view import AppView


class AppController:
    """Connects the GUI actions to the Database logic."""
    
    def __init__(self, model: TodoModel, view: AppView):
        self.model = model
        self.view = view

        # Wire up the view's commands to the model's database functions
        self.view.bind_commands(
            add_cmd=self.model.add_task,
            toggle_cmd=self.model.toggle_task,
            delete_cmd=self.model.delete_task,
            edit_cmd=self.model.edit_task
        )