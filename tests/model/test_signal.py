import pytest

from logic.signal import Signal
from model.vector import Vector


def test_two_signals_are_equal_when_their_currents_are_equal():
    assert Signal(Vector(0, 0), True) == Signal(Vector(0, 0), True)
    assert Signal(Vector(0, 0), False) == Signal(Vector(0, 0), False)
    assert Signal(Vector(0, 0), True) != Signal(Vector(0, 0), False)
    assert Signal(Vector(0, 0), True) != Signal(Vector(9, 5), True)


def test_signals_can_be_switched_on_and_off():
    signal = Signal(Vector(0, 0), False)
    signal.on()
    assert signal == Signal(Vector(0, 0), True)
    signal.off()
    assert signal == Signal(Vector(0, 0), False)


def test_signal_can_be_toggled_on_and_off():
    signal = Signal(Vector(0, 0), False)
    signal.toggle()
    assert signal == Signal(Vector(0, 0), True)
    signal.toggle()
    assert signal == Signal(Vector(0, 0), False)


@pytest.mark.parametrize('before, after', [(0, 1), (1, 2), (10, 11)])
def test_a_propagated_signal_has_distance_increased_by_1(before, after):
    signal = Signal(Vector(0, 0), distance=before)

    new_signal = signal.propagate_to(Vector(1, 0))

    assert new_signal.distance == after
