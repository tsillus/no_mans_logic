from typing import List

import pygame
import pygame.event


class GameEvents:
    CREATE_LOGIC = pygame.event.custom_type()
    ADD_LOGIC = pygame.event.custom_type()
    PLACE_LOGIC = pygame.event.custom_type()
    TICK = pygame.event.custom_type()


class EventFilter:
    """Presets to use with EventHandler().listen().

    e.g.:
    events = event_handler.listen(*EventFilter.LEFT_CLICK)
    """
    LEFT_CLICK = (pygame.MOUSEBUTTONDOWN, {'button': lambda b: b == 1})
    MIDDLE_CLICK = (pygame.MOUSEBUTTONDOWN, {'button': lambda b: b == 1})
    RIGHT_CLICK = (pygame.MOUSEBUTTONDOWN, {'button': lambda b: b == 3})


class EventHandler:
    """Organizes a list of events so they can be accessed efficiently"""
    def __init__(self, events: List[pygame.event.Event]):
        self.events = events
        self.type = self.__by_event_type(events)
        self.path = self.__by_path(events)
        self.key = self.__by_key(events)

    def __by_key(self, events):
        key = {}
        for ev in events:
            if hasattr(ev, 'key') and ev.key:
                char = str(ev.key)
                k = key.get(char, [])
                k.append(ev)
                key[char] = k
        return key

    def __by_event_type(self, events):
        ev_type = {}
        for ev in events:
            event_list = ev_type.get(str(ev.type), [])
            event_list.append(ev)
            ev_type.update({str(ev.type): event_list})
        return ev_type

    def __by_path(self, events):
        routes = {}
        for ev in events:
            if hasattr(ev, 'path'):
                route = routes.get(ev.path, [])
                route.append(ev)
                routes[ev.path] = route
        return routes

    def quit(self):
        return str(pygame.QUIT) in self.type

    def listen(self, type, filter=None):
        type = str(type)
        if filter is None:
            filter = {}
        result = []
        for event in self.type.get(type, []):
            if self._matches(event, filter):
                result.append(event)
        return result

    def _matches(self, event, filters):
        for key, f in filters.items():
            if not f(getattr(event, key)):
                return False
        return True


class EventFactory:
    def __init__(self, event_type, route=''):
        self.event_type = event_type
        self.route = route

    def create(self, **attributes):
        if 'route' not in attributes:
            attributes.update({'route': self.route})
        return pygame.event.Event(self.event_type, attributes)
