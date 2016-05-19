# -*- coding: utf-8 -*-
__author__ = 'Enzo Ahumada'

from persona import Persona

class Garzon(Persona):

    def __init__(self, idegar, nombre, horas):
        Persona.__init__(self, idegar, nombre)
        self.horas = horas
        
    def set_horas(self, horas):
        self.horas = horas

    def datos_garzon(self):
        datos_garzon = [self.ideper, self.nombre, self.horas]
        return datos_garzon

    

