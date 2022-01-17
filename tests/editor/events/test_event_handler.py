import pytest
from pygame.event import Event
import pygame

from event import OldEventHandler, GameEvents


@pytest.fixture()
def list_of_events():
    return [
        Event(pygame.MOUSEBUTTONDOWN, button=1, pos=(10, 10)),
        Event(GameEvents.CREATE_LOGIC, route='create/button'),
        Event(GameEvents.CREATE_LOGIC, route='create/auto_switch'),
    ]


def test_event_handler_categorizes_events_by_event_type(list_of_events):
    eh = OldEventHandler(list_of_events)
