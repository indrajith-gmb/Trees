

from collections import defaultdict

class Graph:

	def __init__(self, vertices):
		
		self.v = vertices 
		self.graph = defaultdict(list)


	def addEdge(self, u, v):
		self.graph[u].append(v)


	def isReachable(self, s, d):

		visited = [False] * (self.v)
	
		#print(visited) 

		queue = []

		queue.append(s)

		#print(queue)

		visited[s] = True
		
		while(queue):
			
			n = queue.pop(0)

			#print(n)

			if(n == d):
				return True


			for i in self.graph[n]:
				if(visited[i] == False):
					queue.append(i)
					visited[i] = True 

			
		return False


g = Graph(4)

g.addEdge(0,1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)


u = 1
v = 3


if(g.isReachable(u, v)):
	
	print("path is there")

else:
	print("path not available")

if(g.isReachable(3, 2)):

	print("path is there")

else:
	print("path is not available")








