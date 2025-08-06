# contact_book_app/src/domain/model.py
"""This module defines the core business logic (domain model)."""

import uuid
from typing import List, Optional

from .repository import AbstractContactRepository, Contact
from .observer import Observable, Observer


class ContactService:
    """
    The service layer containing the core application logic.
    This class uses the Observable pattern to notify interested parties
    (like the UI) of changes.
    """

    def __init__(self, repo: AbstractContactRepository):
        self.repo = repo
        self._observable = Observable()

    def attach(self, observer: Observer) -> None:
        """Attach an observer to the service."""
        self._observable.attach(observer)

    def detach(self, observer: Observer) -> None:
        """Detach an observer from the service."""
        self._observable.detach(observer)

    def add_contact(self, name: str, email: Optional[str] = None) -> Contact:
        """
        Creates and adds a new contact.

        This is the primary business logic for adding a contact. It handles
        ID generation and validation before passing data to the repository.
        """
        if not name:
            raise ValueError("Name cannot be empty.")

        if email:
            existing_contacts = self.repo.list()
            for contact in existing_contacts:
                if contact.email == email:
                    raise ValueError("Email already exists.")

        new_contact = Contact(
            contact_id=uuid.uuid4(),
            name=name,
            email=email
        )
        self.repo.add(new_contact)
        self._observable.notify(self)  # NOTIFY with self (the service instance)
        return new_contact

    def get_all_contacts(self) -> List[Contact]:
        """Returns all contacts."""
        return self.repo.list()

    def delete_contact(self, contact_id: uuid.UUID) -> None:
        """Deletes a contact by their ID."""
        self.repo.delete(contact_id)
        self._observable.notify(self)  # NOTIFY with self

    def update_contact(self, contact_id: uuid.UUID, name: str, email: Optional[str]) -> Contact:
        """
        Updates an existing contact's details.

        This method retrieves a contact, applies the new data, checks for
        business rule violations, and then persists the changes.
        """
        contact_to_update = self.repo.get(contact_id)
        if not contact_to_update:
            raise ValueError("Contact not found.")

        if not name:
            raise ValueError("Name cannot be empty.")

        if email and email != contact_to_update.email:
            for contact in self.repo.list():
                if contact.contact_id != contact_id and contact.email == email:
                    raise ValueError("Email already exists.")

        contact_to_update.name = name
        contact_to_update.email = email

        self.repo.update(contact_to_update)
        self._observable.notify(self)  # NOTIFY with self
        return contact_to_update