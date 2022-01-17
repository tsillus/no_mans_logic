from datetime import datetime, timedelta

from pygame import Surface

from actor import Actor
from no_mans_logic.editor.grid import GridController, GridModel, GridView
from no_mans_logic.editor.menu import MenuController, MenuModel, MenuView
from no_mans_logic.editor.model.vector import Vector


class Clock:
    def __init__(self, interval):
        self.last_tick = datetime.now()
        self.interval = interval

    def tick(self):
        now = datetime.now()
        if now - self.last_tick > self.interval:
            print('tik tok')
            self.last_tick = now
            return True
        return False


class EditorScene(Actor):
    _uid = 'editor'

    def __init__(self, parent, screen: Surface):
        super(EditorScene, self).__init__(parent)

        self.screen = screen
        self.clock = Clock(timedelta(seconds=1.0))

        screen_width = screen.get_width()
        screen_height = screen.get_height()
        menu_model = MenuModel(Vector(10, 10), size=Vector(75, screen_width - 20))
        self.menu = MenuController(self, menu_model, MenuView(menu_model))

        grid_model = GridModel(Vector(100, 10), size=Vector(screen_width - 100, screen_height - 20), grid_size=30)
        self.grid = GridController(self, grid_model, GridView(grid_model))

    def receive(self, mailbox):
        super(EditorScene, self).receive(mailbox)
        self.menu.receive(mailbox)
        self.grid.receive(mailbox)

        if self.clock.tick():
            self.grid.send_tick()

    def draw(self, surface: Surface):
        self.menu.draw(surface)
        self.grid.draw(surface)
