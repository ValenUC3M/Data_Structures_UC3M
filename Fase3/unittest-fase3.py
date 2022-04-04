#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 17:12:32 2020

@author: isegura
"""

import unittest
from fase3 import Mapa
from fase3 import PuntoEntrega


class Test(unittest.TestCase):
    def setUp(self):
        print('\ninicializando datos...\n')
        
        #https://github.com/isegura/EDA/blob/master/grafoEjemplo.png
        #Creamos puntos de entrega
        self.pA=PuntoEntrega('C/A',1,28921)             #A
        self.pB=PuntoEntrega('C/B',2,28921)             #B
        self.pC=PuntoEntrega('C/C',3,28922)             #C
        self.pD=PuntoEntrega('C/D',4,28922)             #D
        self.pE=PuntoEntrega('C/E',5,28923)             #E
        self.pF=PuntoEntrega('C/F',6,28923)             #F
        self.pG=PuntoEntrega('C/G',6,28923)             #G


        self.puntos=[self.pA,self.pB,self.pC,self.pD,self.pE,self.pF,self.pG]
        self.m=Mapa()
        for p in self.puntos:
            #m.anadirPuntoEntrega(PuntoEntrega(v,5,28911))
            self.m.anadirPuntoEntrega(p)
        
        #print(self.m)
        
        self.m.anadirConexion(self.pA,self.pB,8)                    #A,B,8
        self.m.anadirConexion(self.pA,self.pC,9)                    #A,C,9
        self.m.anadirConexion(self.pA,self.pD,14)                   #A,D,14
        
        self.m.anadirConexion(self.pB,self.pE,15)                   #B,E,15
        self.m.anadirConexion(self.pB,self.pF,11)                   #B,F,11
        
        self.m.anadirConexion(self.pC,self.pF,2)                    #C,F,2
        
        self.m.anadirConexion(self.pF,self.pG,8)                    #F,G,8
        self.m.anadirConexion(self.pD,self.pG,2)                    #D,G,2


        #print(self.m)
        
        
        # ruta aplicando dfs: A B E F C G D
        self.rutaDFS=[self.pA,self.pB,self.pE,self.pF,self.pC,self.pG,self.pD]
            
    
        #self.m.dijkstra()
        
        self.min_A_G=[self.pA,self.pD,self.pG]
        self.dis_A_G=16
        
        self.min_B_D=[self.pB,self.pF,self.pG,self.pD]
        self.dis_B_D=21
        
        self.min_E_D=[self.pE,self.pB,self.pF,self.pG,self.pD]
        self.dis_E_D=36
        
        

        
    def test1_estanConectados(self):
        #comprobamos por ejemplo las conexiones de p0
        print('\n****** test1_estanConectados ******************')
        self.assertEqual(self.m.estanConectados(self.pA,self.pB),8)
        self.assertEqual(self.m.estanConectados(self.pA,self.pC),9)
        self.assertEqual(self.m.estanConectados(self.pA,self.pD),14)
        #y una de sus recíprocas
        self.assertEqual(self.m.estanConectados(self.pB,self.pA),8)
        #comprobamos algunas que no están conectadas
        self.assertEqual(self.m.estanConectados(self.pA,self.pE),0)
        self.assertEqual(self.m.estanConectados(self.pA,self.pF),0)
        self.assertEqual(self.m.estanConectados(self.pA,self.pG),0)

        print('****** OK test1_estanConectados ******************')

        
    
    def test2_eliminarConexion(self):
        print('\n******  test2_eliminarConexion ******************')
        self.assertEqual(self.m.estanConectados(self.pB,self.pC),0)
        self.m.anadirConexion(self.pB,self.pC,10)                   #B,C,10
        self.assertEqual(self.m.estanConectados(self.pB,self.pC),10)
        self.m.eliminarConexion(self.pB,self.pC)
        self.assertEqual(self.m.estanConectados(self.pB,self.pC),0)
        
        print('****** OK test2_eliminarConexion ******************')

    def test3_generarRuta(self):
        print('\n****** test3_generarRuta ******************')
        result=self.m.generarRuta()
        self.assertEqual(len(result),len(self.rutaDFS))
        for i in range(len(result)):
            #print(result[i],self.rutaDFS[i])
            self.assertEqual(result[i],self.rutaDFS[i])
        print('****** OK test3_generarRuta ******************')

    def test4_rutaMinima(self):
        print('\n******  test4_rutaMinima ******************')
        result,d=self.m.rutaMinima(self.pA,self.pG)
        self.assertEqual(d,self.dis_A_G)
        self.assertEqual(len(result),len(self.min_A_G))
        for i in range(len(result)):
            self.assertEqual(result[i],self.min_A_G[i])
        print('****** OK test4_rutaMinima ******************')

    
#Descomenar para usarlo en Spyder
if __name__ == '__main__':
    unittest.main()