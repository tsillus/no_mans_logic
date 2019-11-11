class Grid(object):
    def __init__(self, width, height):
        self.matrix = [[0] * height] * width
        self.items = []

    def current_at(self, pos):
        """
        :param Position pos:
        :return:
        """
        return self.matrix[pos.x][pos.y]

    def activate(self, position):
        """
        :param model.grid.Position position:
        :return:
        """
        self.matrix[position.x][position.y] = 1

    def put(self, item):
        self.items.append(item)


class Position(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Position(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class Direction(object):
    directions = {
        'up': Position(0, -1),
        'down': Position(0, 1),
        'left': Position(-1, 0),
        'right': Position(1, 0),
        'none': Position(0, 0)
    }

    def __init__(self, direction: str):
        self.direction = direction
        self.delta = self.directions.get(direction, Position(0, 0))