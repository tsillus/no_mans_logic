from logic.gate import Gate
from logic.signal import Signal


class AutoSwitch(Gate):

    def tick(self, signals):
        output = super(AutoSwitch, self).tick(signals)
        self.is_open = Signal(True, self.position + self.direction) in signals
        return output
