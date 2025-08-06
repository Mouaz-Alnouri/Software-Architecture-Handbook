# contact_book_app/src/infrastructure/in_memory_repository.py
"""
This module contains the concrete implementation of the Contact Repository
using a simple in-memory dictionary as the data store.
"""
import uuid
from typing import Dict, List, Optional

from ..domain.repository import AbstractContactRepository, Contact

class InMemoryContactRepository(AbstractContactRepository):
    """
    Concrete repository implementation that stores contacts in memory.
    Ideal for testing and simple applications.
    """

    def __init__(self) -> None:
        self._contacts: Dict[uuid.UUID, Contact] = {}

    def add(self, contact: Contact) -> None:
        """Adds a contact to the in-memory dictionary."""
        self._contacts[contact.contact_id] = contact

    def get(self, contact_id: uuid.UUID) -> Optional[Contact]:
        """Retrieves a contact by its ID from the dictionary."""
        return self._contacts.get(contact_id)

    def list(self) -> List[Contact]:
        """Returns a list of all contacts."""
        return list(self._contacts.values())

    def delete(self, contact_id: uuid.UUID) -> None:
        """
        Deletes a contact from the in-memory dictionary.
        Fails silently if the ID does not exist.
        """
        self._contacts.pop(contact_id, None)

    def update(self, contact: Contact) -> None:
        """
        Updates a contact in the dictionary by replacing the existing one.
        Assumes the contact ID already exists.
        """
        if contact.contact_id in self._contacts:
            self._contacts[contact.contact_id] = contact