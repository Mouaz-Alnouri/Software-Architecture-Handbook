# model.py
"""
Contains the data and business logic of the application.

It manages the state and notifies observers of any changes, but it does not
handle how the data is displayed or how user input is received.
"""
from typing import List

class Model:
    """Manages the application's data store (a simple list of items)."""

    def __init__(self) -> None:
        """Initializes the model with an empty list of items."""
        self._item_list: List[str] = []

    def add_item(self, item: str) -> str:
        """
        Adds a new item to the list if it's not a duplicate.

        Args:
            item (str): The item to be added.

        Returns:
            str: A message indicating the result of the operation.
        """
        if not isinstance(item, str) or not item:
            raise ValueError("Item must be a non-empty string.")

        if item not in self._item_list:
            self._item_list.append(item)
            return f"Success: '{item}' added."
        return f"Error: '{item}' is already in the list."

    def remove_item(self, item: str) -> str:
        """
        Removes an item from the list if it exists.

        Args:
            item (str): The item to be removed.

        Returns:
            str: A message indicating the result of the operation.
        """
        if item in self._item_list:
            self._item_list.remove(item)
            return f"Success: '{item}' removed."
        return f"Error: '{item}' not found."

    def get_items(self) -> List[str]:
        """
        Retrieves the current list of items.

        Returns:
            List[str]: A copy of the item list to prevent direct modification.
        """
        return self._item_list.copy()
