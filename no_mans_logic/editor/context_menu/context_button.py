from dataclasses import dataclass, field
from enum import Enum

import pygame
from pygame import Surface

from actor import Actor
from event import GameEvents
from no_mans_logic.editor.model.vector import Vector


class ContextActions(Enum):
    CANCEL = 'cancel'
    DELETE = 'delete'
    ROTATE_RIGHT = 'rotate_right'
    ROTATE_LEFT = 'rotate_left'
    MOVE = 'move'
    # PROPERTIES
    __DEFAULT = 'round_button'

    @classmethod
    def _missing_(cls, value):
        return cls.__DEFAULT


@dataclass
class ContextButtonModel:
    position: Vector
    action: ContextActions = field(default_factory=ContextActions)


class ContextButtonView:
    def __init__(self, model: ContextButtonModel):
        self.model = model
        self.image = self.load_image(model.action)
        self.rect = self.image.get_rect()
        self.rect.center = self.model.position

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def is_clicked_on(self, x, y):
        return self.rect.collidepoint(x, y)

    def load_image(self, name: ContextActions):
        return pygame.image.load(f'images/context_menu/{name.value}.png')


class ContextButtonController(Actor):
    def __init__(self, parent, model, view):
        super(ContextButtonController, self).__init__(parent)
        self.model = model
        self.view = view

    @Actor.listen_to(pygame.MOUSEBUTTONDOWN, button=1)
    def on_click(self, event):
        if self.view.is_clicked_on(*event.pos):
            ev = pygame.event.Event(GameEvents.CONTEXT, receiver=self.parent,
                                    action=self.model.action)
            pygame.event.post(ev)

    def draw(self, screen: Surface):
        self.view.draw(screen)

    @property
    def _uid(self):
        return f'button/{id(self)}'


class ContextButtonFactory:
    def __init__(self, parent):
        self.parent = parent

    def create_one(self, position: Vector, action):
        model = ContextButtonModel(position, action=action)
        view = ContextButtonView(model)
        ctrl = ContextButtonController(self.parent, model, view)
        return ctrl

    def create_many(self, position: Vector, actions):
        offset = Vector(0, 64)

        rotation = 360 / (len(actions) + 1)

        instances = []
        for action in actions:
            button = self.create_one(position + Vector(offset.x, offset.y), action)
            instances.append(button)
            offset = offset.rotate(rotation)

        return instances
