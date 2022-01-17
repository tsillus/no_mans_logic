import pygame.image
from pygame.event import Event

from event import OldEventHandler, GameEvents
from no_mans_logic.editor.logic.factory import LogicFactory
from no_mans_logic.editor.model import vector


def test_logicfactory(pygame_events, game, mailbox):
    factory = LogicFactory()
    mailbox.fill_mailbox(pygame_events)

    factory.receive(mailbox)

    events = pygame.event.get(GameEvents.ADD_LOGIC)
    assert events[0].obj.logic.position == vector.Vector(0, 0)
    assert events[1].obj.logic.position == vector.Vector(10, 10)
