from logic.signal import Signal
from logic.vector import Vector, down
from model.logic import PowerSource


def test_power_source__activates__adjacent_grid_coordinate():
    power_source = PowerSource(Vector(1, 1), down)
    assert power_source.tick() == Signal(True, Vector(1, 2))
