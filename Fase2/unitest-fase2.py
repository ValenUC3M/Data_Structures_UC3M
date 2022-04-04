# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import unittest
from fase2 import Zonas


def areEqual(tree1,tree2):
    """función auxiliar para comprobar si dos árboles de zonas son iguales"""
    return areEqualNode(tree1.root,tree2.root)
    
def areEqualNode(node1,node2):
    """función auxiliar para comprobar si dos nodes de zonas son iguales.
    Ojo!!! No miramos en su lista de repartidores"""

    if node1==None and node2==None:
        return True
    if node1 and node2==None:
        return False
    if node1==None and node2:
        return False
    
    return node1.elem.cp==node2.elem.cp and areEqualNode(node1.left,node2.left) and areEqualNode(node1.right,node2.right)

class Test(unittest.TestCase):
    
    def setUp(self):
        print('\ninicializando datos (se inicializan para cada método)...\n')
        self.lZonas=[28332, 28378, 28142, 28331, 28193, 28766,28760]
        self.objZona=Zonas()
        for z in self.lZonas:
            self.objZona.crearZona(z)
         
        
        self.cp1=28332
        self.rep28332=['Iglesias, P.','Sánchez, P.','Abascal, J.','Arrimadas, I.']
        for r in self.rep28332:
            self.objZona.asignarRepartidor(self.cp1,r)
        
        
        self.cp2=28142
        self.rep28142=['Calvo, C.','Montero, MJ.','Montero, I.']
        for r in self.rep28142:
            self.objZona.asignarRepartidor(self.cp2,r)
        
        
        self.cp3=28766
        self.objZona.asignarRepartidor(self.cp3,'Casado, P.')


        self.cp4=28193
        self.rep28193=['Castells, M.','Grande-Marlaska, F.','Celaa, I.']
        for r in self.rep28193:
            self.objZona.asignarRepartidor(self.cp4,r)
        
        
        #self.objZona.draw()

         
    def test1_zonas(self):
        print('******* test_zonas ***************************************************')
        result=self.objZona.zonas()
        output=sorted(self.lZonas)
        #print('\t\toutput producida:',result)
        #print('\t\toutput esperada:',output)
        self.assertEqual(len(result),len(output),'FAIL: lenghts are different')
        for i in range(len(result)):
            self.assertEqual(result.getAt(i).cp,output[i],'FAIL: zonas are not equal')
        print('****** OK test1_zonas ************************************************\n')
        
        
    def test2_repartidores(self):
        print('******* test_repartidores ********************************************')
        result=self.objZona.repartidores(self.cp1)
        output=sorted(self.rep28332)
        #print('\t\toutput producida:',result)
        #print('\t\toutput esperada:', output)
        self.assertEqual(len(result),len(output),'FAIL: lenghts are different')
        for i in range(len(result)):
            self.assertEqual(result.getAt(i),output[i],'FAIL: repartiores are not equal')
        print('****** OK test2_repartidores *****************************************\n')

    def test3_borrarRepartidor(self):
        print('******* test_borrarRepartidor *************************************************')
        nombreRep='Abascal, J.'
        #print('\tborrarRepartidor() zona='+ str(self.cp1) + ", repartidor="+ nombreRep)
        self.objZona.borrarRepartidor(self.cp1,nombreRep)

        result=self.objZona.repartidores(self.cp1)
        output=sorted(self.rep28332)
        output.remove(nombreRep)
        #print('\t\toutput producida:',result)
        #print('\t\toutput esperada:',output)
        self.assertEqual(len(result),len(output),'FAIL: lenghts are different')
        for i in range(len(result)):
            self.assertEqual(result.getAt(i),output[i],'FAIL: repartidores are not equal')
#
        print('****** OK test3_borrarRepartidor ************************************************\n')

        

    
    def test4_isBalanced(self):
        print()
        print('******* test4_isBalanced ***************************************')
        
        print('\tCaso 1: isBalanced() para no balanceado.')
        #self.objZona.draw()   
        self.assertFalse(self.objZona.isBalanced(),'FAIL: the input is not balanced!!!')
        self.objZona.draw()        
        print('\tCaso 2: isBalanced() para un balanceado.')
        #añado zonas para hacerlo balanceado
        self.objZona.crearZona(28140)
        self.objZona.crearZona(28375)
        #self.objZona.draw()
        self.assertTrue(self.objZona.isBalanced(),'FAIL: the input is not balanced!!!')
#        print('\n\n')

        print('******* OK test4_isBalanced ******************************')


    
    def test5_balance(self):
         print('******* test5_balance ******************************************')
         #self.objZona.draw()
         self.objZona.balance()
         #self.objZona.draw()
         aux=Zonas()
         for z in [28332, 28760,28378, 28766, 28193, 28331, 28142]:
             aux.crearZona(z)
         #aux.draw()
         self.assertTrue(areEqual(self.objZona,aux),'Fail: are not equal')
         
         print('******* OK test5_balance ***************************************')
 
    def test6_borrarZona(self):
        """El caso de borrar una zona con repartidores, el test no verifica la 
        correcta reasignación de repartidores. Se visualiza el árbol 
        y se comprueba manualmente"""
        
        print('******* test6_borrarZona (TIENES QUE MIRAR LOS ÁRBOLES!!!) *****')

        cp=28378
        print('\tCaso 1: borrarZona() para un cp sin repartidor:'+ str(cp) )
        self.objZona.borrarZona(cp)
        result=self.objZona.zonas()
        output=sorted(self.lZonas)
        output.remove(cp)
        #print('\t\toutput producida:',result)
        #print('\t\toutput esperada:',output)
        self.assertEqual(len(result),len(output),'FAIL: lenghts are different')
        for i in range(len(result)):
            self.assertEqual(result.getAt(i).cp,output[i],'FAIL: zonas are not equal')
        print()

        
        print('\tCaso 2: borrarZona() para un cp con repartidor:'+ str(self.cp1) )
        print('\tantes de borrar: ' + str(self.cp1)+'\n')
        self.objZona.draw()
        
        self.objZona.borrarZona(self.cp1)
        result=self.objZona.zonas()
        output.remove(self.cp1)
        #print('\t\toutput producida:',result)
        #print('\t\toutput esperada:',output)
        self.assertEqual(len(result),len(output),'FAIL: lenghts are different')
        for i in range(len(result)):
            self.assertEqual(result.getAt(i).cp,output[i],'FAIL: zonas are not equal')
        print()
        print('\n\tdespués de borrar: ' + str(self.cp1)+'\n')
        self.objZona.draw()
        print('****** OK test6_borrarZona ************************************************\n')

      
        
#Descomenar para usarlo en Spyder
if __name__ == '__main__':
    unittest.main()