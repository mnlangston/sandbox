#!/usr/bin/env python
class Node:
    def __init__(self,data):
        self.data = data
        self.children = []

    def addChild(n):
        self.children.append(n)
    def addLeftChild(n):
        self.children.setitem(0,n)
    def addRightChild(n):
        self.children.setitem(1,n)

class BSTree:
    def __init__(self):
        self.root = None

    def insert(self,data):
        if self.root is None:
            self.root = Node(data)
            return
        iter = self.root
        while iter is not None:
            if data <= iter.data:
                if iter.children[0] is None:
                    iter.addLeftChild(n)
                else:
                    iter = iter.children[0]
            else:
                if iter.children[1] is None:
                    iter.addRightChild(n)
                else:
                    iter = iter.children[1]

    def inorderPrint(self,n):
        if n is None: return
        self.inorderPrint(n.children[0])
        print(n.data)
        self.inorderPrint(n.children[1])
    def walk(self):
        self.inorderPrint(self.root)

if __name__=="__main__":
    tree = BSTree()
    tree.insert(7)
    tree.insert(4)
    tree.insert(10)
    tree.walk()
