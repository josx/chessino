# -*- encoding: utf-8 -*-
from .MenuItem import MenuItem

class Reset(MenuItem):
    def start(self):
        self.audio = "reiniciar-tiempos"
        self.label = 'reiniciar tiemp'

    def back(self):
        pass

    def next(self):
        pass
