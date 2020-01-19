from logic.signal import Signal
from logic.wire import Wire
from model.vector import Vector


class Inverter(object):
    def __init__(self, position: Vector, direction: Vector, is_open=True):
        self.direction = direction
        self.position = position
        self.gate = Wire(position + direction.rotate(3), position + direction.rotate(1))
        self.is_open = is_open

    def tick(self, signals):
        output = []
        if self.is_open:
            output = self.gate.tick(signals)
        self.is_open = not (Signal(True, self.position + self.direction) in signals)
        return output
