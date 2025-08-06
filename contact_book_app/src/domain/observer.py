# contact_book_app/src/domain/observer.py
"""
This module defines the classic Observer design pattern components.
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List, TYPE_CHECKING

# Use a forward reference for the Observable type hint in the Observer
if TYPE_CHECKING:
    from .model import ContactService


class Observer(ABC):
    """
    The Observer interface declares the update method, used by subjects.
    """
    @abstractmethod
    def update(self, subject: ContactService) -> None:
        """Receive update from subject."""
        raise NotImplementedError


class Observable:
    """
    The Observable (or Subject) owns some important state and notifies observers
    when the state changes.
    """

    def __init__(self):
        self._observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        """Attaches an observer to the subject."""
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        """Detaches an observer from the subject."""
        try:
            self._observers.remove(observer)
        except ValueError:
            pass  # Fails silently if observer is not attached

    def notify(self, subject: 'ContactService') -> None:
        """Notify all observers about an event, passing the subject."""
        for observer in self._observers:
            observer.update(subject)