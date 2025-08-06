# contact_book_app/src/main.py
"""
The main entry point for the Contact Book CLI application.
"""
import time
from domain.model import ContactService
from infrastructure.in_memory_repository import InMemoryContactRepository
from presentation.cli_view import CLIView


def main():
    """
    Initializes the application components and runs a simple demonstration.
    """
    # 1. Initialize Components
    repo = InMemoryContactRepository()
    service = ContactService(repo)
    view = CLIView(service)

    # 2. Wire them together: The View observes the Service
    service.attach(view)

    # 3. Run a simple demonstration to show the Observer pattern in action

    # Initially, the view will show an empty list
    print("Initializing...")
    view.display_contacts()
    time.sleep(2)

    # Add a contact - the view should automatically refresh
    print("\nAdding a new contact: Alice...")
    service.add_contact(name="Alice", email="alice@example.com")
    time.sleep(2)

    # Add another contact
    print("\nAdding a new contact: Bob...")
    service.add_contact(name="Bob", email=None)
    time.sleep(2)

    # Get one of the contacts to update it
    print("\nUpdating Alice's name...")
    alice_contact = [c for c in service.get_all_contacts() if c.name == "Alice"][0]
    service.update_contact(
        contact_id=alice_contact.contact_id,
        name="Alice Smith",
        email="asmith@example.com"
    )
    time.sleep(2)

    # Delete a contact
    print("\nDeleting Bob...")
    bob_contact = [c for c in service.get_all_contacts() if c.name == "Bob"][0]
    service.delete_contact(contact_id=bob_contact.contact_id)
    time.sleep(2)

    print("\nDemonstration finished.")


if __name__ == "__main__":
    main()