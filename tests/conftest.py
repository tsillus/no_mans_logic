import pygame
import pytest
from pygame.event import Event
import os

from actor import Actor
from event import GameEvents, Mailbox


@pytest.fixture(scope='session')
def game():
    pygame.init()
    yield
    pygame.quit()


@pytest.fixture()
def mailbox():
    return Mailbox()


@pytest.fixture(scope='session')
def pygame_events():
    return [Event(GameEvents.CREATE_LOGIC, {'path': 'auto_switch', 'pos': (0, 0)}),
            Event(GameEvents.CREATE_LOGIC, {'path': 'button', 'pos': (10, 10)}),
            Event(GameEvents.TICK, {'time': 1}),
            Event(pygame.KEYDOWN, key=pygame.K_a),
            Event(pygame.KEYDOWN, key=pygame.K_b),
            Event(pygame.MOUSEBUTTONDOWN, pos=(10, 10), button=1),
            Event(pygame.MOUSEMOTION, pos=(10, 10)),
            ]


@pytest.fixture(autouse=True)
def change_test_dir(request, monkeypatch):
    test_folder = os.path.join(request.config.rootdir, '..')
    monkeypatch.chdir(test_folder)


class MockActor(Actor):
    def __init__(self, parent=None, uid=''):
        super(MockActor, self).__init__(parent)
        self._uid = uid
