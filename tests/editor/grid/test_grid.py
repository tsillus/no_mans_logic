from no_mans_logic.editor.grid import GridModel, GridView
from no_mans_logic.editor.model.vector import Vector


def test_view_draws_horizontal_lines_with_correct_distance():
    model = GridModel(Vector(0, 0), Vector(100, 100), grid_size=30)
    view = GridView(model)

    h_lines = [*view.horizontal_grid_lines()]

    for i in range(len(h_lines)):
        start, end = h_lines[i]
        assert start.y == i * model.grid_size
        assert start.y == end.y
        assert start.x == model.topleft.x
        assert end.x == model.bottomright.x


def test_view_draws_vertical_lines_with_correct_distance():
    model = GridModel(Vector(0, 0), Vector(100, 100), grid_size=30)
    view = GridView(model)

    v_lines = [*view.vertical_grid_lines()]

    for i in range(len(v_lines)):
        start, end = v_lines[i]
        assert start.x == i * model.grid_size
        assert start.x == end.x
        assert start.y == model.topleft.y
        assert end.y == model.bottomright.y
