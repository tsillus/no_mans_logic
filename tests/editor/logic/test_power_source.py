from no_mans_logic.editor.logic.signal import Signal
from no_mans_logic.editor.model.vector import Vector, down
from no_mans_logic.editor.logic.power_source import PowerSource


def test_power_source__activates__adjacent_grid_coordinate():
    power_source = PowerSource(Vector(1, 1), down)
    assert power_source.tick() == Signal(Vector(1, 2))
