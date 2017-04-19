import sys

def main(parameters):
	try:
		params = open("params.txt", 'w')
		params.write(parameters[1]+'\n')
		params.write(parameters[2]+'\n')
		params.write(parameters[3]+'\n')
		params.write(parameters[4]+'\n')
		params.write(parameters[5])
		params.close()
	except IOError as e:
		print "error: unable to open file 'params.txt'"
		sys.exit(1)
		
if __name__ == '__main__':
	if len(sys.argv) != 6:
		print 'usage:', sys.argv[0], ' chromes_i', ' chromes', ' genes', ' mutfact', ' iters'
		sys.exit(1)
	else:
		main(sys.argv)