#/usr/bin/env python
class Node:
	def __init__(self,label):
		self.label=label
		self.children=[]

class Graph:
	def __init__(self):
		self.nodes=[]
		self.nodemap={}
                self.loadGraph()

	def find(self,label):
		for i in self.nodes:
			if i.label is label:
				return i
		return None
	def first(self):
		return self.nodes[0]

	def printMap(self):
		print "=== constructed table ==="
		for i in range(0,len(self.nodes)):
			print "Node "+str(self.nodes[i].label)+" is connected to:"
			for j in self.nodes[i].children:
				print "--->"+str(j.label)
				

	def loadGraph(self):
		fd = open(raw_input("Graph file: "))
		contents=fd.read().split('\n')
		nodeList=contents[:1]
		nodeList = nodeList[0].split(" ")
		print nodeList
		mapList=contents[1:-1]
		#build node map and create node objects
		for i in mapList:
			self.nodemap[i[0]]=tuple(i[1:].replace(" ",""))
		for i in nodeList:
			self.nodes.append(Node(i))
		#add children
		for i in self.nodes:
			for j in self.nodemap[i.label]:

				i.children.append(self.find(j))
	def depthFirstSearch(self,val,start):
		visited = [] 
		stack = []
		current = None
		stack.append(start)
		while stack:
			current = stack.pop()
			visited.append(current)
			for c in sorted(current.children,reverse=True):
				if c.label is val: 
					return True
				if c not in visited and c not in stack: 
					stack.append(c)
		return False

if __name__=="__main__":
	g = Graph()
	g.printMap()
	val=raw_input("Search for what value: ")
	if g.depthFirstSearch(val,g.first()):
		print "Found it"
	else:
		print "Not found"
