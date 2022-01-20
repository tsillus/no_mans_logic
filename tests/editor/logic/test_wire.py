from no_mans_logic.editor.logic.signal import Signal
from no_mans_logic.editor.logic.wire import Wire
from no_mans_logic.editor.model.vector import Vector


def test_wire_has_two_coordinates():
    wire = Wire(Vector(0, 0), Vector(2, 0))

    assert wire.target == Vector(2, 0)
    assert wire.source == Vector(0, 0)


def test_wire_propagates_signal_to_target_position():
    wire = Wire(Vector(0, 0), Vector(2, 0))

    signal = wire.tick([Signal(Vector(0, 0))])

    assert signal[0].distance == 1
    assert signal[0].position == Vector(2, 0)


def test_wire_propagates_signal_to_source_position():
    wire = Wire(Vector(0, 0), Vector(2, 0))

    signal = wire.tick([Signal(Vector(2, 0))])

    assert signal[0].distance == 1
    assert signal[0].position == Vector(0, 0)


def test_wire_returns_original_signal_if_signal_position_is_not_on_source_or_target():
    wire = Wire(Vector(0, 0), Vector(2, 0))

    assert wire.tick([Signal(Vector(1, 0))]) == []