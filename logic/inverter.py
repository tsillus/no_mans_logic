from typing import List

from logic.gate import Gate
from logic.signal import Signal


class Inverter(Gate):

    def tick(self, signals: List[Signal]):
        output = super(Inverter, self).tick(signals)
        self.is_open = not (Signal(True, self.position + self.direction) in signals)
        return output
