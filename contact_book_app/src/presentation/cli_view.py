# contact_book_app/src/presentation/cli_view.py
"""
This module contains the View component for the CLI application.
"""
import os
from typing import TYPE_CHECKING
from domain.observer import Observer

# Use a forward reference for the ContactService type hint
if TYPE_CHECKING:
    from domain.model import ContactService


class CLIView(Observer):
    """
    The command-line view, responsible for displaying contacts.
    It observes the ContactService for changes and refreshes automatically.
    """

    def __init__(self, service: 'ContactService'):
        self.service = service

    def display_contacts(self) -> None:
        """
        Fetches contacts from the service and prints them in a formatted table.
        """
        contacts = self.service.get_all_contacts()

        # Clear the console screen
        os.system('cls' if os.name == 'nt' else 'clear')

        print("===== Contact Book =====")
        if not contacts:
            print("No contacts found.")
        else:
            # Simple table formatting
            # Header
            print(f"{'ID':<5} | {'Name':<20} | {'Email':<30}")
            print("-" * 60)
            # Rows
            for i, contact in enumerate(contacts, 1):
                email_str = contact.email if contact.email is not None else "N/A"
                print(f"{i:<5} | {contact.name:<20} | {email_str:<30}")

        print("=" * 24)

    def update(self, subject: 'ContactService') -> None:
        """
        Receives notification from the service and redraws the contact list.
        """
        print("\nChange detected, refreshing view...")
        self.display_contacts()