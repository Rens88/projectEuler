import math
from supportScripts.tictoc import tic, toc

def main(factorizeThis, n = None, printStuff = False):

	if n == None:
		
		# Create an upper limit based on the requested number to be factorized
		n = round(math.sqrt(factorizeThis))

	# Starting at 2, until n 
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

	if printStuff:
		print('These are the primes:\n%s' %primes)

	## Now use the list of primes to find the factorization of factorizeThis
	# Store the factors in a list
	primeFactors = []

	while True:

		smallestP = findSmallestPrimeDivider(factorizeThis, primes)

		if smallestP == -1:
			break

		factorizeThis = factorizeThis / smallestP
		
		primeFactors.append(smallestP)
		if printStuff:
			print('Factor found: %d' %smallestP)

	if not round(factorizeThis) == 1:
		print('WARNING: Search not complete. Still <%s> remaining to factorize... Set n manually, larger than <%d>.' %(factorizeThis, n))

	return primeFactors

##########################################
#########################################

def dropNonPrimes(p, n_list):

	for n in n_list.copy():
		if n %p == 0:
			n_list.remove(n)

	return n_list

def findSmallestPrimeDivider(factorizeThis, primes):
	
	smallestP = -1
	
	for p in primes:
		if factorizeThis %p == 0:
			smallestP = p
			break

	return smallestP

if __name__ == "__main__":

	t = tic()
	
	# Specify number to be factorized
	factorizeThis = 600851475143 

	# Specify the upper limit
	n = round(math.sqrt(factorizeThis) / 113)

	primeFactors = main(factorizeThis, printStuff = False, n = n)
	toc(t)

	print('\n\nprimeFactors:\n%s\n\n' %primeFactors)
	