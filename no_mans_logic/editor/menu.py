from dataclasses import dataclass

import pygame
from pygame import Surface

from actor import Actor
from event import GameEvents
from no_mans_logic import colors
from no_mans_logic.editor.gui.button import Button
from no_mans_logic.editor.model.vector import Vector


@dataclass
class MenuModel:
    topleft: Vector
    bottomright: Vector = None
    size: Vector = None

    def __post_init__(self):
        if not self.bottomright and not self.size:
            raise ValueError('MenuModel needs at least one of bottomright or size')

        if not self.bottomright:
            self.bottomright = self.topleft + self.size
        elif not self.size:
            self.size = self.bottomright - self.topleft


menu_config = [
    (Vector(5, 5), 'auto_switch', GameEvents.CREATE_LOGIC),
    (Vector(5, 75), 'inverter', GameEvents.CREATE_LOGIC),
    (Vector(5, 145), 'button', GameEvents.CREATE_LOGIC),
    (Vector(5, 215), 'wall_switch', GameEvents.CREATE_LOGIC),
    (Vector(5, 285), 'power', GameEvents.CREATE_LOGIC),
    (Vector(5, 355), 'output', GameEvents.CREATE_LOGIC),
    (Vector(5, 425), 'wire', GameEvents.CREATE_LOGIC),
]


class MenuView:
    def __init__(self, model: MenuModel):
        self.model = model

    def draw(self, screen: Surface):
        rect = pygame.Rect(self.model.topleft.as_tuple, self.model.size.as_tuple)
        pygame.draw.rect(screen, colors.dark_grey, rect, 2)


class MenuController(Actor):
    _uid = 'menu'

    def __init__(self, parent, model: MenuModel, view: MenuView):
        super(MenuController, self).__init__(parent)
        self.model = model
        self.view = view
        self.actors = {}
        self._init_actors(menu_config)

    def draw(self, surface: Surface):
        self.view.draw(surface)
        for actor in self.actors.values():
            actor.draw(surface)

    def _init_actors(self, menu_config):
        for offset, name, event_type in menu_config:
            button = Button(parent=self,
                            position=self.model.topleft + offset,
                            name=name,
                            event_type=event_type,
                            address='/app/editor/grid')
            self.actors.update({button.uid: button})
