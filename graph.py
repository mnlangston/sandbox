class Node:
	def __init__(self,label):
		self.label=label
		self.children=[]

class Graph:
	def __init__(self):
		self.nodes=[]
		self.loadGraph()

	def loadGraph(self):
		fd = open(raw_input("Graph file: "))
		contents=fd.read().split('\n')
		nodeList=contents[:1]
		nodeMap=contents[1:]
		print "Node list:"
		print nodeList
		print "Node map:"
		print nodeMap #not yet a map

if __name__=="__main__":
	g = Graph()
