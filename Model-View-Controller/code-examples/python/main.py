# main.py
"""
The main entry point for the application.

This script acts as the "Composition Root". It is responsible for creating
and wiring together all the components of the application (Model, View,
and Controller).
"""
from model import Model
from view import View
from controller import Controller

def main() -> None:
    """Constructs the application and runs the simulation."""
    
    # --- Composition Root: Create and wire components ---
    app_model = Model()
    app_view = View()
    app_controller = Controller(model=app_model, view=app_view)

    # --- Simulation: Run the application ---
    print("--- MVC Application Start ---")
    
    # Show initial empty list
    app_controller.update_view()
    
    # Simulate adding items
    app_controller.add_item_to_list("Buy groceries")
    app_controller.add_item_to_list("Read a book on design patterns")
    
    # Simulate adding a duplicate item
    app_controller.add_item_to_list("Buy groceries")
    
    # Simulate removing an item
    app_controller.remove_item_from_list("Read a book on design patterns")
    
    # Simulate removing a non-existent item
    app_controller.remove_item_from_list("Go to the gym")

    print("--- MVC Application End ---")


if __name__ == "__main__":
    main()
