from __future__ import annotations
from no_mans_logic.editor.model.vector import Vector


class Signal(object):
    def __init__(self, position: Vector, distance: int = 0):
        self.position = position
        self.distance = distance
        self.ttl = 3

    def __repr__(self):
        return f'<Signal {self.position} {self.distance}>'

    @property
    def uid(self):
        return f'{self.position.x}/{self.position.y}'

    def propagate_to(self, position: Vector):
        return Signal(position, distance=self.distance + 1)

    def is_located_at(self, position: Vector):
        return self.position == position

    def __eq__(self, other: Signal):
        """Two signals are equal when they are at the same place *and* have traveled the same distance."""
        return self.distance == other.distance and self.position == other.position

    def __ne__(self, other: Signal):
        return self.position != other.position or self.distance != other.distance

    def __le__(self, other):
        return self.position == other.position and self.distance < other.distance

    def __ge__(self, other):
        return self.position == other.position and self.distance > other.distance

    def __lt__(self, other):
        return self.distance < other.distance

    def __gt__(self, other):
        return self.distance > other.distance

    def __or__(self, other: Signal):
        return Signal(self.position)

    def update(self, other: Signal):
        if self.is_located_at(other.position):
            if self.distance >= other.distance and other.ttl > self.ttl:
                return other
        self.ttl = max(self.ttl - 1, 0)
        return self
