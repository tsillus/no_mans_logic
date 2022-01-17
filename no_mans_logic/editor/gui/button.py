import pygame
from pygame.event import Event
from pygame.rect import Rect
from pygame.surface import Surface

from event import EventFilter, OldEventHandler
from actor import Actor
from no_mans_logic.editor.model.vector import Vector


class Button(Actor):
    def __init__(self, parent: Actor, position: Vector, name, event_type=pygame.USEREVENT, **event_attributes):
        super(Button, self).__init__(parent)
        self.position = position
        self.name = name
        self.event_type = event_type
        self.event_attributes = event_attributes

        self.image = pygame.image.load(f'images/{name}.png')
        self.rect = self.image.get_rect().move(self.position.as_tuple)  # type: Rect

    def draw(self, screen: Surface):
        screen.blit(self.image, self.rect)

    @Actor.listen_to(pygame.MOUSEBUTTONDOWN, button=1)
    def on_click(self, event):
        if self.is_click(event):
            attributes = {
                'path': self.name,
                'pos': event.pos,
                'sender': self,
            }
            attributes.update(self.event_attributes)

            e = Event(self.event_type, **attributes)
            pygame.event.post(e)

    def is_click(self, event):
        return self.rect.collidepoint(*event.pos)

    @property
    def _uid(self):
        return f'button/{id(self)}'
