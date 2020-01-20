import pytest

from logic.signal import Signal
from model.vector import Vector


def test_two_signals_are_equal_when_their_currents_are_equal():
    assert Signal(Vector(0, 0)) == Signal(Vector(0, 0))
    assert Signal(Vector(0, 0), 0) != Signal(Vector(0, 0), 1)
    assert Signal(Vector(0, 0)) != Signal(Vector(9, 5))


@pytest.mark.parametrize('before, after', [(0, 1), (1, 2), (10, 11)])
def test_a_propagated_signal_has_distance_increased_by_1(before, after):
    signal = Signal(Vector(0, 0), distance=before)

    new_signal = signal.propagate_to(Vector(1, 0))

    assert new_signal.distance == after
