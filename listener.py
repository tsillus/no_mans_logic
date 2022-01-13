import pygame

from event import EventHandler


class Listener:
    def __init__(self):
        self.__listening = {}
        for methodname in dir(self):

            method = getattr(self, methodname)
            if hasattr(method, 'listen_to'):
                method_list = self.__listening.get(str(method.listen_to), [])
                method_list.append(method)
                self.__listening.update({str(method.listen_to): method_list})

    @staticmethod
    def to(event_type, **query):
        def listening(f):
            f.listen_to = str(event_type)
            f.query = query
            return f

        return listening

    def receive(self, events):
        if isinstance(events, EventHandler):
            self.receive_event_handler(events)
            return
        for event in events:
            self.receive_one(event)

    def receive_event_handler(self, handler):
        for event_type in self.__listening.keys():
            self.receive(handler.listen(str(event_type)))

    def receive_one(self, event: pygame.event.Event):
        for method in self.__listening.get(str(event.type), []):
            conditions = [event.dict[k] == method.query[k] for k in method.query.keys()]
            if method.query != {} and not all(*[conditions]):
                continue
            method(event)
