from typing import List

from logic.gate import Gate
from logic.signal import Signal


class Inverter(Gate):

    def update(self, signals: List[Signal]):
        self.is_open = not (Signal(self.position + self.direction) in signals)
