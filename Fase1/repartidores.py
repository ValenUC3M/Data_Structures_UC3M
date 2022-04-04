#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 14:57:54 2020

@author: Gonzalo Valenti y Noelia Rodriguez
"""

from dlist import DList
from paquetes import Paquetes

#########################################################################################################################    
class Repartidores(DList):
    """Clase para representar al conjunto de todos los repartidores 
    ordenados por orden alfabético"""
    
    #O(n^2) Mejor caso: lista de nombres vacia. Peor caso: tener que ordenar la lista
    def sortReps(self,data):
        aux = DList()
        aux2 = DList()
        for elem in data: #pasamos de un array a una DList 
            aux.addLast(Repartidor(elem[0],elem[1],elem[2],elem[3]))
        for i in range(aux.size):  #vamos a ordenarlo usando una auxiliar (aux2)
            nodo = aux.head
            rep = aux.head.elem
            for i in range(1,aux.size):
                #usamos el asignado como manera de saber que reps ya están ordenados
                if rep.asignado == True:
                    rep = nodo.next.elem
                    nodo = nodo.next
                elif rep.nombre > nodo.next.elem.nombre and nodo.next.elem.asignado == False:
                    nodo = nodo.next
                    rep = nodo.elem
                else:
                    nodo = nodo.next
            #una vez encontrado, guardamos ese rep en la lista definitiva y seguimos con los demás    
            aux2.addLast(rep)
            rep.asignado = True
           
        return aux2
            
#########################################################################################################################
class Zonas(DList):
    """clase para representar la lista de zonas de un rep"""
    
#########################################################################################################################
class Repartidor():
    """Clase para represenar un repartidor """
    
    #O(n) Mejor caso: lista de zonas vacia; peor caso: lista de zonas con elementos
    def __init__(self,idrep,nombre,estado,zonas):
        #establecemos sus parámetros base
        self.idrep=idrep
        self.nombre=nombre
        self.estado=estado
        self.zonas= Zonas()
        for elem in zonas:
            self.zonas.addFirst(str(elem))
        self.paquetesRep=Paquetes()
        self.asignado = False
    
    #O(n) Mejor caso: self.zonas vacio; peor caso: self.zonas con elementos
    def __str__(self):
        zone = "["
        nodo = self.zonas.head
        for i in range(0,self.zonas.size):
            zone += nodo.elem +","
            nodo = nodo.next
        zone = zone[:-1]
        zone += "]"
            
        result = self.idrep + ", " + self.nombre + ", " + self.estado + ", Zonas: " + zone 
        return result
    
    #O(n) Mejor caso: self.zonas vacio; peor caso: self.zonas con elementos
    def zoneo(self,zona):
        #función para comprobar si el repartidor actúa en esa zona
        nodo = self.zonas.head
        for i in range(0,self.zonas.size):
            if zona == nodo.elem:
                return True
            nodo = nodo.next
        return False 
 
    
