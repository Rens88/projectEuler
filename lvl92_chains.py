
from supportScripts.tictoc import tic, toc
import timeit
from functools import reduce

def doit_n89(nn):

	n89 = 0
	printIt = False

	while True:
		
		nn = reduce(lambda s,d: s + int(d)**2, str(nn), 0)

		if nn == 89:
			n89 = 1
			if printIt:
				print('Found 89..')
			break

		elif nn == 1:
			n89 = 0

			if printIt:
				print('Found 1..')
			break

		if printIt:
			print('nn not yet 89 or 1 = %d' %nn)

	return n89

def doit(nnrange, printIt = False, method = 2):
	
	# nn = 10000000
	n89 = 0
	n1 = 0

	for nn in range(1,nnrange):
		while True:
			
			if method == 1:
				nn = sum(map(lambda dig: int(dig)**2, str(nn)))
			elif method == 2:
				nn = sum([int(dig)**2 for dig in str(nn)])
			elif method == 3:
				nn = reduce(lambda s,d: s + int(d)**2, str(nn), 0)

			if nn == 89:
				n89 += 1
				if printIt:
					print('Found 89..')
				break

			elif nn == 1:
				n1 += 1
				if printIt:
					print('Found 1..')
				break

			if printIt:
				print('nn not yet 89 or 1 = %d' %nn)

	return (n1, n89)

if __name__ == '__main__':

	nnrange = 100000

	t = tic()
	ans = doit(nnrange, printIt = False, method = 1)
	print('\nMethod 1:')
	print('n1  = %d\nn89 = %d' %ans)
	toc(t)
	t = tic()

	ans = doit(nnrange, printIt = False, method = 2)
	print('\nMethod 2:')
	print('n1  = %d\nn89 = %d' %ans)
	toc(t)

	t = tic()
	ans = doit(nnrange, printIt = False, method = 3)
	print('\nMethod 3:')
	print('n1  = %d\nn89 = %d' %ans)
	toc(t)
	
	t = tic()
	n89 = reduce(lambda s,nn: s + doit_n89(nn), range(1,nnrange), 0)
	print('\nMethod 3+:')
	print('n1  = XX\nn89 = %d' %n89)
	toc(t)
	
	
	# n1  = 1418853
	# n89 = 8581146
	# Elapsed time is 170.56654906 seconds.

	# totTime = timeit.timeit('doit()', 'from __main__ import doit', number = 100000)
	# print('Time using timeit: %.5f' %totTime)