import pygame
import pytest


@pytest.fixture(scope='session')
def game():
    pygame.init()
    yield
    pygame.quit()
