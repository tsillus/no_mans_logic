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