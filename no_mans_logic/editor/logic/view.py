import pygame.image
from pygame import Rect, Surface

from no_mans_logic.editor.logic.gate import Gate
from no_mans_logic.editor.model import vector


class LogicView:
    def __init__(self, model: Gate, image: Surface):
        self.model = model
        self.image = image
        self.rect = self.image.get_rect()  # type: Rect
        self.rect.center = model.pos

    def draw(self, screen: Surface):
        if hasattr(self.model, 'image') and isinstance(self.model.image, Surface):
            self.image = self.model.image
        self.rect.center = self.model.pos
        angle = vector.down.angle_to(self.model.direction)
        image = pygame.transform.rotate(self.image, angle)
        screen.blit(image, self.rect)
