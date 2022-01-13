import pygame

from event import EventFilter
from listener import Listener
from no_mans_logic.logic.gate import Gate
from no_mans_logic.logic.view import LogicView


class LogicController(Listener):
    def __init__(self, logic: Gate, view: LogicView):
        super(LogicController, self).__init__()
        self.logic = logic
        self.view = view
        self.placed = False

    def draw(self, surface):
        self.view.draw(surface)

    @Listener.to(pygame.MOUSEBUTTONDOWN, button=1)
    def on_left_click(self, event):
        if self.view.rect.collidepoint(event.pos):
            self.logic.press()

    @Listener.to(pygame.MOUSEBUTTONDOWN, button=3)
    def on_right_click(self, event):
        if self.view.rect.collidepoint(event.pos):
            self.logic.rotate(1)

    @Listener.to(pygame.MOUSEMOTION)
    def on_drag(self, event):
        if self.placed:
            return
        (x, y) = event.pos
        self.logic.pos = (x - (x % 30) + 10, y - (y % 30) + 10)

    @Listener.to(pygame.MOUSEBUTTONUP, button=1)
    def on_release_click(self, event):
        self.placed = True
