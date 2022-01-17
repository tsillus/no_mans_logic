import pygame.event
import pygame.image
from pygame.event import Event

from actor import Actor
from event import GameEvents
from no_mans_logic.editor.logic.auto_switch import AutoSwitch
from no_mans_logic.editor.logic.button import Button
from no_mans_logic.editor.logic.logic_controller import LogicController
from no_mans_logic.editor.logic.inverter import Inverter
from no_mans_logic.editor.logic.output import Output
from no_mans_logic.editor.logic.power_source import PowerSource
from no_mans_logic.editor.logic.view import LogicView
from no_mans_logic.editor.logic.wire import Wire
from no_mans_logic.editor.logic.wire_controller import Wirecontroller, WireView
from no_mans_logic.editor.model import vector


class LogicFactory(Actor):
    _uid = 'logic_factory'

    path = {
        'button': Button,
        'auto_switch': AutoSwitch,
        'inverter': Inverter,
        'power': PowerSource,
        'wire': Wire,
        'output': Output
    }

    @Actor.listen_to(GameEvents.CREATE_LOGIC, path='button')
    def create_button(self, event):
        logic = Button(vector.Vector(*event.pos), vector.down)
        self.create_logic(event, logic)

    @Actor.listen_to(GameEvents.CREATE_LOGIC, path='auto_switch')
    def create_switch(self, event):
        logic = AutoSwitch(vector.Vector(*event.pos), vector.down)
        self.create_logic(event, logic)

    @Actor.listen_to(GameEvents.CREATE_LOGIC, path='inverter')
    def create_inverter(self, event):
        logic = Inverter(vector.Vector(*event.pos), vector.down)
        self.create_logic(event, logic)

    @Actor.listen_to(GameEvents.CREATE_LOGIC, path='power')
    def create_power(self, event):
        logic = PowerSource(vector.Vector(*event.pos), vector.down)
        self.create_logic(event, logic)

    @Actor.listen_to(GameEvents.CREATE_LOGIC, path='wire')
    def create_wire(self, event):
        source = vector.Vector(*event.pos)
        logic = Wire(source, source)
        view = WireView(logic)
        ctrl = Wirecontroller(self.parent, logic, view)
        ev = Event(GameEvents.ADD_LOGIC, obj=ctrl)
        pygame.event.post(ev)
        # self.create_logic(event, logic)

    @Actor.listen_to(GameEvents.CREATE_LOGIC, path='output')
    def create_output(self, event):
        logic = Output(vector.Vector(*event.pos), vector.down)
        self.create_logic(event, logic)

    def create_logic(self, event, logic):
        if isinstance(logic.image, str):
            image = pygame.image.load(f'images/{logic.image}.png')
        else:
            image = logic.image
        view = LogicView(logic, image)
        controller = LogicController(self.parent, logic, view)
        e = Event(GameEvents.ADD_LOGIC, obj=controller)
        pygame.event.post(e)
