from dataclasses import dataclass, field
from typing import List, Tuple

import pygame
from pygame import Surface

from actor import Actor
from event import GameEvents
from no_mans_logic import colors
from no_mans_logic.editor.logic.factory import LogicFactory
from no_mans_logic.editor.model.vector import Vector
from no_mans_logic.model import Model


@dataclass
class GridModel(Model):
    grid_size: int = 30
    offset = Vector(0, 0)

    logic: List[Actor] = field(default_factory=list)


class GridView:
    def __init__(self, model: GridModel):
        self.model = model
        self.line_color = colors.light_grey

    def draw(self, screen: Surface):
        for top_left, bottom_right in self.horizontal_grid_lines():
            pygame.draw.line(screen, self.line_color, top_left, bottom_right)

        for top_left, bottom_right in self.vertical_grid_lines():
            pygame.draw.line(screen, self.line_color, top_left, bottom_right)

    def horizontal_grid_lines(self) -> Tuple[Vector, Vector]:
        for y in range(0, self.model.size.y, self.model.grid_size):
            start = self.model.topleft + Vector(0, y)
            end = start + Vector(self.model.bottomright.x, 0)
            yield start, end

    def vertical_grid_lines(self):
        for x in range(0, self.model.size.x, self.model.grid_size):
            start = self.model.topleft + Vector(x, 0)
            end = start + Vector(0, self.model.bottomright.y)
            yield start, end


class GridController(Actor):
    _uid = 'grid'

    def __init__(self, parent: Actor, model: GridModel, view: GridView):
        super(GridController, self).__init__(parent)
        self.model = model
        self.view = view
        self.logic_factory = LogicFactory(self)
        self.signals = {}

    def draw(self, screen: Surface):
        self.view.draw(screen)
        for actor in self.actors.values():
            actor.draw(screen)

    def send_tick(self):
        event = pygame.event.Event(GameEvents.TICK, signals=[*self.signals.values()])
        pygame.event.post(event)

    @Actor.listen_to(GameEvents.CREATE_LOGIC)
    def create_logic(self, event):
        self.logic_factory.receive_one(event)

    @Actor.listen_to(GameEvents.ADD_LOGIC)
    def add_logic(self, event):
        actor = event.obj
        self.actors.update({actor.uid: actor})

    @Actor.listen_to(GameEvents.DELETE_LOGIC)
    def delete_logic(self, event):
        print(f'deleting {event.sender} at {event.sender.uid}')
        del self.actors[event.sender.uid]

    @Actor.listen_to(GameEvents.SIGNAL)
    def on_signal(self, event):
        print(f'Signal at {event.signal.uid}')
        signal = self.signals.get(event.signal.uid, None)
        if signal is None:
            self.signals[event.signal.uid] = event.signal
            return
        self.signals.update({signal.uid: signal.update(event.signal)})
