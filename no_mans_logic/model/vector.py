from math import sqrt

import pygame


class Vector(pygame.Vector2):
    __slots__ = ['__x', '__y']

    def __init__(self, x, y):
        super(Vector, self).__init__(x, y)
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def rotate(self, steps):
        """
        rotates the vector `steps` times clockwise by 90°
        :return: a new Vector instane
        """
        steps = steps % 4
        if steps == 0:
            return self

        v = Vector(-self.y, self.x).rotate(steps - 1)
        print(v)
        return v

    @property
    def length(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2)

    @property
    def angle(self):
        return up.angle_to(self)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __repr__(self):
        return '<Vector x: {}, y: {}>'.format(self.x, self.y)


up = Vector(0, -1)
down = Vector(0, 1)
left = Vector(-1, 0)
right = Vector(1, 0)
identity = Vector(0, 0)
