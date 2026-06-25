from model import TodoModel
from view import AppView


class AppController:
    """Connects the GUI actions to the Database logic."""
    
    def __init__(self, model: TodoModel, view: AppView):
        self.model = model
        self.view = view
        
        # Wire up the view's commands to the controller's new handler functions
        self.view.bind_commands(
            add_cmd=self.handle_add_task,
            toggle_cmd=self.handle_toggle_task,
            delete_cmd=self.handle_delete_task,
            edit_cmd=self.handle_edit_task
        )
        
    def refresh_view(self) -> None:
        """Pulls fresh data from the model and pushes it to the view."""
        todos = self.model.fetch_all()
        self.view.display_todos(todos)

    def handle_add_task(self, task_text: str) -> None:
        self.model.add_task(task_text)
        self.refresh_view()

    def handle_toggle_task(self, task_id: int, is_completed: bool) -> None:
        self.model.toggle_task(task_id, is_completed)
        self.refresh_view()

    def handle_delete_task(self, task_id: int) -> None:
        self.model.delete_task(task_id)
        self.refresh_view()

    def handle_edit_task(self, task_id: int, new_text: str) -> None:
        self.model.edit_task(task_id, new_text)
        self.refresh_view()