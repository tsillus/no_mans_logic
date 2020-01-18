import math

from logic.vector import Vector


def test_vector_is_created_with_x_y_coordinates():
    vector = Vector(0, 1)
    assert vector.x == 0
    assert vector.y == 1


def test_two_vectors_are_equal_if_x_and_y_coordinates_are_equal():
    assert Vector(1, 0) == Vector(1, 0)
    assert Vector(1, 0) != Vector(0, 1)
    assert Vector(1, 0) != Vector(1, 1)
    assert Vector(1, 0) != Vector(0, 0)


def test_adding_two_vectors_adds_their_x_and_y_coordinates():
    assert Vector(1, 0) + Vector(0, 1) == Vector(1, 1)


def test_subtracting_two_vectors_subtracts_right_xy_values_from_left_xy_values():
    assert Vector(1, 1) - Vector(1, 0) == Vector(0, 1)
    assert Vector(1, 1) - Vector(0, 1) == Vector(1, 0)


def test_rotates_by_90_degree_steps_clockwise_for_positive_values():
    assert Vector(1, 0).rotate(0) == Vector(1, 0)
    assert Vector(1, 0).rotate(1) == Vector(0, 1)
    assert Vector(1, 0).rotate(2) == Vector(-1, 0)
    assert Vector(1, 0).rotate(3) == Vector(0, -1)
    assert Vector(1, 0).rotate(4) == Vector(1, 0)


def test_rotates_by_90_degress_steps_anticlockwise_for_negative_values():
    assert Vector(1, 0).rotate(-1) == Vector(0, -1)


def test_vector_has_length(self):
    assert math.isclose(Vector(1, 1).length, math.sqrt(2))
