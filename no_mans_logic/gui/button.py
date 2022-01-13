import pygame
from pygame.event import Event
from pygame.rect import Rect
from pygame.surface import Surface

from event import EventFilter, EventHandler
from listener import Listener


class Button(Listener):
    def __init__(self, position, name, event_type=pygame.USEREVENT):
        super(Button, self).__init__()
        self.y, self.x = position
        self.name = name
        self.event_type = event_type

        self.image = pygame.image.load(f'images/{name}.png')
        self.rect = self.image.get_rect().move((self.x, self.y))  # type: Rect

    def draw(self, screen: Surface):
        screen.blit(self.image, self.rect)

    @Listener.to(pygame.MOUSEBUTTONDOWN, button=1)
    def on_click(self, event):
        if self.is_click(event):
            e = Event(self.event_type, {'path': self.name, 'pos': event.pos})
            pygame.event.post(e)

    def is_click(self, event):
        return self.rect.collidepoint(*event.pos)
