from logic.signal import Signal


class Wire:
    def __init__(self, source, target):
        self.source = source
        self.target = target

    def tick(self, signal):
        if signal.position == self.source:
            return Signal(signal.current, self.target)

        if signal.position == self.target:
            return Signal(signal.current, self.source)

        return signal
