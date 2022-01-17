import pygame.draw_py
from pygame import Surface

from actor import Actor
from event import GameEvents
from no_mans_logic import colors
from no_mans_logic.editor.logic.wire import Wire
from no_mans_logic.editor.model.vector import Vector


class WireView:
    def __init__(self, model: Wire):
        self.model = model
        self.color = colors.blue

    def draw(self, surface: Surface):
        pygame.draw.line(surface, self.color,
                         (self.model.source.x, self.model.source.y),
                         (self.model.target.x, self.model.target.y),
                         width=3)


class Wirecontroller(Actor):
    _uid = 'wire'

    def __init__(self, parent: Actor, model: Wire, view: WireView):
        super(Wirecontroller, self).__init__(parent)
        self.model = model
        self.view = view
        self.placed_source = False
        self.placed_target = False

    def draw(self, surface: Surface):
        self.view.draw(surface)

    @Actor.listen_to(pygame.MOUSEMOTION)
    def on_mouse_move(self, event):
        x, y = event.pos
        self.view.color = colors.blue
        if self.hovers_wire(Vector(x, y)):
            self.view.color = colors.green

        if not self.placed_source:
            self.model.source = Vector(x - (x % 30) + 10, y - (y % 30) + 10)
        if not self.placed_target:
            self.model.target = Vector(x - (x % 30) + 10, y - (y % 30) + 10)

    @Actor.listen_to(pygame.MOUSEBUTTONDOWN, button=1)
    def on_left_click(self, event):
        mouse_position = Vector(*event.pos)
        if not self.placed_source:
            self.placed_source = True
            return
        if not self.placed_target:
            self.placed_target = True
            return

        if not self.hovers_wire(mouse_position):
            return
        if mouse_position.distance_to(self.model.source) < 15:
            self.placed_source = False
            return
        if mouse_position.distance_to(self.model.target) < 15:
            self.placed_target = False

    @Actor.listen_to(pygame.MOUSEBUTTONDOWN, button=3)
    def on_right_click(self, event):
        if self.hovers_wire(Vector(*event.pos)):
            e = pygame.event.Event(GameEvents.DELETE_LOGIC, sender=self, receiver=self.parent)
            pygame.event.post(e)

    def hovers_wire(self, v: Vector):
        to_source = self.model.source - v
        to_target = v - self.model.target
        wire_length = self.model.source.distance_to(self.model.target)
        distance_to_target = v.distance_to(self.model.target)
        distance_to_source = v.distance_to(self.model.source)

        small_angle = abs(to_source.angle_to(to_target)) < 10
        closer_to_target = distance_to_target < wire_length
        closer_to_source = distance_to_source < wire_length

        return small_angle and closer_to_source and closer_to_target and \
               (distance_to_source < 15 or distance_to_target < 15)

    @property
    def uid(self):
        uid = super(Wirecontroller, self).uid
        return f'{uid}/{id(self)}'

    # def __place_source(self, position: Vector):
    #     self.model.source = position
    #     self.placed_source  = True
    #
    # def __place_target(self, position: Vector):
    #     self.model.target = position
    #     self.placed_target = True
