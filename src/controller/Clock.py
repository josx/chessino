# -*- encoding: utf-8 -*-
from .Controller import Controller

class Clock(Controller):
    def b1(self):
        print("negras")

    def b2(self):
        print("lee negras")

    def w1(self):
        print("blancas")

    def w2(self):
        print("lee blancas")

    def menu(self):
        self.setController("Menu")