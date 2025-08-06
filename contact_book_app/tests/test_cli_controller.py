# src/contact_book_app/src/contact_book_app/presentation/cli_controller.py
"""
This module contains the Controller component for the CLI application.
"""
import time  # Import the time module
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..domain.model import ContactService
    from .cli_view import CLIView


class CLIController:
    """
    The command-line controller, responsible for handling user input
    and orchestrating the application flow.
    """

    def __init__(self, service: 'ContactService', view: 'CLIView'):
        self.service = service
        self.view = view

    def _display_menu(self):
        """Prints the command menu."""
        print("\n--- Commands ---")
        print("add    - Add a new contact")
        print("list   - Refresh the contact list view")
        print("update - Update a contact (by ID)")
        print("delete - Delete a contact (by ID)")
        print("exit   - Exit the application")
        print("----------------")

    def run(self):
        """Starts the main application loop."""
        while True:
            self._display_menu()
            command = input("Enter command: ").strip().lower()

            if command == "exit":
                print("Exiting...")
                break

            elif command == "add":
                name = input("Enter name: ").strip()
                email = input("Enter email (optional): ").strip()
                if not email:
                    email = None
                try:
                    self.service.add_contact(name=name, email=email)
                except ValueError as e:
                    print(f"Error: {e}")

            elif command == "update":
                try:
                    list_id = int(input("Enter contact ID to update: ").strip())
                    contacts = self.service.get_all_contacts()
                    if 1 <= list_id <= len(contacts):
                        contact_to_update = contacts[list_id - 1]

                        new_name = input(f"Enter new name for {contact_to_update.name}: ").strip()
                        new_email = input(f"Enter new email for {contact_to_update.name} (optional): ").strip()
                        if not new_email:
                            new_email = None

                        self.service.update_contact(
                            contact_id=contact_to_update.contact_id,
                            name=new_name,
                            email=new_email
                        )
                    else:
                        print("Error: Invalid ID.")
                except ValueError as e:
                    print(f"Error: Invalid input. Please enter a number. Details: {e}")

            elif command == "delete":
                try:
                    list_id = int(input("Enter contact ID to delete: ").strip())
                    contacts = self.service.get_all_contacts()
                    if 1 <= list_id <= len(contacts):
                        contact_to_delete = contacts[list_id - 1]
                        self.service.delete_contact(contact_id=contact_to_delete.contact_id)
                    else:
                        print("Error: Invalid ID.")
                except ValueError:
                    print("Error: Invalid input. Please enter a number.")

            elif command == "list":
                # Add feedback and a pause for a better user experience.
                print("Refreshing contact list...")
                time.sleep(0.75)
                self.view.display_contacts()

            else:
                print("Unknown command.")