from abc import ABC, abstractmethod
from typing import List

from no_mans_logic.editor.logic.signal import Signal
from no_mans_logic.editor.logic.wire import Wire
from no_mans_logic.editor.model.vector import Vector


class Gate(ABC):
    image = ''

    def __init__(self, position: Vector, direction: Vector, is_open=True):
        self.direction = direction
        self.position = position
        self.gate = Wire(position + direction.rotate_90(3), position + direction.rotate_90(1))
        self.is_open = is_open

    def tick(self, signals: List[Signal]) -> List[Signal]:
        if self.is_open:
            return self.gate.tick(signals)
        return []

    @property
    def pos(self):
        """returns a pygame compatible (x, y) position"""
        return (self.position.x, self.position.y)

    @pos.setter
    def pos(self, pos):
        self.position = Vector(*pos)

    @abstractmethod
    def update(self, signals):
        pass

    def press(self):
        pass

    def rotate(self, n):
        self.direction = self.direction.rotate_90(n)
