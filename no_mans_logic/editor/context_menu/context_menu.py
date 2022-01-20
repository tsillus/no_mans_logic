from dataclasses import dataclass

import pygame.event
from pygame import Surface
from pygame.event import Event

from actor import Actor
from event import GameEvents
from no_mans_logic.editor.context_menu.context_button import ContextButtonFactory
from no_mans_logic.editor.model.vector import Vector


@dataclass
class ContextModel:
    center: Vector


class ContextView:
    def __init__(self, model: ContextModel):
        self.model = model


class ContextMenuController(Actor):
    _uid = 'context_menu'

    def __init__(self, parent, model: ContextModel, view):
        super(ContextMenuController, self).__init__(parent)
        self.model = model
        self.view = view
        self.factory = ContextButtonFactory(self)

    def spawn_buttons(self, actions):

        for button in self.factory.create_many(self.model.center, actions):
            self.actors[button.uid] = button

    def draw(self, screen: Surface):
        for actor in self.actors.values():
            actor.draw(screen)

    @Actor.listen_to(GameEvents.CONTEXT)
    def on_action(self, event: Event):
        attrs = event.dict
        attrs['receiver'] = self.parent
        attrs['sender'] = self
        ev = pygame.event.Event(event.type, **attrs)
        pygame.event.post(ev)
        self.actors = {}
