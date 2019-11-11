class PowerSource(object):
    def __init__(self, position, direction):
        """

        :param model.grid.Direction direction:
        :param model.grid.Position position:
        """
        self.position = position
        self.direction = direction

    def visit(self, old_grid, new_grid):
        """
        :param model.grid.Grid old_grid:
        :param model.grid.Grid new_grid:

        :return: the modified new Grid
        :rtype: model.grid.Grid
        """
        pos = self.position + self.direction.delta
        new_grid.activate(pos)
        return new_grid