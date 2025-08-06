# src/contact_book_app/main.py
"""
The main entry point for the Contact Book CLI application.
"""
from .domain.model import ContactService
from .infrastructure.in_memory_repository import InMemoryContactRepository
from .presentation.cli_view import CLIView
from .presentation.cli_controller import CLIController


def main():
    """
    Initializes the application components and starts the controller.
    """
    # 1. Initialize Components
    repo = InMemoryContactRepository()
    service = ContactService(repo)
    view = CLIView(service)
    # Pass both the service and the view to the controller
    controller = CLIController(service=service, view=view)

    # 2. Wire them together: The View observes the Service
    service.attach(view)

    # 3. Display the initial empty view
    view.display_contacts()

    # 4. Hand control to the controller's main loop
    controller.run()


if __name__ == "__main__":
    main()