import sys
from random import randint

class Populate(object):
	def __init__(self, matrix, chromosomes, mutation):
		self.matrix = matrix
		self.genPop(chromosomes)
		self.sortPop()
		self.mutationOdds = mutation
	def genPop(self, numChromes):
		iteration = 0
		self.population = []
		while iteration < numChromes:
			self.population.append(self.genPerm())
			iteration += 1
	def genPerm(self):
		pool = [0,1,2,3,4,5,6,7]
		used = [0,0,0,0,0,0,0,0]
		answer = []
		n = 0
		while n < 8:
			index = randint(0,7)
			while used[index] != 0:
				index = randint(0,7)
			used[index] = 1
			answer.append(index)
			n += 1
		return answer
	def sortPop(self):
		cost = []
		for perm in self.population:
			cost.append(self.getCost(perm))
		self.population = self.msort(cost,self.population)
	def msort(self,cost,pop):
		size = len(cost)
		if size < 2:
			return pop
		mid = int(size/2)
		fcost = self.mhelper(cost[:mid])
		bcost = self.mhelper(cost[mid:])
		fpop = self.msort(cost[:mid],pop[:mid])
		bpop = self.msort(cost[mid:],pop[mid:])
		return self.merge(fcost,bcost,fpop,bpop)
	def mhelper(self,cost):
		size = len(cost)
		if size < 2:
			return cost
		mid = int(size/2)
		fcost = self.mhelper(cost[:mid])
		bcost = self.mhelper(cost[mid:])
		return self.merge(fcost,bcost,fcost,bcost)
	def merge(self,fcost,bcost,fpop,bpop):
		answer = []
		felems = len(fcost)
		belems = len(bcost)
		findex = 0
		bindex = 0
		while findex<felems and bindex<belems:
			if fcost[findex] > bcost[bindex]:
				answer.append(bpop[bindex])
				bindex += 1
			else:
				answer.append(fpop[findex])
				findex += 1
		answer += fpop[findex:]
		answer += bpop[bindex:]
		return answer
	def getCost(self,perm):
		n = 0
		answer = 0
		while n < 8:
			answer = answer+self.matrix[perm[n]][perm[(n+1)%8]]
			n += 1
		return answer
	def killBottom(self):
		size = len(self.population)
		mid = int(size/2)
		self.population = self.population[:mid]
		
	def topDown(self, numPairs):
		pairs = []
		n = 0
		while (n<numPairs*2):
			pairs.append((self.population[n],self.population[n+1]))
			n+=2
		return pairs
	def tournamentPairs(self, numPairs):
		pairs = []
		tSize = 8
		n = 0
		popSize = len(self.population)
		while n < numPairs:
			tournament = []
			k = 0
			while k < tSize:
				tournament.append(self.population[randint(0,popSize-1)])
				k += 1
			lowest = self.getCost(tournament[0])
			for perm in tournament:
				temp = self.getCost(perm)
				if temp < lowest:
					lowest = temp
			parent1 = perm

			tournament = []
			k = 0
			while k < tSize:
				tournament.append(self.population[randint(0,popSize-1)])
				k += 1
			lowest = self.getCost(tournament[0])
			for perm in tournament:
				temp = self.getCost(perm)
				if temp < lowest:
					lowest = temp
			parent2 = perm
			pairs.append((parent1,parent2))
			n += 1
		return pairs
	def orderedXOver(self,p1,p2):
		a= list(p1)
		b= list(p2)
		i = randint(0,4)
		j = i + randint(0,3)
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
		k = 0
		while k <= len(a)-1:
			if a[k] == -1:
				self.moveToFront(a,k)
			if b[k] == -1:
				self.moveToFront(b,k)
			k= k + 1
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
		self.mutate(a)
		self.mutate(b)
		self.population.append(a)
		self.population.append(b)
	def moveToFront(self,x, k):
		temp = x[k]
		while k >0 :
			x[k] = x[k-1]
			k = k-1
		x[0] = temp
	def cycleXOver(self,p1,p2):
		a= list(p1)
		b= list(p2)

		#swap first
		i = 0 
		temp = a[i]
		a[i] = b[i]
		b[i] = temp

		#Loop until no duplicate
		while self.checkDuplicates(i, a):
			i = self.duplicateIndex(i,a)
			temp = a[i]
			a[i] = b[i]
			b[i] = temp
		
		self.mutate(a)
		self.mutate(b)
		self.population.append(a)
		self.population.append(b)

	def checkDuplicates (self,i, p):
		k = 0
		while k < len(p):
			if k !=i:
				if p[k] == p[i]:
					return True
			k = k+1
		return False

	def duplicateIndex (self,i, p):
		k = 0
		while k < len(p):
			if k !=i:
				if p[k] == p[i]:
					return k
			k = k+1
		return -1

	def mutate(self,xs):
		mutationFactor = self.mutationOdds *100
		dieRoll = randint(1,100)
		if mutationFactor >= dieRoll: #Mutate (switch two random elements)
			i = randint(0,len(xs)-1)
			j = randint(0,len(xs)-1)
			while i == j:
				j = randint(0,len(xs)-1) #Re-Roll if equal
			temp = xs[i]
			xs[i] = xs[j]
			xs[j] = temp


		return