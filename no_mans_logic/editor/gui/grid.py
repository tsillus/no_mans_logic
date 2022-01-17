import pygame
from pygame.rect import Rect
from pygame.surface import Surface

from no_mans_logic import colors


class Grid(object):
    def __init__(self, position, size, grid_size):
        self.left, self.top = self.position = position
        self.width, self.height = self.size = size
        self.grid_size = grid_size

    def draw(self, screen: Surface):
        self._draw_grid(screen)
        self._draw_frame(screen)

    def _draw_grid(self, screen):
        for x in range(0, self.size[0], self.grid_size):
            pygame.draw.line(screen, colors.light_grey, (self.left + x, self.top),
                             (self.left + x, self.top + self.height))
        for y in range(0, self.size[1], self.grid_size):
            pygame.draw.line(screen, colors.light_grey, (self.left, self.top + y),
                             (self.left + self.width, self.top + y))

    def _draw_frame(self, screen):
        pygame.draw.rect(screen, colors.dark_grey, Rect(self.position, self.size), 2)

    def listen(self, event):
        pass
