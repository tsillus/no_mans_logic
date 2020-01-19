from logic.signal import Signal
from model.vector import Vector, down
from logic.power_source import PowerSource


def test_power_source__activates__adjacent_grid_coordinate():
    power_source = PowerSource(Vector(1, 1), down)
    assert power_source.tick() == Signal(Vector(1, 2))
