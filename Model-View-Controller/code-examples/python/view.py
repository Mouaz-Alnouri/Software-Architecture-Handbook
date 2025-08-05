# view.py
"""
Contains the presentation logic of the application.

Its sole responsibility is to display data provided by the controller.
It should not contain any business logic.
"""
from typing import List

class View:
    """A simple console-based view to display data."""

    def display_items(self, items: List[str]) -> None:
        """
        Prints the list of items to the console.

        Args:
            items (List[str]): The list of items to display.
        """
        print("--- Your List ---")
        if not items:
            print("The list is empty.")
        else:
            for item in items:
                print(f"- {item}")
        print("-----------------\n")

    def display_message(self, message: str) -> None:
        """
        Prints a general status message to the console.

        Args:
            message (str): The message to display.
        """
        print(f"STATUS: {message}\n")
