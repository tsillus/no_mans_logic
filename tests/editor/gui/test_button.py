import pygame
import pygame.event
from pygame import MOUSEBUTTONDOWN

from event import OldEventHandler, GameEvents
from no_mans_logic.editor.gui.button import Button
from no_mans_logic.editor.model.vector import Vector


def test_gui_button_fires_event_when_clicked(game):
    button = Button(None, Vector(10, 10), 'button', event_type=GameEvents.CREATE_LOGIC)
    ev = pygame.event.Event(MOUSEBUTTONDOWN, {'pos': (10, 10), 'button': 1})

    button.receive_one(ev)

    events = pygame.event.get(GameEvents.CREATE_LOGIC)
    assert len(events) == 1
    assert events[0].type == GameEvents.CREATE_LOGIC
    assert events[0].path == 'button'
    assert events[0].pos == (10, 10)


def test_gui_button_does_not_fire_event_when_not_clicked(game):
    button = Button(None, Vector(10, 10), 'button', event_type=GameEvents.CREATE_LOGIC)
    ev = pygame.event.Event(MOUSEBUTTONDOWN, {'pos': (11, 100), 'button': 1})

    button.receive_one(ev)

    events = pygame.event.get(GameEvents.CREATE_LOGIC)
    assert len(events) == 0


def test_gui_button_does_not_fire_when_event_is_not_a_leftclick(game):
    button = Button(None, Vector(10, 10), 'button', event_type=GameEvents.CREATE_LOGIC)
    ev = pygame.event.Event(pygame.USEREVENT, {})

    button.receive_one(ev)

    events = pygame.event.get(GameEvents.CREATE_LOGIC)
    assert len(events) == 0
