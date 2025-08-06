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


def test_repository_can_delete_a_contact():
    """
    Tests that a contact can be deleted from the repository.
    """
    # ARRANGE
    repo = InMemoryContactRepository()
    contact_id = uuid.uuid4()
    contact = Contact(contact_id=contact_id, name="John Doe")
    repo.add(contact)

    assert len(repo.list()) == 1

    # ACT
    repo.delete(contact_id)

    # ASSERT
    assert repo.get(contact_id) is None
    assert len(repo.list()) == 0


def test_repository_can_update_a_contact():
    """
    Tests that a contact's details can be updated in the repository.
    """
    # ARRANGE
    repo = InMemoryContactRepository()
    contact_id = uuid.uuid4()
    original_contact = Contact(contact_id=contact_id, name="John Doe")
    repo.add(original_contact)

    # ACT
    updated_contact = Contact(contact_id=contact_id, name="Johnathan Doe", email="jd@example.com")
    repo.update(updated_contact)
    retrieved_contact = repo.get(contact_id)

    # ASSERT
    assert retrieved_contact == updated_contact
    assert retrieved_contact.name == "Johnathan Doe"
    assert retrieved_contact.email == "jd@example.com"