import pytest

from logic.inverter import Inverter
from logic.signal import Signal
from model.vector import Vector, up, left, right


@pytest.fixture()
def inverter():
    return Inverter(Vector(0, 0), up)


def test_wires_left_and_right_from_the_direction(inverter):
    assert inverter.gate.source == inverter.position + left
    assert inverter.gate.target == inverter.position + right


def test_inverter__closes__when__a_signal__is_at_the_control_input(inverter):
    inverter.is_open = True

    inverter.update([Signal(inverter.position + up)])

    assert not inverter.is_open


def test_inverter__opens__when__no_signal__is_at_the_control_input(inverter):
    inverter.is_open = False

    inverter.update([])

    assert inverter.is_open


def test_an_open_inverter_puts_a_signal_from_one_side_to_the_other(inverter):
    inverter.is_open = True
    assert inverter.tick([Signal(inverter.position + left, 0)]) == [Signal(inverter.position + right, 1)]
    assert inverter.tick([Signal(inverter.position + right, 0)]) == [Signal(inverter.position + left, 1)]


def test_a_closed_inverter_returns_no_signal(inverter):
    inverter.is_open = False
    signal_left = Signal(inverter.position + left)
    signal_right = Signal(inverter.position + right)
    signal_up = Signal(inverter.position + up)

    assert inverter.tick([signal_up, signal_left]) == []
    assert inverter.tick([signal_up, signal_right]) == []
