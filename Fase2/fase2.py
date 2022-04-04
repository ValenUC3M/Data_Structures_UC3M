



from binarytree import Node
from binarysearchtree import BinarySearchTree
from dlist import DList

class Repartidores(BinarySearchTree):
    
################################################################################
    #versión del inorder que guarda los nodos en la DList aux
    #O(n) Mejor caso: self.root este vacia; peor caso: que tenga que recorrer todo el arbol
    def inorder(self,aux):
        self._inorder(self.root,aux)

    def _inorder(self,node,aux):
       if node!=None:
          self._inorder(node.left,aux)
          aux.addLast(node.elem)
          self._inorder(node.right,aux)
        
################################################################################
class Zona:
    #O(1) No hay mejor ni peor caso
    def __init__(self,cp):
        self.cp = cp
        self.repartidores = Repartidores()
     
    #O(1) No hay mejor ni peor caso
    def __str__(self):
        if self.repartidores.root == None:
           retorno = "["+str(self.cp)+"]"
           
        else:
           retorno = "["+str(self.cp)+"]"
       
        return(retorno)
    
    #funciones para comparar objetos sin que python se vuelva loco
    #O(1) No hay mejor ni peor para ninguna de ellas y tienen la misma complejidad
    def _eq_(self,otro):
        if self.cp==otro.cp:
            return True
        return False
    
    def _gt_(self,otro):
        if self.cp>otro.cp:
            return True
        return False
    
    def _lt_(self,otro):
        if self.cp<otro.cp:
            return True
        return False
                 
################################################################################    
class Zonas(BinarySearchTree):

    #versión del inorder que guarda los nodos en la DList aux
    #guardamos el nodo entero, es decir tanto el cp como sus reps
    #O(n) Mejor caso: la raiz esta vacia; peor caso: llamada recursiva funcion _inorder
    def inorder(self,aux):
        if self.root == None:
            print("Error: tree is empty")
        else:
            self._inorder(self.root,aux)

    def _inorder(self,node,aux):
       if node!=None:
          self._inorder(node.left,aux)
          aux.addLast(node.elem)
          self._inorder(node.right,aux)
       
################################################################################   
    #version del find que devuelve el objeto del arbol     
    #O(log2(n)) Mejor caso: root esta vacio, la funcion devuelve found; peor caso: el contrario y la funcion entre en el while
    def find(self,cp):
        nodo = self.root
        found = None
        while nodo != None and found == None:
            if nodo.elem.cp == cp:
                found = nodo
            elif nodo.elem.cp > cp:
                nodo = nodo.left
            else:
                nodo = nodo.right
        return found
            
################################################################################           
    
    #funcion para añadir una nueva zona al arbol 
    #O(nlog(n)) Mejor caso: el cp es igual y salta un error; peor caso: recorrer el arbol para añador la zona       
    def crearZona(self,cp):
      #si el root no existe es que el arbol esta vacio
      if self.root == None:
          self.root = Node(Zona(cp))
          return
      nodo = self.root
      asignado = False
      while asignado == False:
          #de encontrar un nodo que sea igual su cp saltará un error
          if nodo.elem.cp == cp:
              asignado = True
              print("Error 420: Cp ["+str(cp)+"] already exist")
          #recorremos el arbol en busca de donde asignar el nuevo nodo              
          elif nodo.elem.cp < cp:
              if nodo.right == None:
                  newNode = Node(Zona(cp))
                  newNode.parent = nodo
                  nodo.right = newNode
                  asignado = True
              else:
                  nodo = nodo.right
             
          else:
              if nodo.left == None:
                  newNode = Node(Zona(cp))
                  newNode.parent = nodo
                  nodo.left = newNode
                  asignado = True
              else:
                  nodo = nodo.left
                  
################################################################################  
    #en este método creamos una lista ordenada usando el inorder de los nodos de zonas
    #cada nodo contendrá tanto su cp como sus correspondientes reps
    #O(n) Porque llama al método inorder, no hay peor ni mejor caso
    def zonas(self):
        aux = DList()
        self.inorder(aux)
        return aux
    
