import pygame
import pytest

# TODO: right click creates context menu
# TODO: context menu buttons are ordered around the object clicked on
# TODO: context menu buttons send events to object clicked on
from pygame import Surface
from pygame.event import Event

from conftest import MockActor
from event import GameEvents
from no_mans_logic.editor.context_menu.context_button import ContextActions, ContextButtonController
from no_mans_logic.editor.context_menu.context_menu import ContextMenuController, ContextModel, ContextView
from no_mans_logic.editor.gui.button import Button
from no_mans_logic.editor.logic.logic_controller import LogicController
from no_mans_logic.editor.logic.inverter import Inverter
from no_mans_logic.editor.logic.view import LogicView
from no_mans_logic.editor.model.vector import up, Vector


def test_right_click_on_logic_creates_context_menu(game, mailbox):
    gate = Inverter(Vector(10, 10), up)
    logic = LogicController(MockActor(uid='test'), gate, LogicView(gate, Surface((100, 100))))

    pygame.event.post(Event(pygame.MOUSEBUTTONDOWN, pos=(5, 5), button=3))
    mailbox.fill_mailbox()

    assert len(logic.actors.values()) == 0
    logic.receive(mailbox)
    assert len(logic.actors.values()) == 1

    context_menu = [*logic.actors.values()][0]
    assert isinstance(context_menu, ContextMenuController)

    for button in context_menu.actors.values():
        assert isinstance(button, ContextButtonController)
    # else:
    #     pytest.fail('Right click did not create a context menu')
    # ev = pygame.event.Event(pygame.MOUSEBUTTONDOWN, pos=button.model.position.astuple, test='TEST')
    # pygame.event.post(ev)
    #
    # assert len(context_menu.actors.values()) > 0
    #
    # mailbox.flush_mailbox()
    # mailbox.fill_mailbox()
    #
    # event = mailbox.get_global_mailbox()[0]
    # assert event.type == GameEvents.CONTEXT
    #
    # logic.receive(mailbox)


def test_clicking_context_menu_button_sends_CONTEXT_event_to_parent(game, mailbox):
    parent = MockActor(uid='TEST')
    model = ContextModel(Vector(10, 10))
    menu = ContextMenuController(parent, model, ContextView(model))
    menu.spawn_buttons([ContextActions.CANCEL])

    click = pygame.event.Event(pygame.MOUSEBUTTONDOWN, button=1, pos=(11, 75))
    mailbox.fill_mailbox([click])

    menu.receive(mailbox)

    mailbox.flush_mailbox()
    mailbox.fill_mailbox()

    assert len(mailbox.get_mailbox(menu)) == 1
    assert mailbox.get_mailbox(menu)[0].type == GameEvents.CONTEXT


def test_context_menu_removes_context_buttons_after_one_of_them_was_clicked(game, mailbox):
    parent = MockActor(uid='TEST')
    model = ContextModel(Vector(10, 10))
    menu = ContextMenuController(parent, model, ContextView(model))
    menu.spawn_buttons([ContextActions.CANCEL])

    assert menu.actors != {}

    context = pygame.event.Event(GameEvents.CONTEXT, receiver=menu, sender=list(menu.actors.values())[0])
    mailbox.fill_mailbox([context])

    menu.receive(mailbox)

    mailbox.flush_mailbox()
    mailbox.fill_mailbox()

    assert len(mailbox.get_mailbox(parent)) == 1
    assert menu.actors == {}
