import pytest

from no_mans_logic.editor.logic.button import Button
from no_mans_logic.editor.logic.signal import Signal
from no_mans_logic.editor.model.vector import Vector, up, left, right


@pytest.fixture()
def button():
    return Button(Vector(0, 0), up)


def test_button_is_not_pressed_by_default(button):
    assert not button.is_open
    button.tick([])
    assert not button.is_open


def test_press_opens_the_gate_within_the_button_after_the_next_tick(button):
    button.press()
    assert not button.is_open
    button.update([])
    assert button.is_open


def test_pressed_button_closes_after_two_ticks(button):
    button.press()
    assert not button.is_open
    button.update([])
    assert button.is_open
    button.update([])
    assert not button.is_open


input_signals = [
    Signal(Vector(0, 0) + left),
    Signal(Vector(0, 0) + right),
]


@pytest.mark.parametrize('input_signal', input_signals)
def test_closed_button_blocks_input_signals(button, input_signal):
    assert button.tick([input_signal]) == []


signals = [
    (Signal(Vector(0, 0) + (right * 30), 0), Signal(Vector(0, 0) + (left * 30), 1)),
    (Signal(Vector(0, 0) + (left * 30), 0), Signal(Vector(0, 0) + (right * 30), 1)),
]


@pytest.mark.parametrize('input_signal, output_signal', signals)
def test_open_button_put_input_signals_through(button, input_signal, output_signal):
    button.press()
    button.update([input_signal])
    assert button.tick([input_signal]) == [output_signal]
