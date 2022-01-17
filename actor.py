import pygame


class Actor:
    _uid = ''

    def __init__(self, parent=None):
        """
        :type parent: Actor|None
        """
        self.parent = parent
        self.actors = {}
        self.__listening = {}
        for methodname in dir(self):

            method = getattr(self, methodname)
            if hasattr(method, 'listen_to'):
                method_list = self.__listening.get(str(method.listen_to), [])
                method_list.append(method)
                self.__listening.update({str(method.listen_to): method_list})

    @property
    def uid(self):
        if not self.parent:
            return f'/{self._uid}'
        return f'{self.parent.uid}/{self._uid}'

    @staticmethod
    def listen_to(event_type, **query):
        def listening(f):
            f.listen_to = str(event_type)
            f.query = query
            return f

        return listening

    def receive(self, mailbox):
        """
        :type mailbox: event.Mailbox
        """
        for event in mailbox.get_mailbox(self):
            self.receive_one(event)

        for event in mailbox.get_global_mailbox():
            self.receive_one(event)

        for actor in self.actors.values():
            actor.receive(mailbox)

    def receive_event_handler(self, handler):
        for event_type in self.__listening.keys():
            self.receive(handler.listen(str(event_type)))

    def receive_one(self, event: pygame.event.Event):
        for method in self.__listening.get(str(event.type), []):
            conditions = [event.dict[k] == method.query[k] for k in method.query.keys()]
            if method.query != {} and not all(*[conditions]):
                continue
            method(event)
