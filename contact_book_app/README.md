# CLI Contact Book: A Clean Architecture Demo

[![Python CI and Test](https://github.com/Mouaz-Alnouri/Software-Architecture-Handbook/actions/workflows/main.yml/badge.svg)](https://github.com/Mouaz-Alnouri/Software-Architecture-Handbook/actions/workflows/main.yml)
![Python Version](https://img.shields.io/badge/python-3.7%2B-blue.svg)
![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

This isn't just another contact book application. It's a portfolio project designed from the ground up to demonstrate a professional, modern approach to software development. It serves as a practical example of building a robust, maintainable, and testable application using clean architecture principles in Python.

## ✨ Key Features

**User-Facing Features:**
* **Add, Update, and Delete** contacts.
* **List** all contacts in a clean, tabular format.
* An **interactive command-line interface** for easy use.
* **Automatic UI updates** whenever data changes.

**Technical & Architectural Features:**
* **Clean Architecture:** Strictly separates concerns into `domain`, `infrastructure`, and `presentation` layers.
* **Model-View-Controller (MVC):** The presentation layer is organized using the classic MVC pattern.
* **Repository Pattern:** Decouples business logic from the data source.
* **Observer Pattern:** Enables the Model to notify the View of state changes without creating a direct dependency.
* **Test-Driven Development (TDD):** The entire application was built following a TDD workflow.
* **Comprehensive Test Suite:** A full suite of unit tests using `pytest` and `unittest.mock`.
* **Modern Packaging:** Uses `pyproject.toml` and a `src-layout` for a clean, installable package with a command-line entry point.

## 🏛️ Architectural Overview

> The guiding principle of this project is **decoupling**. Each component is designed to be independent and easily replaceable, adhering to SOLID principles.

* **Model (Domain Layer):** The `ContactService` contains the core business rules and knows nothing about the UI or the database.
* **View (Presentation Layer):** The `CLIView` is responsible only for displaying data. It observes the Model for changes and refreshes itself.
* **Controller (Presentation Layer):** The `CLIController` handles user input and directs the Model.
* **Repository (Infrastructure Layer):** An abstraction that handles the "how" of data storage, allowing our business logic to remain blissfully ignorant of whether it's dealing with an in-memory list or a SQL database.

## 🧠 Design Philosophy & Patterns

This section details the specific design choices made during development.

### Test-Driven Development (TDD)
* **What it is:** A process where we write a failing test *before* writing the application code to make it pass.
* **Why we chose it:** It forces clear requirements and results in a simpler, more focused design. It also guarantees that every feature is tested from the start, providing a safety net for future changes.
* **When to use it:** Invaluable for any project with critical business logic where reliability and maintainability are key.

### Clean Architecture & SOLID Principles
* **What it is:** An architectural style that organizes code into independent layers (**Presentation**, **Domain**, **Infrastructure**). Inner layers (like `domain`) cannot know about outer layers.
* **Why we chose it:** It creates maximum **decoupling**. Our core business logic could be reused with a completely different UI or database without requiring any changes to the logic itself.
* **When to use it:** Ideal for any application that is expected to grow or change over time. It's the professional standard for building resilient, long-lasting software.

### Model-View-Controller (MVC) Pattern
* **What it is:** A pattern for organizing UI code into three distinct parts: the Model (data and logic), the View (display), and the Controller (user input).
* **Why we chose it:** It cleanly separates responsibilities. The logic for handling user commands isn't mixed up with the logic for displaying a table, making each part easier to understand and manage.
* **When to use it:** A standard pattern for any application with a user interface (CLI, desktop, or web).

### Repository Pattern
* **What it is:** An abstraction that separates the business logic from the details of data storage.
* **Why we chose it:** It makes our application incredibly flexible and **testable**. We can easily test our business logic with a fake in-memory repository without needing a real database. It also means we could swap our `InMemoryRepository` for a `SQLiteRepository` in the future with minimal effort.
* **When to use it:** Whenever your application needs to store and retrieve data.

### Observer Pattern
* **What it is:** A pattern where a "Subject" (our `ContactService`) notifies a list of "Observers" (our `CLIView`) when its state changes.
* **Why we chose it:** It allows the View to update automatically without being tightly coupled to the Model. The `ContactService` just sends out a notification, unaware of who or what is listening. This is key for a reactive UI.
* **When to use it:** Perfect for situations where one part of a system needs to react to changes in another part without creating a direct dependency.

## 📂 Project Structure

The project uses a modern src-layout to clearly separate the application package from other project files like tests and configuration.
```
contact-book-app/
+-- src/
|   +-- contact_book_app/   # Main application package
|       +-- __init__.py
|       +-- domain/         # Core business logic and entities
|       +-- infrastructure/ # Concrete data layer implementations
|       +-- presentation/   # UI components (View, Controller)
|       +-- main.py         # Application entry point callable
+-- tests/                  # Unit and integration tests
+-- pyproject.toml          # Project configuration and dependencies

```
## 🚀 Getting Started

Follow these steps to get the application running on your local machine.

Prerequisites
```
Python 3.7+

pip and venv
```
Installation
Clone the repository:

Bash
```
git clone [https://github.com/Mouaz-Alnouri/Software-Architecture-Handbook.git](https://github.com/Mouaz-Alnouri/Software-Architecture-Handbook.git)
cd Software-Architecture-Handbook
```
Create and activate a virtual environment:
Bash
```
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
Install the package in editable mode:
This command uses pyproject.toml to install the application and create the contact-book command-line script.
```
Bash
```
pip install -e .
```

## 💻 Usage

After installation, you can run the application from anywhere in your activated virtual environment.

Run the application:

Bash
```
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
```

✅ Running the Tests
To run the full suite of unit tests, use pytest.

Bash
```
pytest
```
You should see all tests pass, confirming the application's integrity.
```
========================= test session starts =========================
...
collected 17 items

tests/test_cli_controller.py ...                                 [ 17%]
tests/test_cli_view.py ..                                        [ 29%]
tests/test_contact_service.py ...........                        [ 94%]
tests/test_repository.py ...                                     [100%]

========================= 17 passed in 0.10s ==========================
```
## 📜 License

This project is licensed under the MIT License.
