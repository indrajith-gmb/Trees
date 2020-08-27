

''' one way is to by verifying inorder traversal on the given tree if they are in sorted order or not '''

import sys

class Node:

	def __init__(self, data):
		
		self.left = None

		self.right = None

		self.data = data




def check(a, min, max):

	if(a==None):

		return True


	if(a.data <= min or a.data > max):
		return False

	
	if((check(a.left, min, a.data)) and ((a.right, a.data, max))):

		return True

	return False


root = Node(5)

root.left = Node(2)

root.right = Node(10)

root.right.right = Node(30)

min = -sys.maxsize-1

max = sys.maxsize

print(check(root, min, max))




