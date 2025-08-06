# contact_book_app/tests/test_cli_view.py
"""Tests for the CLI View component."""
import uuid
import pytest
from unittest.mock import MagicMock
from contact_book_app.domain.model import ContactService
from contact_book_app.domain.repository import Contact
from contact_book_app.presentation.cli_view import CLIView


@pytest.fixture
def mock_service() -> MagicMock:
    """Provides a mocked service for testing the view."""
    return MagicMock(spec=ContactService)


def test_display_contacts_shows_correct_output(mock_service: MagicMock, capsys):
    """
    Tests that the view correctly formats and prints a list of contacts.
    """
    # ARRANGE
    # Create some sample contacts
    contacts = [
        Contact(contact_id=uuid.uuid4(), name="Alice", email="alice@example.com"),
        Contact(contact_id=uuid.uuid4(), name="Bob", email="bob@example.com")
    ]
    # Configure the mock service to return our sample contacts
    mock_service.get_all_contacts.return_value = contacts

    view = CLIView(service=mock_service)

    # ACT
    view.display_contacts()

    # ASSERT
    captured = capsys.readouterr()
    output = captured.out

    assert "Contact Book" in output
    assert "Alice" in output
    assert "alice@example.com" in output
    assert "Bob" in output
    assert "bob@example.com" in output


def test_view_updates_on_notification(mock_service: MagicMock, capsys):
    """
    Tests that the view calls display_contacts when it receives an update notification.
    """
    # ARRANGE
    contacts = [Contact(contact_id=uuid.uuid4(), name="Charlie", email=None)]
    mock_service.get_all_contacts.return_value = contacts
    view = CLIView(service=mock_service)

    # ACT
    # Directly call the update method, simulating a notification from the service
    view.update(subject=mock_service)

    # ASSERT
    # Verify that the view fetched the latest data to display it
    mock_service.get_all_contacts.assert_called_once()

    # Verify that the output was rendered
    captured = capsys.readouterr()
    output = captured.out
    assert "Charlie" in output