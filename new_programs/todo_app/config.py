import json
from pathlib import Path
from dataclasses import dataclass


_config_path = Path(__file__).parent / "config.json"
with open(_config_path, "r", encoding="utf-8") as f:
    _config_data = json.load(f)


class Theme:
    """Dynamically loaded UI settings."""
    TITLE = _config_data["window"]["title"]
    WIDTH = _config_data["window"]["width"]
    HEIGHT = _config_data["window"]["height"]
    LOGO_FILE = _config_data["window"]["logo_file"]
    LOGO_SUBSAMPLE = _config_data["window"]["logo_subsample"]
    
    BG = _config_data["colors"]["bg"]
    LIST_BG = _config_data["colors"]["list_bg"]
    FG = _config_data["colors"]["fg"]
    ACCENT = _config_data["colors"]["accent"]
    DANGER = _config_data["colors"]["danger"]
    EDIT = _config_data["colors"]["edit"]
    
    FONT_TITLE = tuple(_config_data["fonts"]["title"])
    FONT_TEXT = tuple(_config_data["fonts"]["text"])


@dataclass
class TodoItem:
    """A data container representing a single row in the database."""
    id: int
    task: str
    is_completed: bool