import pygame
import pygame.event
from pygame import MOUSEBUTTONDOWN

from event import EventHandler, GameEvents
from no_mans_logic.gui.button import Button


def test_gui_button_fires_event_when_clicked(game):
    button = Button((10, 10), 'button', event_type=GameEvents.CREATE_LOGIC)
    ev = pygame.event.Event(MOUSEBUTTONDOWN, {'pos': (10, 10), 'button': 1})

    button.receive(EventHandler([ev]))

    events = pygame.event.get(GameEvents.CREATE_LOGIC)
    assert len(events) == 1
    assert events[0].type == GameEvents.CREATE_LOGIC
    assert events[0].path == 'button'
    assert events[0].pos == (10, 10)


def test_gui_button_does_not_fire_event_when_not_clicked(game):
    button = Button((10, 10), 'button', event_type=GameEvents.CREATE_LOGIC)
    ev = pygame.event.Event(MOUSEBUTTONDOWN, {'pos': (11, 100), 'button': 1})

    button.receive(EventHandler([ev]))

    events = pygame.event.get(GameEvents.CREATE_LOGIC)
    assert len(events) == 0


def test_gui_button_does_not_fire_when_event_is_not_a_leftclick(game):
    button = Button((10, 10), 'button', event_type=GameEvents.CREATE_LOGIC)
    ev = pygame.event.Event(pygame.USEREVENT, {})

    button.receive(EventHandler([ev]))

    events = pygame.event.get(GameEvents.CREATE_LOGIC)
    assert len(events) == 0
