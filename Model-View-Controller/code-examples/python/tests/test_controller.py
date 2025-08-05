# tests/test_controller.py
"""Unit tests for the Controller component, using mocks."""

import pytest
from unittest.mock import MagicMock
from model import Model        
from view import View           
from controller import Controller 

@pytest.fixture
def mock_model() -> MagicMock:
    """Provides a mock of the Model."""
    return MagicMock(spec=Model)

@pytest.fixture
def mock_view() -> MagicMock:
    """Provides a mock of the View."""
    return MagicMock(spec=View)

@pytest.fixture
def controller(mock_model: MagicMock, mock_view: MagicMock) -> Controller:
    """Provides a Controller instance with mocked dependencies."""
    return Controller(model=mock_model, view=mock_view)

def test_add_item_to_list_successfully(controller: Controller, mock_model: MagicMock, mock_view: MagicMock) -> None:
    """
    Test that the controller correctly calls model and view methods when adding an item.
    """
    # Arrange: Configure the mock model's return value for this test
    mock_model.add_item.return_value = "Success: 'New Task' added."
    mock_model.get_items.return_value = ["New Task"]

    # Act: Call the controller method under test
    controller.add_item_to_list("New Task")

    # Assert: Verify that the correct methods were called on the mocks
    mock_model.add_item.assert_called_once_with("New Task")
    mock_view.display_message.assert_called_once_with("Success: 'New Task' added.")
    mock_model.get_items.assert_called_once()
    mock_view.display_items.assert_called_once_with(["New Task"])

def test_controller_handles_model_error(controller: Controller, mock_model: MagicMock, mock_view: MagicMock) -> None:
    """
    Test that the controller handles a ValueError from the model gracefully.
    """
    # Arrange: Configure the mock model to raise an error
    test_error_message = "Item cannot be empty."
    mock_model.add_item.side_effect = ValueError(test_error_message)

    # Act: Call the controller method
    controller.add_item_to_list("")

    # Assert: Verify that the controller caught the error and showed it to the user
    mock_model.add_item.assert_called_once_with("")
    mock_view.display_message.assert_called_once_with(f"Error: {test_error_message}")
    # Also assert that the view was still updated to show the current state
    mock_view.display_items.assert_called_once()

def test_remove_item_from_list(controller: Controller, mock_model: MagicMock, mock_view: MagicMock) -> None:
    """
    Test that the controller correctly orchestrates the removal of an item.
    """
    # Arrange
    mock_model.remove_item.return_value = "Success: 'Old Task' removed."
    mock_model.get_items.return_value = [] # The list is now empty

    # Act
    controller.remove_item_from_list("Old Task")

    # Assert
    mock_model.remove_item.assert_called_once_with("Old Task")
    mock_view.display_message.assert_called_once_with("Success: 'Old Task' removed.")
    mock_view.display_items.assert_called_once_with([])
