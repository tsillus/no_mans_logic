import pytest

from no_mans_logic.editor.logic.signal import Signal
from no_mans_logic.editor.model.vector import Vector


def test_two_signals_are_equal_when_their_currents_are_equal():
    assert Signal(Vector(0, 0)) == Signal(Vector(0, 0))
    assert Signal(Vector(0, 0), 0) != Signal(Vector(0, 0), 1)
    assert Signal(Vector(0, 0)) != Signal(Vector(9, 5))


def test_a_signal_is_larger_than_the_other_if_they_have_traveled_a_Longer_distance():
    v1 = Vector(0, 0)
    v2 = Vector(1, 1)
    assert Signal(v1, 0) < Signal(v1, 1)
    assert Signal(v2, 0) < Signal(v1, 1)
    assert Signal(v1, 0) < Signal(v2, 1)
    assert Signal(v1, 1) > Signal(v1, 0)
    assert Signal(v2, 1) > Signal(v1, 0)
    assert Signal(v1, 1) > Signal(v2, 0)


@pytest.mark.parametrize('before, after', [(0, 1), (1, 2), (10, 11)])
def test_a_propagated_signal_has_distance_increased_by_1(before, after):
    signal = Signal(Vector(0, 0), distance=before)

    new_signal = signal.propagate_to(Vector(1, 0))

    assert new_signal.distance == after
