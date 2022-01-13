import pytest

import event
import pygame

from listener import Listener


class MockListener(Listener):
    """ TestListener to demonstrate how to use the Listener class"""

    @Listener.to(event.GameEvents.TICK)
    def simple_event(self, *args):
        raise Exception('simple_event')

    @Listener.to(event.GameEvents.CREATE_LOGIC, path='create/button')
    def query_event(self, *args):
        raise Exception('query_event')


def test_listener_routes_an_event_to_its_method():
    listener = MockListener()
    with pytest.raises(Exception) as exc:
        listener.receive_one(pygame.event.Event(event.GameEvents.TICK))
    assert str(exc.value) == 'simple_event'

    with pytest.raises(Exception) as exc:
        listener.receive_one(pygame.event.Event(event.GameEvents.TICK, path='doesnt/matter'))
    assert str(exc.value) == 'simple_event'


def test_listener_filters_event_by_query():
    listener = MockListener()
    with pytest.raises(Exception) as exc:
        listener.receive_one(pygame.event.Event(event.GameEvents.CREATE_LOGIC, path='create/button'))
    assert str(exc.value) == 'query_event'

    listener.receive_one(pygame.event.Event(event.GameEvents.CREATE_LOGIC, path='create/auto_switch'))
