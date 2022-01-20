from no_mans_logic.editor.logic.gate import Gate
from no_mans_logic.editor.logic.signal import Signal
from no_mans_logic.editor.model.vector import Vector


class AutoSwitch(Gate):
    image = 'auto_switch'

    def __init__(self, position: Vector, direction: Vector):
        super().__init__(position, direction)
        self.is_open = False

    def tick(self, signals):
        new_signals = super(AutoSwitch, self).tick(signals)
        self.update(signals)

        print(new_signals)
        return new_signals

    def update(self, signals):
        self.is_open = Signal(self.position + (self.direction * 30)) in signals
