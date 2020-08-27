


class Node:

	def __init__(self, data):

		self.left = None 
		self.right = None
		self.data = data



lis = [] 

def inOrder(root):
	

	if(root is None):
		return None

	inOrder(root.left)

	lis.append(root.data)

	inOrder(root.right)




root = Node(10)

root.left = Node(5)

root.right = Node(20)

inOrder(root) 

print(lis)