# contact_book_app/tests/test_repository.py
"""Tests for the repository implementations."""
import uuid
import pytest
from domain.repository import Contact
from infrastructure.in_memory_repository import InMemoryContactRepository


def test_repository_can_add_a_contact():
    """
    Tests that a contact can be added to the repository and retrieved.
    """
    # ARRANGE
    repo = InMemoryContactRepository()
    contact_id = uuid.uuid4()
    contact = Contact(contact_id=contact_id, name="John Doe")

    # ACT
    repo.add(contact)
    retrieved_contact = repo.get(contact_id)

    # ASSERT
    assert retrieved_contact == contact
    assert len(repo.list()) == 1
