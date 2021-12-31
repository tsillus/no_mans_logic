from abc import ABC, abstractmethod
from typing import List

from no_mans_logic.logic.signal import Signal
from no_mans_logic.logic.wire import Wire
from no_mans_logic.model.vector import Vector


class Gate(ABC):

    def __init__(self, position: Vector, direction: Vector, is_open=True):
        self.direction = direction
        self.position = position
        self.gate = Wire(position + direction.rotate(3), position + direction.rotate(1))
        self.is_open = is_open

    def tick(self, signals: List[Signal]) -> List[Signal]:
        if self.is_open:
            return self.gate.tick(signals)
        return []

    @abstractmethod
    def update(self, signals):
        pass
