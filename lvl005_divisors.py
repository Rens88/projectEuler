
def findDivisor(maxDiv = 10, upperLim = 3000, lowerLim = 0):
	for i in range(lowerLim,upperLim,1):

		for j in range(1,maxDiv):

			if i %j == 0:
				iFound = i
			else:
				iFound = []
				break

		if iFound != []:
			# Found it!
			break

	return iFound

maxDivs = range(10,21)
upperLim = 2000
lowerLim = 1

for j in range(1,21):
	if 20000139999840 %j ==0:
		print('%s = True' %j)
	else:
		print('%s = False' %j)

# Crappy as grid search solution
232792560
iFound = findDivisor(maxDiv = 20, upperLim = 20000139999840, lowerLim = 1)

print(iFound)

exit()

for m in maxDivs:
	iFound = []	
	while iFound == []:
		print('upperLim = %s' %upperLim)
		print('lowerLim = %s' %lowerLim)
		iFound = findDivisor(maxDiv = m, upperLim = upperLim, lowerLim = lowerLim)
		lowerLim = upperLim
		upperLim = upperLim*10


	print('Max divisor for <%s> = <%s>' %(m, iFound))