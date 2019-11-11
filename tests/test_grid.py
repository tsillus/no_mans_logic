from model.grid import Grid, Position, Direction


def test_empty_grid__has__x_y_dimensions():
    grid = Grid(3, 4)

    assert len(grid.matrix) == 3
    assert len(grid.matrix[0]) == 4
    assert len(grid.matrix[1]) == 4
    assert len(grid.matrix[2]) == 4


def test_empty_grid__is__off():
    grid = Grid(2, 2)

    assert grid.current_at(Position(0, 0)) == 0
    assert grid.current_at(Position(0, 1)) == 0
    assert grid.current_at(Position(1, 0)) == 0
    assert grid.current_at(Position(1, 1)) == 0


def test_pulse__activates__current_at_pulse_location():
    grid = Grid(3, 3)

    grid.activate(Position(1, 1))
    assert grid.current_at(Position(0, 0)) == 0
    assert grid.current_at(Position(1, 1)) == 1


def test_direction__is_determined__by_name():
    up = Direction('up')
    assert up.delta == Position(0, -1)

