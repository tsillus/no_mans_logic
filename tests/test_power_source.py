from logic.vector import Vector, down
from model.grid import Grid
from model.logic import PowerSource


def test_power_source__activates__adjacent_grid_coordinate():
    grid = Grid(3, 3)

    power_source = PowerSource(Vector(1, 1), down)
    grid.put(power_source)

    new_grid = power_source.visit(grid, Grid(3, 3))

    assert new_grid.current_at(Vector(1, 2)) == 1
