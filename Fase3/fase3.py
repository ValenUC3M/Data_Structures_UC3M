#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 20:49:06 2020

@author: isegura
"""
import sys

class PuntoEntrega():
    
    #O(1) No hay mejor ni peor caso
    def __init__(self,via,num=None,cp=None):
        self.via=via
        self.num=num
        self.cp=cp
        
    #O(1) No hay mejor ni peor caso
    def __eq__(self,other):
        if other==None:
            return False
        
        return self.via==other.via and self.num==other.num and self.cp==other.cp
    
    #O(1) No hay mejor ni peor caso
    def __str__(self):
        result=str(self.via)
        if self.num!=None:
            result+=', '+str(self.num)
        if self.cp!=None:
            result+=', '+str(self.cp)
        return result


 
class Mapa():
    #el mapa sera el grafo que usaremos para la representacion y estara basado en un diccionario
    
    #O(1) No hay mejor ni peor caso
    def __init__(self):
        self.vertices={}
        self.puntosEntrega = []
        
    #O(1) No hay mejor ni peor caso    
    def anadirPuntoEntrega(self,pto):
        self.puntosEntrega.append(pto)
        self.vertices[len(self.puntosEntrega)-1] = []
        
    
    #O(n) Mejor caso: que los puntos no esten en la lista y se imprima el error; peor caso: los puntos
#estan en la lista y con subindices les añadimos una tupla de sus conexiones    
    def anadirConexion(self,pto1,pto2,distancia):
        if pto1 in self.puntosEntrega and pto2 in self.puntosEntrega:
            index1 = self.puntosEntrega.index(pto1)
            index2 = self.puntosEntrega.index(pto2)
            self.vertices[index1].append((index2,distancia))
            self.vertices[index2].append((index1,distancia))
        else:
            print("Error: Conexion not in database")
            
            
    
    #creo esta funcion que dados dos puntos, devuelve sus dos index para el diccionario   
    #O(n) No hay mejor ni peor caso ya que con el uso del break la funcion queda optimizada   
    def buscaIndex(self,pto1,pto2):
        #me complico usando estos bucles para hacer que su complejidad se reduzca
        #antes usaba dos lista.index y dos x in lista y era poco optimo
        index1 = None
        index2 = None
        for i in range(len(self.puntosEntrega)):
            if self.puntosEntrega[i] == pto1:
                index1 = i
            if self.puntosEntrega[i] == pto2:
                index2 = i
            if index1 != None and index2 != None:
                break
        if index1 != None and index2 != None:
            return (index1,index2)
                   
    #O(n) Mejor caso: que no encuentre los indices y devuelva un 0; peor caso: que los indices sean distintos        
    def estanConectados(self,pto1,pto2):
        #recibo dos indexs para los dos puntos
        indexs = self.buscaIndex(pto1,pto2)
        values = 0
        if indexs[0] == indexs[1]:
            #comprobacion por si ambos puntos son el mismo punto 
            return 0
        if indexs != None:
            #si indexs es distinto de none busco si tienen indexs en comun
            if len(self.vertices[indexs[0]])> 0:
                for i in self.vertices[indexs[0]]:
                    if i[0]==indexs[1]:
                        values = i[1]
                        break
                if values != 0:
                    #si encontramos uno, es decir values tiene valor, lo devolvemos
                    if (indexs[0],values) in self.vertices[indexs[1]]:
                        return values
                    
            #si no se cumplen las condiciones, devolvemos cero         
            return 0
    
    
    #O(n^2) Mejor caso: que los indices no existan o sean los mismo; peor caso: que sean distintos y haya que eliminarlos       
    def eliminarConexion(self,pto1,pto2):
        #podri­a reutilizar el metodo anterior pero sera­a muy poco optimo hacerlo
        #recibo dos indexs para los dos puntos
        indexs = self.buscaIndex(pto1,pto2)
        values = 0
        if indexs[0] == indexs[1]:
            #por si ambos puntos son el mismo punto 
            return 0
        if indexs != None:
            #si indexs es distinto de none busco si tienen indexs en comun
            if len(self.vertices[indexs[0]])> 0:
                for i in self.vertices[indexs[0]]:
                    if i[0]==indexs[1]:
                        values = i[1]
                        self.vertices[indexs[0]].remove((indexs[1],values))
                        break
                if values != 0:
                    #si encontramos uno, es decir values tiene valor, 
                    if (indexs[0],values) in self.vertices[indexs[1]]:
                        self.vertices[indexs[1]].remove((indexs[0],values))
        else:
            print("Error: indexs not found")

    
    #O(n) Mejor caso:self.puntoEntrega esta vacia; peor caso: contiene elementos    
    def __str__(self):
        value = 0
        for i in self.puntosEntrega:
            print(i,"["+str(value)+"] :",self.vertices[value])
            value += 1
        return ""
    
    
    #O(n^2) Hay que recorrer todos los vertices del grafo y en cada vertice 
    #recorrer su lista de vertices adyacentes
    def generarRuta(self): 
        """Funcion para devolver una lista de py con todos los vertices usando DFS"""
        #Marcamos los vertices como no visitados 
        visited={}
        aux = []
        for v in self.vertices.keys():
            visited[v]=False
    
        for v in self.vertices.keys():
            #uno a uno vamos guardándolos en nuestra lista auxiliar
            if visited[v]==False:
              self._dfs(v, visited, aux)      
        return aux 

    def _dfs(self, v, visited,aux): 
        """This funcion prints the DFS traversal from the vertex whose index is indexV"""
        # Mark the current node as visited and print it 
        visited[v] = True
        #print(v, end = ' ') 
        #Instead of printing the index, we have to print its label
        aux.append(self.puntosEntrega[v])
        # Recur for all the vertices  adjacent to this vertex 
        for elem in self.vertices[v]: 
          if visited[elem[0]] == False: 
            self._dfs(elem[0], visited,aux)
        
    
    
    #algoritmos de cálculo de dijkstra 
    #son tres: el cálculo de distancias minimas, el calculo de los posibles caminos y el de el camino en cuestión
    #O(n) Mejor caso: lista de vertices vacia; peor caso: que contenga elementos 
    def minDistance(self, distances, visited): 
        """This functions returns the vertex (index) whose associated value in
        the dictionary distances is the smallest value. We 
        only consider the set of vertices that have not been visited"""
        # Initilaize minimum distance for next node 
        min = sys.maxsize 

        #returns the vertex with minimum distance from the non-visited vertices
        for vertex in self.vertices.keys(): 
            #vamos a buscar el vertice con la menor distancia 
            if distances[vertex] <= min and visited[vertex] == False: 
                min = distances[vertex] #update the new smallest
                min_vertex = vertex      #update the index of the smallest
    
        return min_vertex 


    #O(n^2) Mejor caso: que la lista de vertices este vacia; peor caso: que tenga elementos y calculemos dijkstra
    def dijkstra(self, origin): 
        """Usaremos esta función para dado un vértice, calcular las menores distancias a el mismo
        desde todos los demás vértices, podríamos hacer que solo fuera de uno a todos pero permitiremos que
        cualquier vertice sea el origen"""
        #visited servirá para coger los vertexs no asignados aún
        #default de visited[v] queremos que sea False
        visited={}
        for v in self.vertices.keys():
            visited[v]=False

        #Guardaremos el vertice anterior al vertice seleccionado, será muy util a la hora de deshacer el camino
        previous={}
        for v in self.vertices.keys():
            #initially, we defines the previous vertex for any vertex as None
            previous[v]=None

        #This distance will save the accumulate distance from the origin to the vertex (key)
        distances={}
        for v in self.vertices.keys():
            distances[v]=sys.maxsize
            #default todos tienen una distancia 'infinita'
            
        #The distance from origin to itself is 0
        distances[origin] = 0
        
        for n in range(len(self.vertices)): 
            # Pick the vertex with the minimum distance vertex. En la primera iteración cogerá el origin
            # u is always equal to origin in first iteration 
            winner = self.minDistance(distances, visited) 
            visited[winner] = True
            
            # Update distance value of the u's adjacent vertices only if the current  
            # distance is greater than new distance and the vertex in not in the shotest path tree 
            
            #we must visit all adjacent vertices (neighbours) for u
            for elem in self.vertices[winner]: 
                adjV = elem[0]
                adjW = elem[1]
                #vamos a comprobar para los adj a el vertice escogido si sus actuales distancias,
                #son menores que la distancia total de vertex + el peso de adj
                if visited[adjV]==False and distances[adjV] > distances[winner] + adjW:
                    #si se cumple, actualizamos su distancia a la nueva
                    distances[adjV]=distances[winner] + adjW  
                    previous[adjV]= winner
                    
        return distances, previous
    
    #O(n^2) Mejor caso: start==end; peor caso: que sean distintos y haya que calcular el camino entre ellos
    def camineador(self,start,end,previous):
        #función que calcula el camino de start a end y lo devuelve en forma de array
        caminico = [self.puntosEntrega[end]]
        vertice = end
        while vertice != start:
            #vamos recorriendo el diccionario de previous hasta llegar a start
            #simultaneamente vamos metiendo esos vertices en la lista
            vertice = previous[vertice]
            #como vertice solo es un señalizador, necesitamos escoger el objeto vertice de la lista de entregas
            caminico.insert(0,self.puntosEntrega[vertice])
        
        return caminico
            
######################################################################################
    
    #O(n^2) Mejor caso: que starty end sean iguales; peor caso: que sean distintos y tengamos que calcular su ruta minima            
    def rutaMinima(self, start, end):
        #como queremos usarlos en forma de indices y no de objetos, primero habrá que cambiarlos
        start = self.puntosEntrega.index(start)
        end = self.puntosEntrega.index(end)
        #invocamos a dijkstra todopoderoso para que nos devuelva los diccionarios de distances y previous
        distances, previous = self.dijkstra(start)
        #usando estos diccionarios calcularemos el camino a seguir y el peso
        camino = self.camineador(start,end,previous)
        
        return camino,distances[end]
    
        
        
        

       

def test():
    
    pA=PuntoEntrega('C/A',1,28921)             #A
    pB=PuntoEntrega('C/B',2,28921)             #B
    pC=PuntoEntrega('C/C',3,28922)             #C
    pD=PuntoEntrega('C/D',4,28922)             #D
    pE=PuntoEntrega('C/E',5,28923)             #E
    pF=PuntoEntrega('C/F',6,28923)             #F
    pG=PuntoEntrega('C/G',7,28923)             #G


    puntos=[pA,pB,pC,pD,pE,pF,pG]
    m=Mapa()
    for p in puntos:
        m.anadirPuntoEntrega(p)
        
    print(m)
    
    m.anadirConexion(pA,pB,8)                    #A,B,8
    m.anadirConexion(pA,pC,9)                    #A,C,9
    m.anadirConexion(pA,pD,14)                   #A,D,14
        
    m.anadirConexion(pB,pE,15)                   #B,E,15
    m.anadirConexion(pB,pF,11)                   #B,F,11
        
    m.anadirConexion(pC,pF,2)                    #C,F,2
        
    m.anadirConexion(pF,pG,8)                    #F,G,8
    m.anadirConexion(pD,pG,2)                    #D,G,2
    
    print(m)
#    
#    m.modificarConexion(m.puntosEntrega[0],m.puntosEntrega[1],8)#A,B,8
#    
    print(pA,pB,' conectados?:',m.estanConectados(pA,pB))
   
    print(pC,pG,' conectados?:',m.estanConectados(pC,pG))
    
    m.eliminarConexion(pA,pB)
    print()
    print(m)
#    
#    m.anadirConexion(pA,pB,8)                    #A,B,8
#
#    
#    print('generarRutas:',end=' ')
    ruta=m.generarRuta()
    print('Ruta:')
    for i in ruta:
        print(i)
#    for r in ruta:
#        print(r, end=' ')
#    print()
    print("minimun")
    minimum_path,d=m.rutaMinima(pA,pG)
    for p in minimum_path:
        print(p)
    print('total distance:',d)


#Descomenar para usarlo en Spyder
if __name__ == '__main__':
    test()