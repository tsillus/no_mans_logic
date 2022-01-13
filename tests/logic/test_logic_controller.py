import pygame

from no_mans_logic.logic.button import Button
from no_mans_logic.logic.controller import LogicController
from no_mans_logic.logic.view import LogicView
from no_mans_logic.model import vector
from no_mans_logic.model.vector import Vector


def test_logic_controller_applies_event(pygame_events, game):
    logic_button = Button(vector.Vector(10, 10), vector.up)
    logic_view = LogicView(logic_button, pygame.image.load(f'images/button.png'))
    controller = LogicController(logic_button, logic_view)

    assert not logic_button.pressed
    controller.receive(pygame_events)
    assert logic_button.pressed
