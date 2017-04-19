import sys

class Connections(object):
	def __init__(self, filename):
		try:
			self.input_stream = open(filename, 'r')
		except IOError as e:
			print "error: unable to open file '" +filename+ "'"
			sys.exit(1)
	def matrix(self):
		answer = []
		for line in self.input_stream.readlines():
			part = []
			for i in line.strip().split(','):
				part.append(int(i))
			answer.append(part)
		return answer