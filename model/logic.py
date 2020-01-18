from logic.signal import Signal


class PowerSource(object):
    def __init__(self, position, direction):
        """

        :param logic.vector.Vector direction:
        :param logic.vector.Vector position:
        """
        self.position = position
        self.direction = direction

    def tick(self):
        """
        :return: the output Signal
        :rtype: Signal
        """
        return Signal(True, self.position + self.direction)
