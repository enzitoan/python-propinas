# -*- coding: utf-8 -*-
__author__ = 'Enzo Ahumada'

import sistema

def carga_sistema():
    print ('SISTEMA CALCULO DE PROPINAS')
    print ('***************************')
    
    valor = input('Inserte Propina Total: ')
    
    if valida_propina(valor) == True:        
        sistema.prop.set_propina(int(valor))
        print('Propina:', sistema.prop.get_propina())
        sistema.crea_garzon(1,'Gar1',8)
        sistema.crea_garzon(2,'Gar2',5)
        sistema.crea_garzon(3,'Gar3',4)
    else:
        print (' ')
        carga_sistema()

def valida_propina(valor):
    while True:
        try:
            valor = int(valor)
            return True
        except ValueError:
            print ("ATENCIÓN: Debe ingresar un número entero.")
            return False
        
if __name__ == '__main__':
    carga_sistema()    


