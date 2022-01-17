import pygame
import pytest

# TODO: right click creates context menu
# TODO: context menu buttons are ordered around the object clicked on
# TODO: context menu buttons send events to object clicked on
from pygame import Surface
from pygame.event import Event

from conftest import MockActor
from no_mans_logic.editor.logic.logic_controller import LogicController
from no_mans_logic.editor.logic.inverter import Inverter
from no_mans_logic.editor.logic.view import LogicView
from no_mans_logic.editor.model.vector import up, Vector


def test_right_click_on_logic_creates_context_menu(game, mailbox):
    gate = Inverter(Vector(10, 10), up)
    logic = LogicController(MockActor(uid='test'), gate, LogicView(gate, Surface((100, 100))))

    pygame.event.post(Event(pygame.MOUSEBUTTONDOWN, pos=(5, 5), button=3))
    mailbox.fill_mailbox()

    logic.receive(mailbox)

    events = pygame.event.get()
