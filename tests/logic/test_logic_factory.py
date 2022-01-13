import pygame.image
import pytest
from pygame.event import Event

from event import EventHandler, GameEvents
from listener import Listener
from no_mans_logic.logic.auto_switch import AutoSwitch
from no_mans_logic.logic.button import Button
from no_mans_logic.logic.controller import LogicController
from no_mans_logic.logic.inverter import Inverter
from no_mans_logic.logic.power_source import PowerSource
from no_mans_logic.logic.view import LogicView
from no_mans_logic.logic.wire import Wire
from no_mans_logic.model import vector


class LogicFactory(Listener):
    path = {
        'button': Button,
        'automatic_switch': AutoSwitch,
        'inverter': Inverter,
        'power': PowerSource,
        'wire': Wire
    }

    @Listener.to(GameEvents.CREATE_LOGIC, path='button')
    def create_button(self, event):
        logic = Button(vector.Vector(*event.pos), vector.up)
        self.create_logic(event, logic)

    @Listener.to(GameEvents.CREATE_LOGIC, path='automatic_switch')
    def create_switch(self, event):
        logic = AutoSwitch(vector.Vector(*event.pos), vector.up)
        self.create_logic(event, logic)

    @Listener.to(GameEvents.CREATE_LOGIC, path='inverter')
    def create_inverter(self, event):
        logic = Inverter(vector.Vector(*event.pos), vector.up)
        self.create_logic(event, logic)

    @Listener.to(GameEvents.CREATE_LOGIC, path='power')
    def create_power(self, event):
        logic = PowerSource(vector.Vector(*event.pos), vector.up)
        self.create_logic(event, logic)

    @Listener.to(GameEvents.CREATE_LOGIC, path='wire')
    def create_wire(self, event):
        source = vector.Vector(*event.pos)
        logic = Wire(source, source + vector.right)
        self.create_logic(event, logic)

    def create_logic(self, event, logic):
        view = LogicView(logic, pygame.image.load(f'images/{event.path}.png'))
        controller = LogicController(logic, view)
        e = Event(GameEvents.ADD_LOGIC, obj=controller)
        pygame.event.post(e)


def test_logicfactory(pygame_events, game):
    factory = LogicFactory()

    factory.receive(EventHandler(pygame_events))

    events = pygame.event.get(GameEvents.ADD_LOGIC)
    assert events[0].obj.logic.position == vector.Vector(0, 0)
    assert events[1].obj.logic.position == vector.Vector(10, 10)
