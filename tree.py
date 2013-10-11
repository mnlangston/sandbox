#!/usr/bin/env python
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BSTree:
    def __init__(self):
        self.root = None

    def insert(self,data):
        if self.root is None:
            self.root = Node(data)
            return
        iter = self.root
        done = False
        while not done:
            if data <= iter.data:
                if iter.left is None:
                    iter.left = Node(data)
                    done = True
                else:
                    iter = iter.left    
            else:
                if iter.right is None:
                    iter.right = Node(data)
                    done = True
                else:
                    iter = iter.right

    def inorder(self,node):
        if node is None: return
        self.inorder(node.left)
        print(node.data)
        self.inorder(node.right)

    def walk(self):
        self.inorder(self.root)

if __name__=="__main__":
    tree = BSTree()
    vals=[7,4,10,12,8,2,5]
    for i in vals:
        tree.insert(i)
    tree.walk()
