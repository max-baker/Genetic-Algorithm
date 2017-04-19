#Name: Max Baker
#Date: 4/18/17
from random import randint

def orderdXOver(a,b):
	p1 = list(a)
	p2 = list(b)
	i = randint(0,4)
	j = i + randint(0,3)
	print i
	print j
	p = []
	q = []
	i1 = i
	#Cross-Over
	while i <= j:
		p.append(a[i])
		q.append(b[i])
		temp = b[i]
		b[i] = a[i]
		a[i] = temp
		i = i+1

	#Find Duplicates
	k=0
	while k<i1:
		if a[k] in q:
			a[k] = -1
		if b[k] in p:
			b[k] = -1
		k = k +1

	k = j+1
	while k<len(p1):
		if a[k] in q:
			a[k] = -1
		if b[k] in p:
			b[k] = -1
		k = k +1

	#Move Blanks to front
	k = 7
	while k >= 0:
		if a[k] == -1:
			moveToFront(a,k)
		if b[k] == -1:
			moveToFront(b,k)
		k= k - 1

	#Sub In
	k = 0
	l = 0 
	while a[k] == -1:
		if p[l] not in a:
			a[k] = p[l]
			k = k+1
			l= l+1
		else: 
			l = l+1

	
	k = 0
	l = 0 
	while b[k] == -1:
		if q[l] not in b:
			b[k] = q[l]
			k = k+1
			l=l+1
		else: 
			l = l+1
	

	print a
	print b
	print p1
	print p2
	

def moveToFront(x, k):
	temp = x[k]
	while k >0 :
		x[k] = x[k-1]
		k = k-1
	x[0] = temp


x = [0,1,2,3,4,5,6,7]
y = [6,7,2,0,5,3,1,4]
orderdXOver(x,y)