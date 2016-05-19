# -*- coding: utf-8 -*-
__author__ = 'Enzo Ahumada'

from garzon import Garzon
from propina import Propina

garzones = []
prop = Propina()

def crea_garzon(ide, nom, hor):
    gar = Garzon(ide, nom, hor)
    add_garzon(gar)

def add_garzon(garzon):
    garzones.append(garzon)
    print ('Garzon añadido','   Garzones:', total_garzones())
    
def del_garzon(idegar):
    index = idegar - 1
    del garzones[index]
    print ('Garzon eliminado','   Garzones:', total_garzones())

def listar_garzones():
    for garzon in garzones:
        print(garzon.ideper, garzon.nombre)
    
def total_garzones():
    return len(garzones)

def total_horas():
    horas = []
    for garzon in garzones:
        horas.append(garzon.horas)
    return sum(horas)

def calcula_valor_hora():
    return prop.get_propina() / total_horas()

def calcula_propina_garzon(horas):
    return horas * calcula_valor_hora()

def calcula_propina():

    if prop.get_propina() == 0:
        print("No se puede calcular propina")
        print("El valor propina debe ser mayor a 0")
        print(' ')
    else:
        valor = []
        valor_garzon = 0
        for garzon in garzones:
            valor_garzon = calcula_propina_garzon(garzon.horas)
            valor.append(valor_garzon)
            print(garzon.nombre, ': ', int(valor_garzon))
        print ('Valor Propina:', int(sum(valor)))
