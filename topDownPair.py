#Name: Max Baker
#Date: 4/18/17

from random import randint


def topDown(pop, n):
	pairs = []
	i = 0
	while (i<n*2):
		pairs.append((pop[i],pop[i+1]))
		i+=2
	return pairs

def tourneyPairs(pop, n):
	pairs = []
	tourneySize = 4
	i=0
	while i < n:
		tourney = []
		j =0
		while j <tourneySize:
			tourney.append(pop[randint(0,len(pop)-1)])
			j += 1
		fit = fitness(tourney[0])
		for p in tourney:
			if fitness(p) > fit:
				fit = fitness(p)
		parent1 = p

		tourney = []
		j =0
		while j <tourneySize:
			tourney.append(pop[randint(0,len(pop)-1)])
			j += 1
		fit = fitness(tourney[0])
		for p in tourney:
			if fitness(p) > fit:
				fit = fitness(p)
		parent2 = p
		pairs.append((parent1,parent2))



		i+=1

	print pairs

def fitness(i):
	return i % 5

j=0
population = []
while j < 64:
	population.append(j)
	j += 1

tourneyPairs(population, 32)