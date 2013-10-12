#!/usr/bin/env python
class Node:
	def __init__(self,data):
		self.root = self.left = self.right = None
		self.data = data
		
class BSTree:
	def __init__(self):
		self.root=None
		
	def insert(self,data):
		if self.root is None:
			self.root = Node(data)
			return
		iter=self.root
		done=False
		while not done:
			if data < iter.data:
				if iter.left is None:
					iter.left = Node(data)
					done=True
				else:
					iter = iter.left
			else:
				if iter.right is None:
					iter.right = Node(data)
					done=True
				else:
					iter = iter.right

	def inorderWalk(self,node=-1,depth=0):
		if node is -1: node = self.root
		if node is None: return
		self.inorderWalk(node.left,depth+1)
		print (" "*depth)+str(node.data)
		self.inorderWalk(node.right,depth+1)

	def preorderWalk(self,node=-1,depth=0):
		if node is -1: node = self.root
		if node is None: return
		print (" "*depth)+str(node.data)
		self.preorderWalk(node.left,depth+1)
		self.preorderWalk(node.right,depth+1)

	def find(self,n,node=-1):
		if node is -1: node = self.root	
		if node is None: return False
		if node.data is n: return True
		else:
			if n < node.data:
				return self.find(n,node.left)
			else:
				return self.find(n,node.right)

if __name__=="__main__":
	T = BSTree();
	vals = [7,4,2,3,10,8,12]
	for i in vals:
		T.insert(i)
	#T.inorderWalk();
	T.preorderWalk();
	n=input("Find what value:")
	if T.find(n):
		print "I found it!"
	else:
		print "No Cigar..."
