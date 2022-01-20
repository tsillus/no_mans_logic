import pytest

from no_mans_logic.editor.logic.auto_switch import AutoSwitch
from no_mans_logic.editor.logic.signal import Signal
from no_mans_logic.editor.model.vector import left, right, up, Vector


@pytest.fixture()
def auto_switch():
    return AutoSwitch(Vector(0, 0), up)


def test_wires_left_and_right_from_the_direction(auto_switch):
    assert auto_switch.gate.source == auto_switch.position + (left * 30)
    assert auto_switch.gate.target == auto_switch.position + (right * 30)


def test_auto_switch__opens__when__a_signal__is_at_the_control_input(auto_switch):
    auto_switch.is_open = False
    auto_switch.update([Signal(auto_switch.position + (up * 30))])
    assert auto_switch.is_open


def test_inverter__closes__when__no_signal__is_at_the_control_input(auto_switch):
    auto_switch.is_open = True
    auto_switch.update([])
    assert not auto_switch.is_open


def test_tick_always_returns_no_signal_when_control_input_is_off(auto_switch):
    assert auto_switch.tick([Signal(auto_switch.position + left)]) == []
    assert not auto_switch.is_open


def test_signal_on_control_input_opens_gate(auto_switch):
    position = auto_switch.position

    assert auto_switch.tick([Signal(position + (left))]) == []
    assert auto_switch.tick([Signal(position + (right * 30))]) == []

    auto_switch.update([Signal(position + (up * 30))])
    assert auto_switch.tick([Signal(position + (left * 30), 0)]) == [Signal(position + (right * 30), 1)]

    auto_switch.update([Signal(position + (up * 30))])
    assert auto_switch.tick([Signal(position + (right * 30), 0)]) == [Signal(position + (left * 30), 1)]

    auto_switch.update([Signal(position + (up * 30))])

    assert str(auto_switch.tick([
        Signal(position + (right * 30), 0),
        Signal(position + (left * 30), 1)])) == str([Signal(position + (left * 30), 1)])