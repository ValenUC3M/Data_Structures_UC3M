#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 14:06:33 2020

@author: isegura
"""
from dlist import DList
from repartidores import Repartidores
from paquetes import Paquetes
from paquetes import Paquete
from paquetes import PaqueteEntregado
from paquetes import PaqueteIncidencia
import random 


class GestionAmazon():
    """Clase principal para representar la funcionalidad de la fase 1"""
    
    #O(1) No hay mejor ni peor caso
    def __init__(self):
        self.paquetes=Paquetes()
        self.repartidores=Repartidores()
        self.entregados=PaqueteEntregado()
        self.incidencias=PaqueteIncidencia()
        #creo esta lista para aquellos paquetes cuya asignación sea imposible por la razón que sea
        self.paquetesNoAsignados = PaqueteIncidencia()

#########################################################################################################################
    
    #O(n) Mejor caso: lista de paquetes vacia; peor caso: lista de paquetes con elementos
    def cargarPedidos(self,data):
        for elem in data:
            self.paquetes.enqueue(Paquete(elem[0],elem[1],elem[2],str(elem[3])))
            
#########################################################################################################################
    
    #O(n^2) Mejor caso: data esta vacio; peor caso: data tiene elementos
    def cargarRepartidores(self,data):
        self.repartidores = self.repartidores.sortReps(data)
                
#########################################################################################################################
    
    #O(n) Mejor caso: self.repartidores esta vacio; peor caso: que la lista contenga repartidores        
    def mostrarRepartidores(self):
        nodo = self.repartidores.head
        for i in range(0,self.repartidores.size):
            print("Repartidor:",nodo.elem)
            if nodo.elem.paquetesRep.size > 0:
                print("\t  Paquetes:")
                print("\t       ", nodo.elem.paquetesRep)
            else:
                print()
            nodo = nodo.next
            
#########################################################################################################################
    
    #O(n^2) Mejor caso: que la lista de pedidos esté vacia; peor caso: no encontrar ningun repartidor que cumpla lo requisitos      
    def asignarReparto(self,pedido=None,tipo="estandar"):
        if pedido == None:
            #suponemos que por pedido puede no entrar nada o puede entrar una dqueue
            pedido = self.paquetes
        while pedido.head != None: #bucle para asignar todos los pedidos
            repWin = None #primero le damos valor None
            repWin = self._selectRep1(repWin,pedido,tipo) #invocamos a la función para buscar un rep 
            #si no encontramos ninguno, repWin será None    
            if repWin == None:
                #si no encontramos,buscaremos al rep con menos zonas y activo para asignar ahí
                repWin = self._selectRep2(repWin,pedido,tipo)
            #print(repWin)
            if repWin == None:
                #en el caso de no haber ningun rep en activo, entraremos aqui para guardar el pedido en incidencias
                paq = pedido.head.elem
                print("No hay repartidor disponible para su reparto.")
                print("""Paquete {} en calle {} no asignado y retirado hasta que pueda ser asignado"""
                      .format(paq.idpaq, paq.via))
                self.paquetesNoAsignados.addLast(pedido.dequeue())

#########################################################################################################################
    
    #O(n) Mejor caso: la lista de repartidores esta vacia; peor caso: debemos recorrer la lista
    def _selectRep1(self,repWin,pedido,tipo):
        rep = self.repartidores.head
        #buscamos dentro de todos los reps el que cumpla las condiciones
        for i in range (self.repartidores.size):
                if rep.elem.estado == "Activo":
                    if rep.elem.zoneo(pedido.head.elem.cp) == True:
                        if repWin == None:
                            #este if está para asignarle al primer rep activo y con el zoneo == True, el rep win
                            repWin = rep.elem
                        else:
                            if repWin.paquetesRep.size > rep.elem.paquetesRep.size:
                                #si encontramos un rep que tenga el mismo cp que repWin y menos paqs, le asignamos a él el repWIn
                                repWin = rep.elem
                rep = rep.next
        #al rep que sea más favorable le llamamos repWin y le asignamos el pedido
        if repWin != None:
            if tipo == "reasignando":
                print("""Paquete [{}] reasignado a: {}""".format(pedido.head.elem.idpaq,repWin.idrep))
            repWin.paquetesRep.enqueue(pedido.dequeue()) 
        #devlvemos el repWin para poder usarlo en el resto de la función por si es None        
        return repWin 
                 
#########################################################################################################################   
    
    #O(n) Mejor caso: la lista de repartidores esta vacia; peor caso: hay que recorrer la lista
    def _selectRep2(self,repWin,pedido,tipo):
        #aqui entramos solo si ningun rep tiene el mismo cp que el del pedido
        rep = self.repartidores.head 
        for i in range (self.repartidores.size):
            if rep.elem.estado=="Activo":
                #buscamos reps activos
                if repWin == None:
                    #este if está para asignarle al primer rep activo, el rep win
                    repWin = rep.elem
                else:
                    #dentro de los reps activos, buscamos los que menos zonas tengan
                    if rep.elem.zonas.size < repWin.zonas.size:
                        repWin = rep.elem
                    #dentro de los que menos zonas tengan, buscamos el que menos paquetes asignados tenga a su nombre
                    elif rep.elem.zonas.size == repWin.zonas.size:
                        if rep.elem.paquetesRep.size < repWin.paquetesRep.size:
                            repWin = rep.elem
                                    
                    rep=rep.next
        if repWin != None:
        #al rep que sea más favorable le llamamos repWin y le asignamos el pedido
            if tipo == "reasignando":
                print("""Paquete [{}] reasignado a: {}""".format(pedido.head.elem.idpaq,repWin.idrep))
            repWin.zonas.addLast(pedido.head.elem.cp)   #en el rep ganador, creamos un nuevo cp con el cp del pedido
            repWin.paquetesRep.enqueue(pedido.dequeue())
        #devolvemos el repWin para poder usarlo en el resto de la función por si es None
        return repWin
            
#########################################################################################################################    
   
    #O(n^2) Mejor caso: self.repartidores esta vacio o el repartidor no existe;
    #peor caso: encontrar el repartidor y reasignar su reparto                        
    def bajaRepartidor(self,idRep):
        print("hola")
        rep = None
        asignado = False
        nodo = self.repartidores.head
        #en este bucle buscaremos si esa id corresponde a la de algún repartidor...
        for i in range(0,self.repartidores.size):
            if idRep == nodo.elem.idrep and asignado == False:
                asignado = True
                rep = nodo.elem
                nodo = nodo.next
            else:
               nodo = nodo.next
        #si existe ese rep invocaremos a la función asignar reparto
        if rep != None:
            print("""\nDando de baja repartidor de id: {} y reasignando paquetes...""".format(rep.idrep))
            rep.estado = "No Activo"
            self.asignarReparto(rep.paquetesRep,"reasignando")
        #de no existir nadie con esa id lanzaremos una excepcción
        else:
            print("""repartidor con id: {} no existe dentro de nuestro equipo de repartidores y por tanto no es dado de baja""".format(idRep))

######################################################################################################################### 
    
    #O(n^3) Mejor caso: la lista de repartidores esta vacia ; peor caso: hay repartidores con paquetes por entregar        
    def reparto(self):
        #llamamos a todos los reps y entregamos todos sus paqs usando la funcion de entregaPaquetes
        if self.repartidores.size > 0:
            nodo = self.repartidores.head
            for i in range(0,self.repartidores.size):
                if nodo.elem.paquetesRep.size > 0:
                    self.entregaPaquetes(nodo.elem,True)
                nodo = nodo.next
                      
        else:
            print("Error en los repartos: No hay repartidores")

#########################################################################################################################    
    
    #O(n^2) Mejor caso: el repartidor ya este asignado; peor caso: que debamos asignarlo         
    def entregaPaquetes(self,repartidor,asignado=True):
        #por repartidor nos van a pasar o la ip o el objeto, para eso tenemos el asignado
        #con el asignado comprobaremos si el repartidor lo llaman desde dentro de la función reparto
        #de no ser así se ejecuta el for que comprueba si ese repartidor existe en la lista de reps
        rep = None
        nodo = self.repartidores.head
        if asignado == False:
            for i in range(0,self.repartidores.size):
                if repartidor == nodo.elem.idrep and asignado == False:
                    asignado = True
                    rep = nodo.elem
                    nodo = nodo.next
                else:
                    nodo = nodo.next
        else:
            #recibiremos el elem del nodo repartidor en la entrada
            rep = repartidor
        print("""\nEjecutando repartos de {}:""".format(rep.idrep))
        while rep.paquetesRep.size != 0:
            #para el rep vamos a entregar cada uno de sus paquetes
            self._entregaPaquetes(rep)
           
#########################################################################################################################
    
    #O(n) Mejor caso: lista de paquetes del repartidor este vacia; 
    #peor caso: que la lista tenga elementos y haya paquetes que entregar 
    def _entregaPaquetes(self,rep): 
         #para cada paquete vamos a entregarlo con un 50% de probabilidad de exito
         #vamos a llevar como minimo una iteración por paq y como máximo 3 
         for i in range(rep.paquetesRep.size):
                nodo = rep.paquetesRep.head
                if random.randint(0,1)== 1:
                    #si sale 1, el paq será entregado
                    nodo.elem.numIntento += 1
                    print("""-Paquete [{}] entregado con éxito por {}.\nSerán guardados los datos del envío en la lista de entregados.""".format(nodo.elem.idpaq, rep.idrep))
                    print("Número de intentos necesitados: "+ str(nodo.elem.numIntento))
                    #guardaremos la idrep la idpaq el num de intentos en una aux que luego meteremos en la lista de entregados
                    aux = DList()
                    aux.addLast(rep.idrep)
                    aux.addLast(nodo.elem.idpaq)
                    aux.addLast(nodo.elem.numIntento)
                    self.entregados.addLast(aux)
                    #aqui extraemos el paq de la lista del rep ya que ya ha sido entregado
                    rep.paquetesRep.dequeue()
                    
                else:
                    nodo.elem.numIntento += 1
                    if nodo.elem.numIntento == 3:
                        print("""-Paquete [{}] no entregado por: {}. \nDebido a incidencia con reparto, será guardado en la lista de incidencias."""
                              .format(nodo.elem.idpaq, rep.idrep))
                        #guardaremos la idrep la idpaq el motivo de incidencia en una aux que luego meteremos en la lista de entregados
                        aux = DList()
                        aux.addLast(rep.idrep)
                        aux.addLast(nodo.elem.idpaq)
                        aux.addLast("intentos máximos superados")
                        self.incidencias.addLast(aux)
                        rep.paquetesRep.dequeue()
                    else:
                        #si no es 3, el paquete se quita del head y entra en el tail
                        #de esta manera vamos recorriendo todo el tiempo la queue 
                        rep.paquetesRep.enqueue(rep.paquetesRep.dequeue())                    
                        
                        
                        
                



