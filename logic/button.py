from logic.gate import Gate
from model.vector import Vector


class Button(Gate):

    def __init__(self, position: Vector, direction: Vector):
        super().__init__(position, direction)
        self.is_open = False
        self.pressed = 0

    def tick(self, signals):
        if self.pressed > 0:
            self.pressed -= 1
        self.is_open = self.pressed > 0
        output = super(Button, self).tick(signals)

        return output

    def press(self):
        self.pressed = 2

    def move(self, new_position: Vector):
        self.position = new_position

    def rotate(self):
        self.orientation = self.orientation.rotate(1)
