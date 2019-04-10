import math
from supportScripts.tictoc import tic, toc

def main(n = 10001, listrange = 10):

	# Starting at 2, until n 
	n_list = set(range(2,listrange))

	# Loop over all integeres
	primes = [] # store all primes in a list
	nthPrime = 0
	solvedIt = False
	for p in n_list.copy():
		if not p in n_list:
			# Not a prime, as p was already dropped from the list
			continue

		n_list = dropNonPrimes(p, n_list)
		
		# p is a prime!
		nthPrime += 1
		if nthPrime == n:
			solvedIt = True
			break

	if not solvedIt:
		p = -1
		print('Couldnt solve it. Use larger range.')

	return p

def dropNonPrimes(p, n_list):

	for n in n_list.copy():
		if n %p == 0:
			n_list.remove(n)

	return n_list

t = tic()
n=10001
p = main(n=n, listrange = n*200)
toc(t)
print('The %dth Prime = %d' %(n,p))
	