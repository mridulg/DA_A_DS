#!/usr/bin/python3

# BinarySearchTree implemented in Python 3. 
# Note
# 1. In insert, the value goes to the left of the tree if it is less than the current node, right otherwise.
# 2. Delete function yet to be implemented

class Node:
	def __init__(self, value):
		self.l = None
		self.r = None
		self.val = value

class Tree:
	def __init__(self):
		self.root = None

	def getRoot(self):
		return self.root

	def addElement(self, value):
		if self.root == None:
			self.root=Node(value)
		else:
			self._addElement(value, self.root)

	def _addElement(self, value, node):
		if value < node.val:
			if node.l == None:
				node.l = Node(value)
			else:
				self._addElement(value, node.l)
		else:
			if node.r == None:
				node.r = Node(value)
			else:
				self._addElement(value, node.r)

	def printInorderTree(self):
		if(self.root != None):
			self._printInorderTree(self.root)

	def _printInorderTree(self, node):
		if(node != None):
			self._printInorderTree(node.l)
			print (str(node.val), end=',')
			self._printInorderTree(node.r)

	def printPreorderTree(self):
		if(self.root != None):
			self._printPreorderTree(self.root)

	def _printPreorderTree(self, node):
		if(node != None):
			print (str(node.val), end=',')
			self._printTree(node.l)
			self._printPreorderTree(node.r)

	def printPostorderTree(self):
		if(self.root != None):
			self._printPostorderTree(self.root)

	def _printPostorderTree(self, node):
		if(node != None):
			self._printPostorderTree(node.l)
			self._printPostorderTree(node.r)
			print(str(node.val), end=',')


#  Test tree

tree = Tree()
tree.addElement(3)
tree.addElement(4)
tree.addElement(0)
tree.addElement(8)
tree.addElement(2)
tree.printInorderTree()



