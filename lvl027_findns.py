from functools import reduce
from operator import mul
import math
from supportScripts.tictoc import tic, toc

def dropNonPrimes(p, n_list):

	for n in n_list.copy():
		if n %p == 0:
			n_list.remove(n)

	return n_list

def findPrimes(n):
	n_list = set(range(2,n+1))

	# Loop over all integeres
	primes = [] # store all primes in a list
	for p in n_list.copy():
		if not p in n_list:
			# Not a prime, as p was already dropped from the list
			continue

		n_list = dropNonPrimes(p, n_list)
		# p is a prime!
		primes.append(p)

	return primes

def computeFormula(primes, a, b, startingN = 40, maxN = 1000, printStuff = False):

	largestPrime = -1
	largestN = -1
	
	for n2 in range(maxN - startingN):

		n = n2 + startingN

		cur = n**2 + a * n + b

		if cur not in primes:
			if n != startingN:

				largestN = n - 1
				largestPrime = (n-1)**2 + a * (n-1) + b
			else:
				if printStuff:
					print('WARNING: Did not converge...')

			break

	if printStuff:
		if largestN == -1:
			print('WARNING: No n found. For a = <%d> and b = <%d>' %(a, b))

		else:
			print('For a = <%d> and b = <%d>:' %(a, b))
			print('largestN = %d' %largestN)
			print('largestPrime = %d' %largestPrime)

	return largestN

def test(a = None, b = None, n = 10000):
	
	primes = findPrimes(n)

	largestN = \
	computeFormula(primes, a, b, printStuff = True, startingN = 20)


def checkIt(primes, a, b, largestN_soFar, largestN_a, largestN_b):
	largestN = \
	computeFormula(primes, a, b, printStuff = False, startingN = 20)

	if largestN > largestN_soFar:

		largestN_soFar = largestN
		largestN_a = a
		largestN_b = b
		print('a = %d, b = %d, largestN = %d' %(a,b,largestN))

	return largestN_soFar, largestN_a, largestN_b

def search(n = 10000):

	primes = findPrimes(n)

	largestN_soFar = 0
	largestN_a = 1
	largestN_b = 1


	for b in primes:
		if b >= 1000:
			# Made it to the threshold
			print('Found the first prime over 1000: %d' %b)
			break

		for atmp in range(1000):
			# a =  # a moet oneven zijn.			
			a = atmp*2 + 1

			largestN_soFar, largestN_a, largestN_b = checkIt(primes, a, b, largestN_soFar, largestN_a, largestN_b)
			largestN_soFar, largestN_a, largestN_b = checkIt(primes, -a, b, largestN_soFar, largestN_a, largestN_b)

	return largestN_a, largestN_b

t = tic()

## test cases
test(a = 1, b = 41)
test(a = -79, b = 1601)

## The real assignment
print('\n\n*************\nAND NOW THE REAL DEAL:')
largestN_a, largestN_b = search()

print('The product is of <%s> and <%s> is:' %(largestN_a, largestN_b))
print(largestN_a * largestN_b)

toc(t)