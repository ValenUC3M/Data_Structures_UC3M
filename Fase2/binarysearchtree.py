# -*- coding: utf-8 -*-
from binarytree import BinaryTree
from binarytree import Node

class BinarySearchTree(BinaryTree):

  def search(self,x):
    """Returns True if x exists into the tree, eoc False"""
    return self._searchNode(self.root,x)
    
  def _searchNode(self,node,x):
    """Auxiliary method to search a node with value x"""
    if node is None:
      return None
              
    if node.elem==x:
      return node.elem
        
    if x<node.elem:
      return self._searchNode(node.left,x)
        
    if x>node.elem:
      return self._searchNode(node.right,x)



  def insert(self,x):
    """inserts a new node, with element x, into the tree"""
    if self.root==None:
      self.root=Node(x)
    else:
      self._insertNode(self.root,x)

  def _insertNode(self,node,x):
    """Inserts a new node (with the element x) inside of the subtree node"""
    if node.elem==x:
      # Duplicate elements are not allowed
      print(x,' already exists!!!')
      return
        
    if x<node.elem:

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
      

 
  def find(self,x):
    """Returns the ndoe whose element is x. If it is not found, it returns None"""
    return self._findNode(self.root,x)
    
  def _findNode(self,node,x):
    if node is None:
      return None
        
    if node.elem==x:
      return node
        
    if x<node.elem:
      return self._findNode(node.left,x)
        
    if x>node.elem:
      return self._findNode(node.right,x)      
          
  def remove(self,x):
    """Searches and removes the node whose element is x"""
    node=self.find(x)
    if node is None:
      #print(x,' does not exist!!!')
      return
    
    #print('removing ', x)
    self._removeNode(node)
        
  def _removeNode(self,node): 
    """Auxiliary method to remove the node which takes as parameter"""
    #First case: no children
    if node.left==None and node.right==None:
      if node.parent != None:
        
        if node.parent.left==node:
          node.parent.left=None
          
        else:
          node.parent.right=None
        node.parent=None

      else: #if parent_node is  None:
        self.root=None
      return
        
    #Second case: only one child, the left child
    if node.left!=None and node.right==None:
      
      if node.parent!=None:
        if node.parent.left==node:
          node.parent.left=node.left
        else:
          node.parent.right=node.left
        
        node.left.parent=node.parent
      
      else:#if parent_node is not None:
        self.root=node.left
        self.root.parent = None
      return
        
    #Second case: only one child, the right child
    if node.left==None and node.right!=None:
      
      if node.parent!=None:
        if node.parent.left==node:
          node.parent.left=node.right
        else:
          node.parent.right=node.right
        
        node.right.parent=node.parent
      else:
        self.root=node.right
        self.root.parent = None
      return
            
    #Third case: two children
    successor=node.right
    while successor.left!=None:
      successor=successor.left
            
    #we replace the node's elem by the successor's elem
    node.elem=successor.elem
    #we remove the succesor from the tree
    self._removeNode(successor)
        
  def draw(self):
      """Fucntion to draw a tree"""
      self._draw('',self.root,False)
      print()
      
  def _draw(self,prefix, node, isLeft):
    if node !=None:
        self._draw(prefix + "     ", node.right, False)
        print(prefix + ("|-- ") + str(node.elem))
        self._draw(prefix + "     ", node.left, True)
#
#import random
#tree=BinarySearchTree()
#for i in range(20):
#  tree.insert(random.randint(0,25))
#print()
#
#tree.draw()
#print('size:',tree.size())
#print('height:',tree.height())
#
#x=random.randint(0,25)
#if tree.search(x):
#  print(x, ' exists!!!')
#  tree.remove(x)
#  print('after removing ',x)
#  tree.draw()
#else:
#  print(x, ' does not exist!!!')
#  tree.insert(x)
#  print('after inserting ',x)
#  tree.draw()
#
#
#print('inorder')
#tree.inorder()
#
#print('postorder')
#tree.postorder()
#
#print('levelorder')
#tree.levelorder()
#
#print('preorder')
#tree.preorder()