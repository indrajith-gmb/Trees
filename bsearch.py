

''' def bsearch(list, val):

	i = 0
	n = len(list)-1


	while(i<=n):
		
		mid = (i+n)//2
		
		if(list[mid] == val):
			return mid

		elif(mid < val):
			i = mid + 1
		
		else:
			n = mid -1 

	if(i>n):
		return None 

list=input().split()

list.sort()

print(list)

list = [int(i) for i in list]

print(list)

print(bsearch(list, int(input()))) '''


def bsearch(list, val, i, n):

	if(len(list)<=0):
		return 0

	if(n < i):
		return None

	mid = (i+n)//2

	if(list[mid]==val):
		return mid

	elif(list[mid] < val):
		return bsearch(list, val, mid+1, n)

	elif(list[mid] > val):
		return bsearch(list, val, i, mid-1)
	
	else:
		return None	

	


list = [12,13,14,15]

val = 13
val1 = 9

print(bsearch(list, val, 0, 3))

print(bsearch(list, val1, 0, 3))





























	


