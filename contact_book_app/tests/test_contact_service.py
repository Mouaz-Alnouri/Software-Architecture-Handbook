# contact_book_app/tests/test_contact_service.py
"""Tests for the ContactService domain model."""

import uuid
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
    mock_repo.list.return_value = []
    service = ContactService(repo=mock_repo)

    # ACT
    contact = service.add_contact(name="Jane Doe", email="jane.doe@example.com")

    # ASSERT
    assert contact.name == "Jane Doe"
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

    mock_repo.add.assert_not_called()


def test_add_contact_with_duplicate_email_raises_error(mock_repo: MagicMock):
    """

    Tests that adding a contact with a pre-existing email raises a ValueError.
    """
    # ARRANGE
    existing_contact = Contact(contact_id=ANY, name="John Doe", email="john.doe@example.com")
    mock_repo.list.return_value = [existing_contact]
    service = ContactService(repo=mock_repo)

    # ACT & ASSERT
    with pytest.raises(ValueError, match="Email already exists."):
        service.add_contact(name="Jane Doe", email="john.doe@example.com")

    mock_repo.add.assert_not_called()


def test_delete_contact_successfully(mock_repo: MagicMock):
    """
    Tests that the service calls the repo's delete method with the correct ID.
    """
    # ARRANGE
    service = ContactService(repo=mock_repo)
    contact_id_to_delete = uuid.uuid4()

    # ACT
    service.delete_contact(contact_id=contact_id_to_delete)

    # ASSERT
    mock_repo.delete.assert_called_once_with(contact_id_to_delete)