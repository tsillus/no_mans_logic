import pygame
from pygame.event import Event
from pygame.rect import Rect
from pygame.surface import Surface

from event import EventFilter, EventHandler


class Button(object):
    def __init__(self, position, name, event_type=pygame.USEREVENT):
        self.y, self.x = position
        self.name = name
        self.event_type = event_type

        self.image = pygame.image.load(f'images/{name}.png')
        self.rect = self.image.get_rect().move((self.x, self.y))  # type: Rect

    def draw(self, screen: Surface):
        screen.blit(self.image, self.rect)

    def listen(self, event_handler: EventHandler):
        """
        :param pygame.event.Event event:
        :return:
        """
        for event in event_handler.listen(*EventFilter.LEFT_CLICK):
            if self.is_click(event):
                e = Event(self.event_type, {'path': f'create/{self.name}', 'pos': event.pos})
                pygame.event.post(e)

    def is_click(self, event):
        return self.rect.collidepoint(*event.pos)
