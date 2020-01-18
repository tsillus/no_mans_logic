from logic.vector import Vector


class Signal(object):
    def __init__(self, current: bool, position: Vector):
        self.position = position
        self.current = current
        self.sources = []
        self.targets = []

    def on(self):
        self.current = True

    def off(self):
        self.current = False

    def toggle(self):
        self.current = not self.current

    def __bool__(self):
        return self.current

    def __eq__(self, other):
        return self.current == other.current

    def __or__(self, other):
        return Signal(self.current or other.current, self.position)
