from typing import List

import pygame, sys

from event import EventHandler, GameEvents
from listener import Listener
from logic.test_logic_factory import LogicFactory
from no_mans_logic.gui import colors

from no_mans_logic.gui.grid import Grid
from no_mans_logic.gui.menu import Menu


class App(Listener):
    def __init__(self, width, height):
        super(App, self).__init__()
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))  # type: pygame.Surface
        self.factories = [LogicFactory()]  # type: List[Listener]
        self.actors = []  # type: List[Listener]

        self.menu = Menu((10, 10), (75, height - 20))
        self.grid = Grid((100, 10), (width - 110, height - 20), 30)

    def start(self):

        while True:
            self.events()
            self.draw()
            pygame.display.flip()

    def events(self):
        event_handler = EventHandler(pygame.event.get())

        self.receive(event_handler)

        self.menu.listen(event_handler)

        if event_handler.quit():
            pygame.quit()
            sys.exit(0)

        for factory in self.factories:
            factory.receive(event_handler)

        for actor in self.actors:
            actor.receive(event_handler)

    @Listener.to(GameEvents.ADD_LOGIC)
    def add_logic(self, event):
        print(f'adding MVC for {type(event.obj.logic)}')
        self.actors.append(event.obj)

    def draw(self):
        self.screen.fill(colors.white)
        self.menu.draw(self.screen)
        self.grid.draw(self.screen)
        for actor in self.actors:
            actor.draw(self.screen)
