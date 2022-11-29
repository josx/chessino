# -*- encoding: utf-8 -*-
from time import time

class Clock():
    def __init__(self, engine):
        self.engine = engine
        self.active = False
        self.time = 0 # tiempo de la activación.

    def setActive(self, status):
        self.active = status
        if status:
            self.engine.log("Reloj activo")
            self.time = self.getTime()
        else:
            self.engine.log("Reloj pausado")
            self.time=0

    def getTime(self):
        return int(time())

    def tick(self):
        current = self.getTime()
        if self.active and self.time < current:
            s = current - self.time
            self.time = current
            if self.engine.data['white-turn']:
                value = self.engine.data['white']-s
                self.engine.data['white'] = value
            else:
                value = self.engine.data['black']-s
                self.engine.data['black'] = value
            # todo: agregar validaciones para que nunca el tiempo sea valores negativos.
            if value == 0:
                self.finish()
            else:
                self.alarm(value)

    def alarm(self, value):
        pass

    def finish(self):
        self.setActive(False)
        print("finalizado")