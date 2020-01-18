from logic.signal import Signal
from logic.vector import Vector


class Button(object):
    def __init__(self, position: Vector, orientation: Vector):
        """

        :type position: Vector
        :type orientation: Vector
        """
        self.orientation = orientation
        self.position = position
        self.pressed = False
        self.output_signal = Signal(False, self.position + self.orientation)

    @property
    def output(self):
        return self.output_signal

    def tick(self, *args):
        self.output_signal = Signal(self.pressed, self.position + self.orientation)
        self.pressed = False

    def press(self):
        self.pressed = True

    def move(self, new_position: Vector):
        self.position = new_position

    def rotate(self):
        self.orientation = self.orientation.rotate(1)
