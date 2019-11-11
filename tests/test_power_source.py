from model.grid import Grid, Position, Direction
from model.logic import PowerSource


def test_power_source__activates__adjacent_grid_coordinate():
    grid = Grid(3, 3)

    power_source = PowerSource(Position(1, 1), Direction('down'))
    grid.put(power_source)

    new_grid = power_source.visit(grid, Grid(3,3))

    assert new_grid.current_at(Position(1,2)) == 1