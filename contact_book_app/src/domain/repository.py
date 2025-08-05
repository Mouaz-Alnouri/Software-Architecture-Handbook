# contact_book_app/src/domain/repository.py
"""
This module defines the abstract interface for our data persistence layer.

It uses the Repository Pattern to decouple the application's business logic
from the specific data source (e.g., database, in-memory list).
"""
import uuid
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Contact:
    """A simple data class representing a contact entity."""
    contact_id: uuid.UUID
    name: str
    email: Optional[str] = None  # Optional field


class AbstractContactRepository(ABC):
    """Abstract base class defining the repository interface."""

    @abstractmethod
    def add(self, contact: Contact) -> None:
        """Adds a new contact to the repository."""
        raise NotImplementedError

    @abstractmethod
    def get(self, contact_id: uuid.UUID) -> Optional[Contact]:
        """Retrieves a contact by its unique ID."""
        raise NotImplementedError

    @abstractmethod
    def list(self) -> List[Contact]:
        """Lists all contacts in the repository."""
        raise NotImplementedError
