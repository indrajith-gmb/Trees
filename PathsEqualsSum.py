

class Node:

	def __init__(self, data):

		self.left = None
		self.right = None
		self.data = data


def printkPath(root, k):

	path = []

	printkPathUtil(root, path, k)


def printkPathUtil(root, path, k):

	if(root is None):

		return None

	path.append(root.data)

	printkPathUtil(root.left, path, k)
	printkPathUtil(root.right, path, k)

	f = 0

	for j in range(len(path)-1, -1, -1):
		f +=path[j]

		if(f == k):
			printVector(path, j)

	path.pop(-1)


def printVector(v, i):
	for j in range(i, len(v)):
		print(v[j], end= " ")
	print()



root = Node(1)  
root.left = Node(3)  
root.left.left = Node(2)  
root.left.right = Node(1)  
root.left.right.left = Node(1)  
root.right = Node(-1)  
root.right.left = Node(4)  
root.right.left.left = Node(1)  
root.right.left.right = Node(2)  
root.right.right = Node(5)  
root.right.right.right = Node(2)  
  
k = 5
printkPath(root, k) 



