import pygame
from pygame.surface import Surface

from event import GameEvents
from no_mans_logic.gui import colors
from no_mans_logic.gui.button import Button


class Menu:
    def __init__(self, position, size):
        self.top, self.left = position
        self.width, self.height = size
        self.buttons = {
            'auto_switch': Button((self.top + 5, self.left + 5), 'automatic_switch', GameEvents.CREATE_LOGIC),
            'inverter': Button((self.top + 75, self.left + 5), 'inverter', GameEvents.CREATE_LOGIC),
            'button': Button((self.top + 145, self.left + 5), 'button', GameEvents.CREATE_LOGIC),
            'wall_switch': Button((self.top + 215, self.left + 5), 'wall_switch', GameEvents.CREATE_LOGIC),
            'power': Button((self.top + 285, self.left + 5), 'power', GameEvents.CREATE_LOGIC),
            'output': Button((self.top + 355, self.left + 5), 'output_off', GameEvents.CREATE_LOGIC),
            'wire': Button((self.top + 425, self.left + 5), 'wire', GameEvents.CREATE_LOGIC),
        }

    def draw(self, screen: Surface):
        rect = pygame.Rect((self.top, self.left), (self.width, self.height))
        pygame.draw.rect(screen, colors.dark_grey, rect, 2)

        for name, button in self.buttons.items():
            button.draw(screen)

    def listen(self, event_handler):
        for name, button in self.buttons.items():
            button.receive(event_handler)
