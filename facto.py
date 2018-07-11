import math
import fileinput
for line in fileinput.input():
	n = int(line)
	if (n == 0) or (n == 1):
		print('1' )
	else:
		print('%d' % math.factorial(n) )
