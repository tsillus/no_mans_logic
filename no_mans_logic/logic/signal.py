from __future__ import annotations
from no_mans_logic.model.vector import Vector


class Signal(object):
    def __init__(self, position: Vector, distance: int = 0):
        self.position = position
        self.distance = distance

    def propagate_to(self, position: Vector):
        return Signal(position, distance=self.distance + 1)

    def is_located_at(self, position: Vector):
        return self.position == position

    def __eq__(self, other: Signal):
        return self.distance == other.distance and self.position == other.position

    def __or__(self, other: Signal):
        return Signal(self.position)
