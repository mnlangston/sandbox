class Node:
    __init__(self,data):
        self.data = data
        self.children = []

    def addChild(n):
        self.children.append(n)

class BSTree:
    __init__(self):
        self.root = None

    def addNode(n,data):
        iter = self.root
        if iter is None:
            self.root = Node(data)
        else:
            if data <= iter.data:
                if iter.children[0] is None:
                    iter.addChild(
