from logic.vector import Vector
from model.grid import Grid


def test_empty_grid__has__x_y_dimensions():
    grid = Grid(3, 4)

    assert len(grid.matrix) == 3
    assert len(grid.matrix[0]) == 4
    assert len(grid.matrix[1]) == 4
    assert len(grid.matrix[2]) == 4


def test_empty_grid__is__off():
    grid = Grid(2, 2)

    assert grid.current_at(Vector(0, 0)) == 0
    assert grid.current_at(Vector(0, 1)) == 0
    assert grid.current_at(Vector(1, 0)) == 0
    assert grid.current_at(Vector(1, 1)) == 0


def test_pulse__activates__current_at_pulse_location():
    grid = Grid(3, 3)

    grid.activate(Vector(1, 1))
    assert grid.current_at(Vector(0, 0)) == 0
    assert grid.current_at(Vector(1, 1)) == 1
