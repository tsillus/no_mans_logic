import pygame

from no_mans_logic.editor.logic.button import Button
from no_mans_logic.editor.logic.logic_controller import LogicController
from no_mans_logic.editor.logic.view import LogicView
from no_mans_logic.editor.model import vector


def test_logic_controller_applies_event(pygame_events, mailbox, game):
    mailbox.fill_mailbox(pygame_events)

    logic_button = Button(vector.Vector(10, 10), vector.up)
    logic_view = LogicView(logic_button, pygame.image.load(f'images/button.png'))
    controller = LogicController(None, logic_button, logic_view)

    assert not logic_button.pressed
    controller.receive(mailbox)
    assert logic_button.pressed
