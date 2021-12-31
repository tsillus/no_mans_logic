from no_mans_logic.logic.signal import Signal
from no_mans_logic.model.vector import Vector
from no_mans_logic.model.grid import Grid


def test_add_signal_adds_a_signal_to_the_grid():
    grid = Grid(10, 10)
    grid.add_signal(Signal(Vector(2, 3)))

    assert Signal(Vector(2, 3)) in grid.signals


def test_signal_is_only_added_once_per_location_in_the_grid():
    grid = Grid(10, 10)
    grid.add_signal(Signal(Vector(2, 3)))

    assert len(grid.signals) == 1

    grid.add_signal(Signal(Vector(2, 3)))
    assert len(grid.signals) == 1
