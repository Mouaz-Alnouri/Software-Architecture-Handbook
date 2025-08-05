# tests/test_model.py
"""Unit tests for the Model component."""

import pytest
from ..model import Model

@pytest.fixture
def model() -> Model:
    """Provides a fresh Model instance for each test function."""
    return Model()

def test_initialization(model: Model) -> None:
    """Test that the model initializes with an empty item list."""
    assert model.get_items() == []

def test_add_item_successfully(model: Model) -> None:
    """Test the happy path for adding a new, valid item."""
    result = model.add_item("Buy milk")
    assert "Buy milk" in model.get_items()
    assert result == "Success: 'Buy milk' added."

def test_add_duplicate_item(model: Model) -> None:
    """Test that adding a duplicate item is handled correctly."""
    model.add_item("Buy milk")
    result = model.add_item("Buy milk")  # Add the same item again
    assert len(model.get_items()) == 1  # List should only have one instance
    assert result == "Error: 'Buy milk' is already in the list."

def test_remove_item_successfully(model: Model) -> None:
    """Test the happy path for removing an existing item."""
    model.add_item("Clean room")
    result = model.remove_item("Clean room")
    assert "Clean room" not in model.get_items()
    assert result == "Success: 'Clean room' removed."

def test_remove_non_existent_item(model: Model) -> None:
    """Test that trying to remove an item that doesn't exist is handled."""
    result = model.remove_item("Do laundry")
    assert result == "Error: 'Do laundry' not found."

def test_add_invalid_item_raises_error(model: Model) -> None:
    """Test that adding a non-string or empty item raises a ValueError."""
    with pytest.raises(ValueError, match="Item must be a non-empty string."):
        model.add_item("")  # Test with empty string
    with pytest.raises(ValueError):
        model.add_item(123)  # Test with non-string
