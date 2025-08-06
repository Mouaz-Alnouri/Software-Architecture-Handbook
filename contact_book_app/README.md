CLI Contact Book: A Clean Architecture Demo
This isn't just another contact book application. It's a portfolio project designed from the ground up to demonstrate a professional, modern approach to software development. It serves as a practical example of building a robust, maintainable, and testable application using clean architecture principles in Python.

✨ Key Features
User-Facing Features:

Add, Update, and Delete contacts.

List all contacts in a clean, tabular format.

An interactive command-line interface for easy use.

Automatic UI updates whenever data changes.

Technical & Architectural Features:

Clean Architecture: Strictly separates concerns into domain, infrastructure, and presentation layers.

Model-View-Controller (MVC): The presentation layer is organized using the classic MVC pattern.

Repository Pattern: Decouples business logic from the data source, allowing for easy substitution of data layers (e.g., from in-memory to a real database).

Observer Pattern: Enables the Model to notify the View of state changes without creating a direct dependency, ensuring a reactive UI.

Test-Driven Development (TDD): The entire application was built following a TDD workflow.

100% Test Coverage: A comprehensive suite of unit tests using pytest and unittest.mock.

Modern Packaging: Uses pyproject.toml and a src-layout for a clean, installable package with a command-line entry point.

🏛️ Architectural Overview
The guiding principle of this project is decoupling. Each component is designed to be independent and easily replaceable, adhering to SOLID principles.

Model (Domain Layer): The ContactService contains the core business rules (e.g., "a contact name cannot be empty," "emails must be unique"). It knows nothing about the UI or the database. It uses the AbstractContactRepository interface to request data operations and the Observable to announce changes.

View (Presentation Layer): The CLIView is responsible only for displaying data. It implements the Observer interface and listens for notifications from the ContactService. When notified, it redraws the screen with the latest data.

Controller (Presentation Layer): The CLIController handles user input. It translates commands like "add" into calls to the ContactService. It orchestrates the application but contains no business logic itself.

Repository (Infrastructure Layer): The InMemoryContactRepository is a concrete implementation of the AbstractContactRepository interface defined in the domain. It handles the "how" of data storage. This could be swapped with a SQLAlchemyRepository or FileRepository without changing a single line of code in the domain or presentation layers.

📂 Project Structure
The project uses a modern src-layout to clearly separate the application package from other project files like tests and configuration.

contact-book-app/
├── src/
│   └── contact_book_app/   # Main application package
│       ├── __init__.py
│       ├── domain/         # Core business logic, entities, and interfaces
│       ├── infrastructure/ # Concrete data layer implementations
│       ├── presentation/   # UI components (View, Controller)
│       └── main.py         # Application entry point callable
├── tests/                  # All unit tests for the application
└── pyproject.toml          # Project config, dependencies, and entry points
🚀 Getting Started
Follow these steps to get the application running on your local machine.

Prerequisites
Python 3.7+

pip and venv

Installation
Clone the repository:

Bash

git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO
Create and activate a virtual environment:

Bash

# For Windows
python -m venv ex_venv
ex_venv\Scripts\activate

# For macOS/Linux
python3 -m venv ex_venv
source ex_venv/bin/activate
Install the package in editable mode:
This command uses pyproject.toml to install the application and create the contact-book command-line script.

Bash

pip install -e .
💻 Usage
After installation, you can run the application from anywhere in your activated virtual environment.

Run the application:

Bash

contact-book
Interact with the menu:
The application will launch and display the contact list and a menu of commands.

===== Contact Book =====
No contacts found.
========================

--- Commands ---
add    - Add a new contact
list   - Refresh the contact list view
update - Update a contact (by ID)
delete - Delete a contact (by ID)
exit   - Exit the application
----------------
Enter command:
✅ Running the Tests
To run the full suite of unit tests, use pytest.

Bash

pytest
You should see all tests pass, confirming the application's integrity.

========================= test session starts =========================
...
collected 17 items

tests/test_cli_controller.py ...                                 [ 17%]
tests/test_cli_view.py ..                                        [ 29%]
tests/test_contact_service.py ...........                        [ 94%]
tests/test_repository.py ...                                     [100%]

========================= 17 passed in 0.10s ==========================
📜 License
This project is licensed under the MIT License. See the LICENSE file for details.