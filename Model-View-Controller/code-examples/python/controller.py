# controller.py
"""
Coordinates interactions between the Model and the View.

It receives user input (in this simulation, direct method calls) and
invokes changes on the model. After an action, it updates the view with
the latest data from the model.
"""
from model import Model
from view import View

class Controller:
    """
    The controller class that orchestrates the application.

    This class uses dependency injection to receive its model and view,
    making it decoupled and testable.
    """

    def __init__(self, model: Model, view: View) -> None:
        """
        Initializes the Controller.

        Args:
            model (Model): The data model instance.
            view (View): The presentation view instance.
        """
        self.model = model
        self.view = view

    def add_item_to_list(self, item: str) -> None:
        """
        Handles the logic for adding an item.

        Args:
            item (str): The item to add.
        """
        try:
            message = self.model.add_item(item)
            self.view.display_message(message)
        except ValueError as e:
            self.view.display_message(f"Error: {e}")
        finally:
            self.update_view()

    def remove_item_from_list(self, item: str) -> None:
        """
        Handles the logic for removing an item.

        Args:
            item (str): The item to remove.
        """
        message = self.model.remove_item(item)
        self.view.display_message(message)
        self.update_view()

    def update_view(self) -> None:
        """Updates the view with the current list of items."""
        items = self.model.get_items()
        self.view.display_items(items)
