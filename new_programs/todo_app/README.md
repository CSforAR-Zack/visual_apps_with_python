# To-Do App

A simple desktop To-Do application built with Python. Tasks are saved to a local database so they persist between sessions.

![To-Do App](logo.png)

---

## Features

- Add, edit, and delete tasks
- Mark tasks as complete or incomplete
- Tasks are saved automatically — nothing is lost when you close the app

---

## Requirements

- Python 3.10 or higher
- Tkinter (included with most Python installations)

No additional packages need to be installed.

---

## How to Run

1. Clone or download this repository
2. Open a terminal in the project folder
3. Run the following command:

```bash
python main.py
```

---

## Project Structure

```
todo_app/
├── main.py          # Entry point — starts the app
├── model.py         # Handles data and database logic
├── view.py          # Builds and manages the UI
├── controller.py    # Connects the model and the view
├── config.py        # Loads settings and defines data types
├── config.json      # UI theme settings (colors, fonts, window size)
├── logo.png         # App icon
└── todos.db         # SQLite database (created automatically on first run)
```

---

## Architecture

This app follows the **MVC (Model-View-Controller)** pattern, a common way to organize code by separating responsibilities:

| Layer | File | Responsibility |
|---|---|---|
| **Model** | `model.py` | Reads and writes data to the database |
| **View** | `view.py` | Displays the UI to the user |
| **Controller** | `controller.py` | Responds to user actions and updates the model |

The model uses the **Observer pattern** — when data changes, it automatically notifies the view to refresh, so the UI always stays in sync with the database.

---

## Database

Tasks are stored in a local SQLite database file (`todos.db`) with a single table:

| Column | Type | Description |
|---|---|---|
| `id` | INTEGER | Unique identifier for each task |
| `task` | TEXT | The task description |
| `is_completed` | BOOLEAN | Whether the task is done (0 = no, 1 = yes) |

---

## Running the Tests

Unit tests for the model are located in `test_model.py`. To run them:

```bash
python -m pytest test_model.py
```

> Note: You may need to install pytest first with `pip install pytest`.

---

## License

This project was created for educational purposes as part of a Python training course.
