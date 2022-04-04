# -*- coding: utf-8 -*-
import queue #it is Python module to implement queues
#from queue import SQueue

class Node:
  def __init__(self,elem,left=None,right=None,parent=None):
    self.elem=elem
    self.left=left
    self.right=right
    self.parent=parent
    
    
class BinaryTree:
  
  def __init__(self):
    self.root=None

  def size(self):
    """Returns the number of nodes"""
    return self._size(self.root)

  def _size(self,node):
    "función recursiva de vuelve el tamaño de node"
    if node==None:
      return 0
      
    return 1 + self._size(node.left) + self._size(node.right)

  def height(self):
    """Returns the height of the tree"""
    return self._height(self.root)
  
  def _height(self,node):
    "función recursiva que devuelva la altura del nodo"
    if node==None:
      return -1

    return 1 + max(self._height(node.left),self._height(node.right))

  
  def depth(self,node):
    if node==None:
      return 0

    if node.parent==None: 
      #node==self.root
      return 0
    
    return 1 + self.depth(node.parent)

  def preorder(self):
    self._preorder(self.root)
    
  def _preorder(self,node):
    if node!=None:
      print(node.elem)
      self._preorder(node.left)
      self._preorder(node.right)

      
  def postorder(self):
    self._postorder(self.root)
    
  def _postorder(self,node):
    if node!=None:
      self._postorder(node.left)
      self._postorder(node.right)
      print(node.elem)
      
  def inorder(self):
    self._inorder(self.root)

  def _inorder(self,node):
    if node!=None:
      self._inorder(node.left)
      print(node.elem)
      self._inorder(node.right)
     
  def levelorder(self):
    if self.root==None:
      print('tree is empty')
      return
    
    q=queue.Queue()
    q.put(self.root) #enqueue: we save the root
    
    while q.empty()==False:
      current=q.get() #dequeue
      print(current.elem)
      if current.left!=None:
        q.put(current.left)
      if current.right!=None:
        q.put(current.right)