################################################################################  
    
    #O(log2(n)) Mejor caso: no encontar la zona; peor caso: que se ejecute el .insert    
    def asignarRepartidor(self,cp,repartidor):
        #buscamos un cp y si lo encontramos hacemos un insert del repartidor en la base
        zona = self.find(cp)
        if zona != None:
            zona.elem.repartidores.insert(repartidor)
        else:
            print("Error: zone not located in tree")
            
################################################################################ 
            
    #O(log2(n)) Mejor caso: que no encuentre el cp y devuelva el error; peor caso: que se ejecute el .inorder
    def repartidores(self,cp):
        #buscamos un cp y si se encuentra, retornamos una lista de todas los reps de esa zona
        zona = self.find(cp)
        if zona != None:
            aux = DList()
            zona.elem.repartidores.inorder(aux)
            if aux.isEmpty():
                print("No reps found")
                return aux
            else:
                return aux
        else:
            print("Error: zone not located in tree")
            return 
                
################################################################################
    #buscamos una zona, luego el rep y ejecutamos el remove sobre ese tree del rep
    #O(log2(n)) Mejor caso: no encontrar el cp y devuelve un error; peor caso: que se ejecute el .remove
    def borrarRepartidor(self,cp,repartidor):
        zona = self.find(cp)
        if zona != None:
            zona.elem.repartidores.remove(repartidor)
   
################################################################################ 
    
    #O(nlog(n)) Mejor caso: lista de repartidores vacia o longitud 1; peor caso: encontrar la zona para borrar     
    def borrarZona(self,cp):
        listZonas = self.zonas()
        listReps = self.repartidores(cp)
        self.remove(cp)
        print("Zone ["+ str(cp) +"] deleted from dataBase, starting reps distribution...")
        if listZonas.size > 1 and listReps.size > 0 :
            #primero buscaremos el nodo para pivotar sobre él
            pivote = None
            nodo = listZonas.head
            while pivote == None:
                if nodo.elem.cp == cp:
                    pivote = nodo
                else:
                    nodo = nodo.next
            #estos dos nodos serán para ir asignando los reps de forma simúltánea y así reducir
            #la complejidad final del proyecto
            nodoUp = pivote.next
            nodoDown = pivote.prev
            #primer caso: el pivote es el head
            if nodoDown == None:
                while listReps.size > 0:
                    if nodoUp == listZonas.tail:
                        nodoUp.elem.repartidores.insert(listReps.removeFirst())
                        nodoUp = pivote.next
                    else:
                        nodoUp.elem.repartidores.insert(listReps.removeFirst())
                        nodoUp = nodoUp.next
                        
            #segundo caso: si el pivote es el tail           
            elif nodoUp == None:
                while listReps.size > 0:
                    if nodoDown == listZonas.tail:
                        nodoDown.elem.repartidores.insert(listReps.removeFirst())
                        nodoDown = pivote.prev
                    else:
                        nodoDown.elem.repartidores.insert(listReps.removeFirst())
                        nodoDown = nodoUp.prev
            #tercer caso: el pivote no es ni head ni tail
            else:
                while listReps.size > 0:
                    '''llevamos a cabo un asignamiento simultáneo de dos reps maximo y uno
                    como mínimo para asegurar que se reparten equitativamente entre sus atecesores
                    y sus predecesores...'''
                    if  nodoDown == listZonas.tail:
                        nodoDown.elem.repartidores.insert(listReps.removeFirst())
                        nodoDown = pivote.prev
                    else:
                        nodoDown.elem.repartidores.insert(listReps.removeFirst())
                        nodoDown = nodoDown.prev
                    if listReps.size > 0:
                        '''como es simúltaneo, se puede dar el caso de que los reps fueran impares
                        asi pues aquí nos aseguraremos de que aún queden reps que asignar antes de entrar'''
                        if nodoUp == listZonas.tail:
                            nodoUp.elem.repartidores.insert(listReps.removeFirst())
                            nodoUp = pivote.prev
                        else:
                            nodoUp.elem.repartidores.insert(listReps.removeFirst())
                            nodoUp = nodoUp.next
            print("Reasignment of reps completed") 
        else: 
            if listReps.size == 0:
                print("Error: No reps ready for asignment")
            elif listReps.size == 1:
                print("Error: No zones available for reps asignment")
        
                 
                                        
