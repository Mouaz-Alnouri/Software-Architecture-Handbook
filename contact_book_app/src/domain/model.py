# contact_book_app/src/domain/model.py
"""This module defines the core business logic (domain model)."""

import uuid
from typing import List, Optional

from .repository import AbstractContactRepository, Contact


class ContactService:
    """The service layer containing the core application logic."""

    def __init__(self, repo: AbstractContactRepository):
        self.repo = repo

    def add_contact(self, name: str, email: Optional[str] = None) -> Contact:
        """
        Creates and adds a new contact.

        This is the primary business logic for adding a contact. It handles
        ID generation and validation before passing data to the repository.
        """
        if not name:
            raise ValueError("Name cannot be empty.")

        # Check for duplicate emails. This check is ignored if email is None.
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
        return new_contact

    def get_all_contacts(self) -> List[Contact]:
        """Returns all contacts."""
        return self.repo.list()

    def delete_contact(self, contact_id: uuid.UUID) -> None:
        """Deletes a contact by their ID."""
        self.repo.delete(contact_id)