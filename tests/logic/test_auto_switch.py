import pytest

from logic.auto_switch import AutoSwitch
from logic.signal import Signal
from model.vector import Vector, up, left, right


@pytest.fixture()
def auto_switch():
    return AutoSwitch(Vector(0, 0), up)


def test_wires_left_and_right_from_the_direction(auto_switch):
    assert auto_switch.gate.source == auto_switch.position + left
    assert auto_switch.gate.target == auto_switch.position + right


def test_auto_switch__opens__when__a_signal__is_at_the_control_input(auto_switch):
    auto_switch.is_open = False

    auto_switch.tick([Signal(True, auto_switch.position + up)])

    assert auto_switch.is_open


def test_inverter__closes__when__no_signal__is_at_the_control_input(auto_switch):
    auto_switch.is_open = True

    auto_switch.tick([])

    assert not auto_switch.is_open


def test_tick_always_returns_no_signal_when_control_input_is_off(auto_switch):
    assert auto_switch.tick([Signal(True, auto_switch.position + left)]) == []
    assert not auto_switch.is_open


def test_signal_on_control_input_opens_gate():
    position = Vector(0, 0)
    direction = up
    signals = [Signal(True, position + left), Signal(True, position + up)]
    auto_switch = AutoSwitch(position, direction)

    assert not auto_switch.is_open

    assert auto_switch.tick(signals) == []
    assert auto_switch.is_open

    assert auto_switch.tick(signals) == [Signal(True, position + right)]
    assert auto_switch.tick([Signal(True, position + left)]) == [Signal(True, position + right)]
    assert not auto_switch.is_open

    assert auto_switch.tick([Signal(True, position + left)]) == []
