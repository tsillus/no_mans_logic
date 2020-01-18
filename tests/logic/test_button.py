from logic.button import Button
from model.vector import Vector


def test_button_is_not_pressed_by_default():
    button = Button(Vector(1, 1), Vector(1, 0))
    assert not button.output
    button.tick()
    assert not button.output


def test_press_activates_output_signal_after_update():
    button = Button(Vector(1, 1), Vector(1, 0))
    button.press()
    assert not button.output
    button.tick()
    assert button.output


def test_rotate_turns_button_90_degrees_clockwise():
    button = Button(Vector(1, 1), Vector(1, 0))
    assert button.output.position == Vector(2, 1)
    button.rotate()
    assert button.output.position == Vector(2, 1)
    button.tick()
    assert button.output.position == Vector(1, 2)
