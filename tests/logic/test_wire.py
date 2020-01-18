import unittest

from logic.signal import Signal
from logic.vector import Vector
from logic.wire import Wire


class WireTest(unittest.TestCase):

    def test_wire_has_two_coordinates(self):
        wire = Wire(Vector(0, 0), Vector(2, 0))

        assert wire.target == Vector(2, 0)
        assert wire.source == Vector(0, 0)

    def test_wire_moves_signal_to_target_position(self):
        wire = Wire(Vector(0, 0), Vector(2, 0))

        signal = wire.tick(Signal(True, Vector(0, 0)))

        assert signal.current
        assert signal.position == Vector(2, 0)

    def test_wire_moves_signal_to_source_position(self):
        wire = Wire(Vector(0, 0), Vector(2, 0))

        signal = wire.tick(Signal(True, Vector(2, 0)))

        assert signal.current
        assert signal.position == Vector(0, 0)

    def test_wire_returns_original_signal_if_signal_position_is_not_on_source_or_target(self):
        wire = Wire(Vector(0, 0), Vector(2, 0))

        signal = wire.tick(Signal(True, Vector(1, 0)))

        assert signal.current
        assert signal.position == Vector(1, 0)
