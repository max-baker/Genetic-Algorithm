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
	ga = GA.Populate(matrix, int(params[0]))
	
	maxIters = int(params[2])
	iters = 0
	while iters < maxIters:
		pairs = ga.topDown(int(params[0]/2))
		for n in pairs:
			ga.cycleXOver(n[0], n[1])
		ga.sortPop()
		#print ga.getCost(ga.population[0])
		ga.killBottom()
		iters += 1
	
if __name__ == '__main__':
	if len(sys.argv) != 1:
		print 'usage:', sys.argv[0]
		sys.exit(1)
	else:
		main()