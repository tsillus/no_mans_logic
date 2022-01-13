import pygame
import pygame.event
import pytest

from event import EventFactory, EventHandler, GameEvents


@pytest.fixture(scope='session')
def event_handler(pygame_events):
    return EventHandler(pygame_events)


def test_EventHandler_selects_given_events_by_event_type(event_handler):
    assert len(event_handler.listen(GameEvents.CREATE_LOGIC)) == 2
    assert len(event_handler.listen(GameEvents.TICK)) == 1


def test_EventHandler_selects_given_events_by_attributes(event_handler, pygame_events):
    actual_events = event_handler.listen(GameEvents.CREATE_LOGIC, {'path': lambda v: v == 'automatic_switch'})
    assert len(actual_events) == 1
    assert actual_events == [pygame_events[0]]


def test_EventHandler_special_access_for_key_presses(event_handler, pygame_events):
    assert event_handler.key[str(ord('a'))] == [pygame_events[3]]
    assert event_handler.key[str(ord('b'))] == [pygame_events[4]]


def test_EventHandler_special_access_for_routes(event_handler, pygame_events):
    assert event_handler.path['button'] == [pygame_events[1]]
    assert event_handler.path['automatic_switch'] == [pygame_events[0]]


def test_EventHandler_special_access_for_event_types(event_handler, pygame_events):
    assert event_handler.type[str(pygame.MOUSEBUTTONDOWN)] == [pygame_events[5]]
    assert event_handler.type[str(pygame.MOUSEMOTION)] == [pygame_events[6]]


def test_EventFactory_creates_event():
    factory = EventFactory(GameEvents.CREATE_LOGIC)

    event = factory.create(path='X')

    assert event.type == GameEvents.CREATE_LOGIC
    assert 'path' in event.dict
    assert event.dict['path'] == 'X'
    assert event.path == 'X'


def test_Events_from_EventFactory_have_route_attribute():
    factory = EventFactory(pygame.USEREVENT, route='/default')

    ev1 = factory.create()
    ev2 = factory.create(route='/custom')

    assert ev1.route == '/default'
    assert ev2.route == '/custom'
