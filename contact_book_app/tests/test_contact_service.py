# contact_book_app/tests/test_contact_service.py
"""Tests for the ContactService domain model."""

import pytest
from unittest.mock import MagicMock, ANY
from domain.repository import AbstractContactRepository, Contact
from domain.model import ContactService


@pytest.fixture
def mock_repo() -> MagicMock:
    """Provides a mocked repository for testing the service."""
    return MagicMock(spec=AbstractContactRepository)


def test_add_contact_successfully(mock_repo: MagicMock):
    """
    Tests that a contact with a valid name is created and added via the repo.
    """
    # ARRANGE
    # Configure the mock to return an empty list for the duplicate check
    mock_repo.list.return_value = []
    service = ContactService(repo=mock_repo)

    # ACT
    contact = service.add_contact(name="Jane Doe", email="jane.doe@example.com")

    # ASSERT
    assert contact.name == "Jane Doe"
    # Verify that the repository's add method was called exactly once with the new contact
    mock_repo.add.assert_called_once_with(contact)


def test_add_contact_with_empty_name_raises_error(mock_repo: MagicMock):
    """
    Tests that the service raises a ValueError if the name is empty.
    """
    # ARRANGE
    service = ContactService(repo=mock_repo)

    # ACT & ASSERT
    with pytest.raises(ValueError, match="Name cannot be empty."):
        service.add_contact(name="")

    # Verify that the repository's add method was NOT called
    mock_repo.add.assert_not_called()


def test_add_contact_with_duplicate_email_raises_error(mock_repo: MagicMock):
    """
    Tests that adding a contact with a pre-existing email raises a ValueError.
    """
    # ARRANGE
    # Create a pre-existing contact
    existing_contact = Contact(contact_id=ANY, name="John Doe", email="john.doe@example.com")

    # Configure the mock repository's list() method to return our pre-existing contact
    mock_repo.list.return_value = [existing_contact]
    service = ContactService(repo=mock_repo)

    # ACT & ASSERT
    with pytest.raises(ValueError, match="Email already exists."):
        # Attempt to add a new contact with the same email
        service.add_contact(name="Jane Doe", email="john.doe@example.com")

    # Verify that the repository's add method was NOT called
    mock_repo.add.assert_not_called()