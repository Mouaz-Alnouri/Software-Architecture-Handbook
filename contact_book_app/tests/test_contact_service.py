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
    # Add all methods from the Abstract repo to the mock spec
    # This ensures that calling an unimplemented method on the mock will fail the test
    methods = [func for func in dir(AbstractContactRepository) if
               callable(getattr(AbstractContactRepository, func)) and not func.startswith("__")]
    return MagicMock(spec=AbstractContactRepository, **{method: MagicMock() for method in methods})


# ... (keep all existing test functions: test_add_contact_successfully, test_add_contact_with_empty_name_raises_error, test_add_contact_with_duplicate_email_raises_error, test_delete_contact_successfully) ...

def test_update_contact_successfully(mock_repo: MagicMock):
    """
    Tests that a contact can be successfully updated.
    """
    # ARRANGE
    service = ContactService(repo=mock_repo)
    contact_id = uuid.uuid4()
    original_contact = Contact(contact_id=contact_id, name="Old Name", email="old@example.com")

    # Configure mock repo to return the original contact when 'get' is called
    mock_repo.get.return_value = original_contact
    # Configure list to return an empty list for the duplicate email check
    mock_repo.list.return_value = []

    # ACT
    updated_contact = service.update_contact(
        contact_id=contact_id,
        name="New Name",
        email="new@example.com"
    )

    # ASSERT
    mock_repo.get.assert_called_once_with(contact_id)
    assert updated_contact.name == "New Name"
    assert updated_contact.email == "new@example.com"

    # Check that update was called with the modified contact object
    mock_repo.update.assert_called_once_with(original_contact)


def test_update_non_existent_contact_raises_error(mock_repo: MagicMock):
    """
    Tests that updating a contact that does not exist raises a ValueError.
    """
    # ARRANGE
    service = ContactService(repo=mock_repo)
    non_existent_id = uuid.uuid4()

    # Configure mock repo to simulate that the contact was not found
    mock_repo.get.return_value = None

    # ACT & ASSERT
    with pytest.raises(ValueError, match="Contact not found."):
        service.update_contact(contact_id=non_existent_id, name="any name", email="any@email.com")

    mock_repo.update.assert_not_called()


def test_update_contact_to_duplicate_email_raises_error(mock_repo: MagicMock):
    """
    Tests that updating a contact's email to one that already exists raises an error.
    """
    # ARRANGE
    service = ContactService(repo=mock_repo)
    contact_to_update_id = uuid.uuid4()

    contact_to_update = Contact(contact_id=contact_to_update_id, name="Jane Doe", email="jane@example.com")
    existing_contact = Contact(contact_id=uuid.uuid4(), name="John Doe", email="john@example.com")

    # Configure mock repo
    mock_repo.get.return_value = contact_to_update
    mock_repo.list.return_value = [contact_to_update, existing_contact]

    # ACT & ASSERT
    with pytest.raises(ValueError, match="Email already exists."):
        service.update_contact(contact_id=contact_to_update_id, name="Jane Doe", email="john@example.com")

    mock_repo.update.assert_not_called()