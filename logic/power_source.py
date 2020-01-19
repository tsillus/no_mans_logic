from logic.signal import Signal


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
