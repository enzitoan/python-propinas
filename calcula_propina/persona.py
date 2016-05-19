# -*- coding: utf-8 -*-
__author__ = 'Enzo Ahumada'

class Persona(object):
    
    def __init__(self, ideper, nombre):
        self.ideper = ideper
        self.nombre = nombre
        self.apepat = None
        self.apemat = None

    def datos_persona(self):
        lista_datos = [self.ideper, self.nombre, self.apepat, self.apemat]
        return lista_datos




