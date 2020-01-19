from logic.signal import Signal
from model.vector import Vector


class Wire:
    def __init__(self, source: Vector, target: Vector):
        self.source = source
        self.target = target

    def tick(self, signals):
        if Signal(True, self.source) in signals:
            return [Signal(True, self.target)]

        if Signal(True, self.target) in signals:
            return [Signal(True, self.source)]

        return []
