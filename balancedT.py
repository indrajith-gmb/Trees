

class Node:
	
	def __init__(self, val):
		
		self.left = None
		self.right = None
		self.val = val

	def insert(self, val):
	
		if(self.val):
			if(val < self.val):
				if(self.left is None):
					self.left = Node(val)
				else:
					self.left.insert(val)

			if(val > self.val):
				if(self.right is None):
					self.right = Node(val)
				else:
					self.right.insert(val)

		else:
			self.val = val

	
	def printT(self):
		list=[]
		if(self.left):
			self.left.printT()

		print(self.val)
		

		if(self.right):
			self.right.printT()



def getHeight(root):
		
	if(root is None):
		return 0
	return max(getHeight(root.left), getHeight(root.right))+1

	

def isBalanced(root):
		
	if(root is None):
		return True 
	
	heightDiff = getHeight(root.left) - getHeight(root.right)

	if(abs(heightDiff) > 1): 
		return False
	else:
		return (isBalanced(root.left) and isBalanced(root.right))





root = Node(15)
root.insert(20)
root.insert(10)
root.insert(30)
root.insert(40)
root.insert(50)
root.printT()

print(isBalanced(root))

