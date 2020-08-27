


class Node:

	def __init__(self, data):

		self.left = None
		self.right = None	
		self.data = data 


	
	
def bST(arr):

	if(not arr):
		return None 
		
	mid = (len(arr))//2

	root = Node(arr[mid])	

	root.left = bST(arr[:mid])

	root.right = bST(arr[mid+1:])

	return root


def preOrder(root):

	if(not root):
		return None
	
	print(root.data)

	preOrder(root.left)

	preOrder(root.right)


arr = [1,2,3,4,5,6,7]

r = bST(arr)


preOrder(r)




			






