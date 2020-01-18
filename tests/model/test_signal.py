from logic.signal import Signal
from model.vector import Vector


def test_two_signals_are_equal_when_their_currents_are_equal():
    assert Signal(True, Vector(0, 0)) == Signal(True, Vector(9, 5))
    assert Signal(False, Vector(0, 0)) == Signal(False, Vector(9, 5))
    assert Signal(True, Vector(0, 0)) != Signal(False, Vector(9, 5))


def test_signals_can_be_switched_on_and_off():
    signal = Signal(False, Vector(0, 0))
    signal.on()
    assert signal == Signal(True, Vector(0, 0))
    signal.off()
    assert signal == Signal(False, Vector(0, 0))


def test_signal_can_be_toggled_on_and_off():
    signal = Signal(False, Vector(0, 0))
    signal.toggle()
    assert signal == Signal(True, Vector(0, 0))
    signal.toggle()
    assert signal == Signal(False, Vector(0, 0))
