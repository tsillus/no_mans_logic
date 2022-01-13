from no_mans_logic.logic.signal import Signal
from no_mans_logic.model.vector import Vector


class PowerSource(object):
    def __init__(self, position, direction):
        """

        :param logic.vector.Vector direction:
        :param logic.vector.Vector position:
        """
        self.position = position
        self.direction = direction

    def tick(self, *args):
        """
        :return: the output Signal
        :rtype: Signal
        """
        return Signal(self.position + self.direction)

    @property
    def pos(self):
        """returns a pygame compatible (x, y) position"""
        return (self.position.x, self.position.y)

    @pos.setter
    def pos(self, pos):
        self.position = Vector(*pos)

    def update(self, signals):
        pass
