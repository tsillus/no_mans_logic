from typing import List

from no_mans_logic.editor.logic.gate import Gate
from no_mans_logic.editor.logic.signal import Signal


class Inverter(Gate):
    image = 'inverter'

    def update(self, signals: List[Signal]):
        self.is_open = not (Signal(self.position + self.direction) in signals)
