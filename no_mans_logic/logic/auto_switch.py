from no_mans_logic.logic.gate import Gate
from no_mans_logic.logic.signal import Signal
from no_mans_logic.model.vector import Vector


class AutoSwitch(Gate):
    def __init__(self, position: Vector, direction: Vector):
        super().__init__(position, direction)
        self.is_open = False

    def update(self, signals):
        self.is_open = Signal(self.position + self.direction) in signals
