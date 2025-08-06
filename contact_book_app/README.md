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
* **Repository Pattern:** Decouples business logic from the data source, allowing for easy substitution of data layers (e.g., from in-memory to a real database).
* **Observer Pattern:** Enables the Model to notify the View of state changes without creating a direct dependency, ensuring a reactive UI.
* **Test-Driven Development (TDD):** The entire application was built following a TDD workflow.
* **100% Test Coverage:** A comprehensive suite of unit tests using `pytest` and `unittest.mock`.
* **Modern Packaging:** Uses `pyproject.toml` and a `src-layout` for a clean, installable package with a command-line entry point.

## 🏛️ Architectural Overview

> The guiding principle of this project is **decoupling**. Each component is designed to be independent and easily replaceable, adhering to SOLID principles.

* **Model (Domain Layer):** The `ContactService` contains the core business rules (e.g., "a contact name cannot be empty," "emails must be unique"). It knows nothing about the UI or the database. It uses the `AbstractContactRepository` interface to request data operations and the `Observable` to announce changes.

* **View (Presentation Layer):** The `CLIView` is responsible only for displaying data. It implements the `Observer` interface and listens for notifications from the `ContactService`. When notified, it redraws the screen with the latest data.

* **Controller (Presentation Layer):** The `CLIController` handles user input. It translates commands like "add" into calls to the `ContactService`. It orchestrates the application but contains no business logic itself.

* **Repository (Infrastructure Layer):** The `InMemoryContactRepository` is a concrete implementation of the `AbstractContactRepository` interface defined in the domain. It handles the "how" of data storage. This could be swapped with a `SQLAlchemyRepository` or `FileRepository` without changing a single line of code in the domain or presentation layers.

## 📂 Project Structure

The project uses a modern `src-layout` to clearly separate the application package from other project files like tests and configuration.
