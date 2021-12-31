from typing import List

from no_mans_logic.logic.signal import Signal


class Grid(object):
    def __init__(self, width, height):
        self.height = height
        self.width = width
        self.logic = []
        self.signals: List[Signal] = []

    def add_logic_element(self, item):
        self.logic.append(item)

    def add_signal(self, signal: Signal):
        if signal not in self.signals:
            self.signals.append(signal)
