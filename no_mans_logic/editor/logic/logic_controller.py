import pygame

from actor import Actor
from event import GameEvents
from no_mans_logic.editor.context_menu.context_button import ContextActions
from no_mans_logic.editor.context_menu.context_menu import ContextMenuController, ContextModel, ContextView
from no_mans_logic.editor.logic.gate import Gate
from no_mans_logic.editor.logic.view import LogicView


class LogicController(Actor):
    def __init__(self, parent: Actor, logic: Gate, view: LogicView):
        super(LogicController, self).__init__(parent)
        self.logic = logic
        self.view = view
        self.placed = False

    def draw(self, surface):
        self.view.draw(surface)
        for actor in self.actors.values():
            actor.draw(surface)

    @Actor.listen_to(pygame.MOUSEBUTTONDOWN, button=1)
    def on_left_click(self, event):
        if self.view.rect.collidepoint(event.pos):
            self.logic.press()

    @Actor.listen_to(pygame.MOUSEBUTTONDOWN, button=3)
    def on_right_click(self, event):
        if self.view.rect.collidepoint(event.pos):
            model = ContextModel(self.logic.position)
            context_menu = ContextMenuController(self, model, ContextView(model))
            context_menu.spawn_buttons([
                ContextActions.CANCEL, ContextActions.DELETE, ContextActions.ROTATE_LEFT,
                ContextActions.ROTATE_RIGHT, ContextActions.MOVE, ContextActions('properties'),
            ])
            self.actors[context_menu.uid] = context_menu

    @Actor.listen_to(pygame.MOUSEMOTION)
    def on_drag(self, event):
        if self.placed:
            return
        (x, y) = event.pos
        self.logic.pos = (x - (x % 30) + 10, y - (y % 30) + 10)

    @Actor.listen_to(pygame.MOUSEBUTTONUP, button=1)
    def on_release_click(self, event):
        self.placed = True

    @Actor.listen_to(GameEvents.CONTEXT, action=ContextActions.MOVE)
    def on_pickup(self, event):
        self.placed = False
        del self.actors[event.sender.uid]

    @Actor.listen_to(GameEvents.CONTEXT, action=ContextActions.ROTATE_LEFT)
    def on_rotate_left(self, event):
        self.logic.rotate(1)
        del self.actors[event.sender.uid]

    @Actor.listen_to(GameEvents.CONTEXT, action=ContextActions.ROTATE_RIGHT)
    def on_rotate_right(self, event):
        self.logic.rotate(-1)
        del self.actors[event.sender.uid]

    @Actor.listen_to(GameEvents.TICK)
    def on_tick(self, event):
        if not self.placed:
            return
        signal = self.logic.tick(event.signals)
        if signal:
            ev = pygame.event.Event(GameEvents.SIGNAL, signal=signal, receiver=self.parent)
            pygame.event.post(ev)

    @property
    def uid(self):
        uid = super(LogicController, self).uid
        return f'{uid}/{id(self)}'
