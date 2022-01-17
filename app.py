import pygame
import sys

from actor import Actor
from event import Mailbox
from no_mans_logic import colors
from no_mans_logic.editor.scene import EditorScene


class App(Actor):
    _uid = 'app'

    def __init__(self, width, height):
        super(App, self).__init__(None)
        pygame.init()
        self.width = width
        self.height = height
        self.mailbox = Mailbox()
        self.screen = pygame.display.set_mode((width, height))  # type: pygame.Surface

        self.scene = EditorScene(self, self.screen)

    def start(self):
        while True:
            self.events()
            self.draw()
            pygame.display.flip()

    def events(self):
        self.mailbox.flush_mailbox()
        self.mailbox.fill_mailbox()

        self.receive(self.mailbox)

        self.scene.receive(self.mailbox)

    @Actor.listen_to(pygame.QUIT)
    def quit(self, event):
        pygame.quit()
        sys.exit(0)

    def draw(self):
        self.screen.fill(colors.white)
        self.scene.draw(self.screen)
        # self.grid.draw(self.screen)
        # for actor in self.actors:
        #     actor.draw(self.screen)
