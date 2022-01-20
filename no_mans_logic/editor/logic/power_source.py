import pygame.image

from no_mans_logic.editor.logic.signal import Signal
from no_mans_logic.editor.model.vector import Vector


class PowerSource(object):
    # image = 'power'

    def __init__(self, position, direction):
        """

        :param logic.vector.Vector direction:
        :param logic.vector.Vector position:
        """
        self.position = position
        self.direction = direction
        self.image = pygame.image.load('images/power.png')

    def tick(self, *args):
        """
        :return: the output Signal
        :rtype: Signal
        """
        return [Signal(self.position + (self.direction * 30))]

    @property
    def pos(self):
        """returns a pygame compatible (x, y) position"""
        return (self.position.x, self.position.y)

    @pos.setter
    def pos(self, pos):
        self.position = Vector(*pos)

    def update(self, signals):
        pass

    def rotate(self, n):
        self.direction = self.direction.rotate_90(n)

    def press(self):
        pass
