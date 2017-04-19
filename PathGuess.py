import sys
import GetMatrix
import GetParams
import GA

def main():
	#lower bound is 4135
	#upper bound is 16417
	getm = GetMatrix.Connections("connections.txt")
	matrix = getm.matrix()
	getp = GetParams.Parameters("params.txt")
	params = getp.params()
	ga = GA.Populate(matrix, int(params[1]))
	
	maxIters = int(params[4])
	iters = 0
	while iters < maxIters:
		pairs = ga.topDown(int(params[1]/2))
		for n in pairs:
			ga.cycleXOver(n[0], n[1])
		ga.sortPop()
		ga.killBottom()
		iters += 1
	print ga.getCost(ga.population[0])
	
if __name__ == '__main__':
	if len(sys.argv) != 1:
		print 'usage:', sys.argv[0]
		sys.exit(1)
	else:
		main()