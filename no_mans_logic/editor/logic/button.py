from no_mans_logic.editor.logic.gate import Gate
from no_mans_logic.editor.model.vector import Vector


class Button(Gate):
    image = 'button'

    def __init__(self, position: Vector, direction: Vector):
        super().__init__(position, direction)
        self.is_open = False
        self.pressed = 0

    def update(self, signals):
        self.is_open = self.pressed
        if self.pressed:
            self.pressed = False

    def press(self):
        self.pressed = True

    def move(self, new_position: Vector):
        self.position = new_position

    def rotate(self, n):
        self.direction = self.direction.rotate_90(n)
