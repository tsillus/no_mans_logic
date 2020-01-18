from logic.signal import Signal
from logic.vector import Vector
from model.grid import Grid


def test_add_signal_adds_a_signal_to_the_grid():
    grid = Grid(10, 10)
    grid.add_signal(Signal(True, Vector(2, 3)))

    assert Signal(True, Vector(2, 3)) in grid.signals


def test_signal_is_only_add_once():
    grid = Grid(10, 10)
    grid.add_signal(Signal(True, Vector(2, 3)))

    assert len(grid.signals) == 1

    grid.add_signal(Signal(True, Vector(2, 3)))
    assert len(grid.signals) == 1
