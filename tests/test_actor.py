import pytest

import event
import pygame

from actor import Actor


class MockActor(Actor):
    """ TestListener to demonstrate how to use the Listener class"""

    @Actor.listen_to(event.GameEvents.TICK)
    def simple_event(self, *args):
        raise Exception('simple_event')

    @Actor.listen_to(event.GameEvents.CREATE_LOGIC, path='create/button')
    def query_event(self, *args):
        raise Exception('query_event')


def test_actor_routes_an_event_to_its_method():
    listener = MockActor()
    with pytest.raises(Exception) as exc:
        listener.receive_one(pygame.event.Event(event.GameEvents.TICK))
    assert str(exc.value) == 'simple_event'

    with pytest.raises(Exception) as exc:
        listener.receive_one(pygame.event.Event(event.GameEvents.TICK, path='doesnt/matter'))
    assert str(exc.value) == 'simple_event'


def test_actor_filters_event_by_query():
    listener = MockActor()
    with pytest.raises(Exception) as exc:
        listener.receive_one(pygame.event.Event(event.GameEvents.CREATE_LOGIC, path='create/button'))
    assert str(exc.value) == 'query_event'

    listener.receive_one(pygame.event.Event(event.GameEvents.CREATE_LOGIC, path='create/auto_switch'))


def test_actor_tree_is_reflected_the_uid():
    father = MockActor()
    father._uid = 'father'
    assert father.uid == '/father'
    son = MockActor(father)
    son._uid = 'son'
    assert son.uid == '/father/son'
