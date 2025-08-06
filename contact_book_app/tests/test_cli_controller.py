# contact_book_app/tests/test_cli_controller.py
"""Tests for the CLI Controller component."""
import pytest
from unittest.mock import MagicMock, patch

from contact_book_app.domain.model import ContactService
from contact_book_app.presentation.cli_controller import CLIController


@pytest.fixture
def mock_service() -> MagicMock:
    """Provides a mocked service for testing the controller."""
    return MagicMock(spec=ContactService)


def test_controller_calls_add_contact_on_service(mock_service: MagicMock):
    """
    Tests that the controller correctly parses the 'add' command and
    calls the service's add_contact method.
    """
    # ARRANGE
    controller = CLIController(service=mock_service)

    # Simulate user typing: 'add', 'Test User', 'test@example.com', 'exit'
    user_inputs = ['add', 'Test User', 'test@example.com', 'exit']

    # ACT
    with patch('builtins.input', side_effect=user_inputs):
        controller.run()

    # ASSERT
    # Verify that the service's add_contact method was called with the correct arguments
    mock_service.add_contact.assert_called_once_with(name='Test User', email='test@example.com')


def test_controller_calls_list_contacts_on_service(mock_service: MagicMock):
    """
    Tests that the controller calls get_all_contacts when the user lists contacts.
    Note: The 'list' command is implicitly tested because the view refreshes.
    This test ensures the controller itself doesn't need a separate 'list' method.
    When we add a contact, the service notifies the view, which calls get_all_contacts.
    """
    # ARRANGE
    controller = CLIController(service=mock_service)
    user_inputs = ['add', 'Any Name', 'any@email.com', 'exit']

    # ACT
    with patch('builtins.input', side_effect=user_inputs):
        controller.run()

    # ASSERT
    # The view (which is real, not mocked) will be notified after 'add'
    # and will call get_all_contacts.
    assert mock_service.get_all_contacts.called


def test_controller_handles_exit_command(mock_service: MagicMock):
    """
    Tests that the main loop exits when the user types 'exit'.
    """
    # ARRANGE
    controller = CLIController(service=mock_service)
    user_inputs = ['exit']

    # ACT
    with patch('builtins.input', side_effect=user_inputs):
        controller.run()

    # ASSERT
    # If the test finishes without an infinite loop, it has succeeded.
    # We also verify that no core service methods were called.
    mock_service.add_contact.assert_not_called()
    mock_service.delete_contact.assert_not_called()