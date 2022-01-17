import pygame
import pygame.event
import pytest

from conftest import MockActor


def test_mailbox_receives_events(game, mailbox):
    pygame.event.post(pygame.event.Event(pygame.USEREVENT, address='/app', value=1))
    pygame.event.post(pygame.event.Event(pygame.USEREVENT, address='/app/scene', value=2))

    app = MockActor(uid='app')
    scene = MockActor(parent=app, uid='scene')

    mailbox.fill_mailbox()

    app_events = mailbox.get_mailbox(app)
    assert app_events[0].value == 1

    scene_events = mailbox.get_mailbox(scene)
    assert scene_events[0].value == 2
