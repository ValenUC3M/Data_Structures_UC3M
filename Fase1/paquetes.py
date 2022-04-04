#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 14:56:41 2020

@author: isegura
"""

from myqueue import SQueue
from dlist import DList
#########################################################################################################################
class Paquete:
    """Para representar paquetes"""
    
    #O(1) No hay mejor ni peor caso
    def __init__(self,idpaq,via,num,cp):
        self.idpaq=idpaq
        self.via=via
        self.num=num
        self.cp=cp
        #Por defecto la primera vez el número de intentos de entrega es 0
        self.numIntento=0
        self.incidencia = None
    
    #O(1) No hay mejor ni peor caso
    def __str__(self):
        result = "[" + self.idpaq + "  " + self.via + "  " + str(self.num) + "  " + str(self.cp) + "]"
        return result
    

#########################################################################################################################    
class Paquetes(SQueue):
    """Para representar el conjunto de todos los paquetes """
            
#########################################################################################################################    
class PaqueteEntregado(DList):
    """Para representar paquetes correctamente entregados"""

#########################################################################################################################            
class PaqueteIncidencia(DList):
    """clase para representar la lista de paquetes incidentados 
    junto a sus idreps y su motivo de la incidencia en una sublista auxiliar"""
        
        


 