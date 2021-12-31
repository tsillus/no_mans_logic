from typing import List

from no_mans_logic.logic.gate import Gate
from no_mans_logic.logic.signal import Signal


class Inverter(Gate):

    def update(self, signals: List[Signal]):
        self.is_open = not (Signal(self.position + self.direction) in signals)
