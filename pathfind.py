

class Graph:

	def __init__(self, gdict = None):

		if(gdict is None):
			gdict = {}

		self.gdict = gdict 


	def findedges(self):
		edgename = []
		
		for i in self.gdict:
			for j in self.gdict[i]:
				if({i, j} not in edgename):
					edgename.append({i, j})
		
		return edgename

	def edges(self):
		return self.findedges()


def dfs(graph, start, visited = None):
	
	if(visited is None):
		visited = set()

	
	visited.add(start)

	print(start)

	for v in graph[start] - visited: 

		dfs(graph, v, visited)
	
	return visited 

	

ge = { "a":["b", "c"],
	"b":["a", "d"],
	"c":["a", "d"],
	"d":["e"],
	"e":["d"]
}



g = Graph(ge)

print(g.edges()) 


find = dfs(ge, "a")

print(find) 









