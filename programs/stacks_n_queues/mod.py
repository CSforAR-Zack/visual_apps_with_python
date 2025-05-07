# Module for week 9: Stacks and Queues
from typing import Optional

# Base class
class BaseStructure:
    """Base class for Stack and Queue classes"""

    # Constructor with instance variable
    def __init__(self, type: str, items: Optional[list] = None) -> None:
        """Create a new stack"""

        self.type: str = type
        self.items: list = []

        if items is not None:
            self.items: list = items

    # Methods
    def is_empty(self) -> bool:
        """Return True if the stack is empty, False otherwise"""

        return not self.items
    
    def enter_value(self, item: int) -> None:
        """Add an item to the data structure"""

        self.items.append(item)

    # Magic methods
    def __str__(self) -> str:
        """Return a string representation of the stack"""

        return f"{self.type}: {str(self.items)}"


# Stack class
class Stack(BaseStructure):
    """Stack class with a list as the underlying data structure."""

    def __init__(self, items: Optional[list] = None) -> None:
        """Create a new stack"""

        super().__init__("Stack", items)

    # Methods

    def get_value(self) -> Optional[int]:
        """Remove and return the top ite from stack or None if the stack is empty"""
            
        if not self.is_empty():
            return self.items.pop()
        else:
            return None
    
    def view_next(self) -> Optional[int]:
        """Return the top item from the stack or None if the stack is empty"""

        if not self.is_empty():
            return self.items[-1]
        else:
            return None


# Create a Queue class here
# Queue class
class Queue(BaseStructure):
    """Queue class with a list as the underlying data structure."""

    def __init__(self, items: Optional[list] = None) -> None:
        """Create a new queue"""

        super().__init__("Queue", items)
    
    # Methods

    def get_value(self) -> Optional[int]:
        """Remove and return the oldest item from the queue or None if the queue is empty"""
            
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None
    
    def view_value(self) -> Optional[int]:
        """Return the oldest item from the queue or None if the queue is empty"""

        if not self.is_empty():
            return self.items[0]
        else:
            return None