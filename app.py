import pygame, sys

from event import EventHandler, GameEvents
from no_mans_logic.gui import colors

from no_mans_logic.gui.grid import Grid
from no_mans_logic.gui.menu import Menu


class App(object):
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))  # type: pygame.Surface

        self.menu = Menu((10, 10), (75, height - 20))
        self.grid = Grid((100, 10), (width - 110, height - 20), 30)

    def start(self):

        while True:
            self.events()
            self.draw()
            pygame.display.flip()

    def events(self):
        keys_pressed = pygame.key.get_pressed()

        event_handler = EventHandler(pygame.event.get())

        self.menu.listen(event_handler)

        if event_handler.quit():
            pygame.quit()
            sys.exit(0)

        for ev in pygame.event.get():

            self.menu.listen(ev)
            self.grid.listen(ev)

            if ev.type == pygame.QUIT:
                sys.exit(0)

    def draw(self):
        self.screen.fill(colors.white)
        self.menu.draw(self.screen)
        self.grid.draw(self.screen)
