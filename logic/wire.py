from logic.signal import Signal
from model.vector import Vector


class Wire:
    def __init__(self, source: Vector, target: Vector):
        self.source = source
        self.target = target

    def tick(self, signals):
        if Signal(self.source) in signals:
            return [Signal(self.target)]

        if Signal(self.target) in signals:
            return [Signal(self.source)]

        return []
