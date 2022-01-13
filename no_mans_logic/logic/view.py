import pygame.image
from pygame import Rect, Surface

from no_mans_logic.logic.gate import Gate
from no_mans_logic.model import vector


class LogicView:
    def __init__(self, model: Gate, image: Surface):
        self.model = model
        self.image = image
        self.rect = self.image.get_rect()  # type: Rect
        self.rect.center = model.pos

    def draw(self, screen: Surface):
        self.rect.center = self.model.pos
        angle = vector.up.angle_to(self.model.direction)
        image = pygame.transform.rotate(self.image, angle)
        screen.blit(image, self.rect)
