# contact_book_app/tests/test_contact_service.py
"""Tests for the ContactService domain model."""

import uuid
import pytest
from unittest.mock import MagicMock, ANY
from contact_book_app.domain.repository import AbstractContactRepository, Contact
from contact_book_app.domain.model import ContactService
from contact_book_app.domain.observer import Observer


@pytest.fixture
def mock_repo() -> MagicMock:
    """Provides a mocked repository for testing the service."""
    # Add all methods from the Abstract repo to the mock spec
    # This ensures that calling an unimplemented method on the mock will fail the test
    methods = [func for func in dir(AbstractContactRepository) if
               callable(getattr(AbstractContactRepository, func)) and not func.startswith("__")]
    return MagicMock(spec=AbstractContactRepository, **{method: MagicMock() for method in methods})


@pytest.fixture
def mock_observer() -> MagicMock:
    """Provides a mocked observer for testing notifications."""
    return MagicMock(spec=Observer)


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


def test_service_notifies_observers_on_add(mock_repo: MagicMock, mock_observer: MagicMock):
    """Tests that observers are notified when a contact is added."""
    # ARRANGE
    service = ContactService(repo=mock_repo)
    service.attach(mock_observer)
    mock_repo.list.return_value = []

    # ACT
    service.add_contact(name="Test", email="test@example.com")

    # ASSERT
    mock_observer.update.assert_called_once_with(service)


def test_service_notifies_observers_on_update(mock_repo: MagicMock, mock_observer: MagicMock):
    """Tests that observers are notified when a contact is updated."""
    # ARRANGE
    service = ContactService(repo=mock_repo)
    service.attach(mock_observer)
    contact_id = uuid.uuid4()
    original_contact = Contact(contact_id=contact_id, name="Old", email="old@example.com")
    mock_repo.get.return_value = original_contact

    # ACT
    service.update_contact(contact_id=contact_id, name="New", email="new@example.com")

    # ASSERT
    mock_observer.update.assert_called_once_with(service)


def test_service_notifies_observers_on_delete(mock_repo: MagicMock, mock_observer: MagicMock):
    """Tests that observers are notified when a contact is deleted."""
    # ARRANGE
    service = ContactService(repo=mock_repo)
    service.attach(mock_observer)

    # ACT
    service.delete_contact(contact_id=uuid.uuid4())

    # ASSERT
    mock_observer.update.assert_called_once_with(service)


def test_service_does_not_notify_on_error(mock_repo: MagicMock, mock_observer: MagicMock):
    """Tests that observers are NOT notified if an operation fails."""
    # ARRANGE
    service = ContactService(repo=mock_repo)
    service.attach(mock_observer)

    # ACT & ASSERT
    with pytest.raises(ValueError):
        service.add_contact(name="")

    mock_observer.update.assert_not_called()