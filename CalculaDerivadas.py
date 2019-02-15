# -*- coding: utf-8 -*-
from sympy import diff, cos, Symbol, sin, exp, log

#calcula derivadas para o metodo de halley
class CalculaDerivada():

    def getDerivada(self, f):
        x = Symbol('x')
        derivada = diff(f,x)
        return (str)(derivada)
