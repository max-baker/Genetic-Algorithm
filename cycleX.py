#Name: Max Baker
#Date: 4/18/17

def cycleXOver(a,b):
	p1 = list(a)
	p2 = list(b)

	#swap first
	i = 0 
	temp = a[i]
	a[i] = b[i]
	b[i] = temp

	#Loop until no duplicate
	while checkDuplicates(i, a):
		i = duplicateIndex(i,a)
		temp = a[i]
		a[i] = b[i]
		b[i] = temp

	print p1
	print p2
	print a
	print b

def checkDuplicates (i, p):
	k = 0
	while k < len(p):
		if k !=i:
			if p[k] == p[i]:
				return True
		k = k+1
	return False

def duplicateIndex (i, p):
	k = 0
	while k < len(p):
		if k !=i:
			if p[k] == p[i]:
				return k
		k = k+1
	return -1


	
x = [1,2,5,3,4,0,6,7]
y = [5,0,3,1,4,2,6,7]
cycleXOver(x,y)