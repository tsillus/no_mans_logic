from model.vector import Vector


class Signal(object):
    def __init__(self, position: Vector, current: bool = True, distance: int = 0):
        self.position = position
        self.current = current
        self.distance = distance

    def propagate_to(self, position: Vector):
        return Signal(position, distance=self.distance + 1)

    def is_located_at(self, position: Vector):
        return self.position == position

    def on(self):
        self.current = True

    def off(self):
        self.current = False

    def toggle(self):
        self.current = not self.current

    def __bool__(self):
        return self.current

    def __eq__(self, other):
        return self.current == other.current and self.position == other.position

    def __or__(self, other):
        return Signal(self.position, self.current or other.current)
