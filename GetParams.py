import sys

class Parameters(object):
	def __init__(self, filename):
		try:
			self.input_stream = open(filename, 'r')
		except IOError as e:
			print "error: unable to open file '" +filename+ "'"
			sys.exit(1)
	def params(self):
		answer = []
		for line in self.input_stream.readlines():
			answer.append(float(line))
		return answer