################################################################################ 
    #aqui solo comprobamos si el total del arbol está o no balanceado 

    #O(n) Mejor caso: el arbol esta vacio; peor caso: llamada recursiva a ._isBalanced           
    def isBalanced(self):
        if self.root==None:
            print("Árbol vacío")
            return
        else:
            return self._isBalanced(self.root)
    
    #O(n) Mejor caso: node== None; peor caso: llamada recursiva a ._isBalanced       
    def _isBalanced(self,node):
        if node==None:
            return True
        dif=self._size(node.right)-self._size(node.left)
        if dif<-1 or dif >1:
            return False
        else:
            if (self._isBalanced(node.left)) and (self._isBalanced(node.right)):
                return True
            return False
    
################################################################################
    #usaremos para balancearlo una versión de isbalanced que solo aplica a un nodo y no a todos        
    #O(nlog2(n)) Mejor caso: el arbol esta vacio; peor caso: llama recursiva a ._balance
    def balance(self):
        if self.root==None:
            print("Árbol vacío")
            return 
        return self._balance(self.root) 
        #invocamos al submetodo que balancea
    
    #O(nLog2(n)) Mejor caso: la lista ya esta balanceada; peor caso: tenemos que balancearla        
    def _balance(self,node):
        #para cada nodo comprobamos si está balanceado
        if self._esBalanceada(node)==True:
            if node.left!=None:
                self._balance(node.left)
            if node.right!=None:
                self._balance(node.right)
        else:  #de no estar balanceado, lo balanceamos
            dif=self._size(node.right)-self._size(node.left)
            cont=dif//2
            if dif>0:
                #derecha
                #como hay que recolocar cont nodos del lado izq haremos cont iteraciones
                #esto es el algoritmo visto en clase para recolocar nodos llevado a codigo
                for i in range(cont):
                    if node.right!=None:
                        auxNode=node.right
                        while auxNode.left!=None:
                            auxNode=auxNode.left
                    else:
                        auxNode=node
                    if node.left==None:
                        orig=node.elem
                        nuevo=auxNode.elem
                        self._removeNode(auxNode)
                        node.elem=nuevo
                        self.insert(orig)
                    else:
                        self._insertNode(node.left,node.elem)
                                
                        node.elem=auxNode.elem
                        self._removeNode(auxNode)
            else:
                #izquierda
                cont=-cont #como el contador está en negativo lo pasamos a positivo por comodidad
                for i in range(cont):
                    #como hay que recolocar cont nodos del lado izq haremos cont iteraciones
                    #esto es el algoritmo visto en clase para recolocar nodos llevado a codigo
                    if node.left!=None:
                        auxNode=node.left
                        while auxNode.right!=None:
                            auxNode=auxNode.right
                    else:
                        auxNode=node
                    if node.right==None:
                        orig=node.elem
                        nuevo=auxNode.elem
                        self._removeNode(auxNode)
                        node.elem=nuevo
                        self.insert(orig)
                    else:
                        print()
                        self._insertNode(node.right,node.elem)
                                
                        node.elem=auxNode.elem
                        self._removeNode(auxNode)
            #una vez está balanceado el nodo, invocamos a la funcion para su dercha e izquierda
            if node.left!=None:
                self._balance(node.left)
            if node.right!=None:
                self._balance(node.right)
            
################################################################################
    #funcion para comprobar si está balanceado un nodo o no 
    #O(n) Mejor caso: no hay nodo; peor caso: que exista nodo y opere        
    def _esBalanceada(self,node):
        if node==None:
            return True
        dif=self._size(node.right)-self._size(node.left)
        if dif<-1 or dif >1:
            return False
        else:
            return True
                       
################################################################################      
    
    #O(log2(n)) Mejor caso: el nodo ya existe; peor caso: sea crea el nodo y se compara    
    def _insertNode(self,node,x):
        """Inserts a new node (with the element x) inside of the subtree node"""
        if x._eq_(node.elem):
          # Duplicate elements are not allowed
          print(x,' already exists!!!')
          return

        if x._lt_(node.elem):
    
          if node.left==None:
            newNode=Node(x)
            node.left=newNode
            newNode.parent=node
          else:
            self._insertNode(node.left,x)
    
        else: #if x>node.elem
    
          if node.right==None:
            newNode=Node(x)
            node.right=newNode
            newNode.parent=node
          else:
            self._insertNode(node.right,x)
            