from typing import List

import pygame

from no_mans_logic.editor.logic.signal import Signal
from no_mans_logic.editor.model.vector import Vector


class Output:

    def __init__(self, position: Vector, direction: Vector):
        self.position = position
        self.direction = direction
        self.state = 0
        self._images = [
            pygame.image.load('images/output_off.png'),
            pygame.image.load('images/output_on.png')
        ]

    def tick(self, signals: List[Signal]):

        for signal in signals:
            print(f'distance to: {signal.position.distance_to(self.position + (self.direction * 30))}')
            if signal.is_located_at(self.position + (self.direction * 30)):
                print('LIGHT!')
                self.state = 1
                break
        else:
            self.state = 0

    def press(self, *args):
        pass

    @property
    def pos(self):
        return (self.position.x, self.position.y)

    @pos.setter
    def pos(self, pos):
        self.position = Vector(*pos)

    def update(self, signals):
        pass

    def rotate(self, n):
        self.direction = self.direction.rotate_90(n)

    @property
    def image(self):
        return self._images[self.state]
