from supportScripts.tictoc import tic, toc

"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

Strategy:
Generate the largest palindromes possible.
Check for each palinderome if it has two 3 digit factors.

"""

t = tic()
nlimit = 100
nCount = 0
foundIt = []
for k in range(9,0, -1):
	for j in range(9,-1, -1):
		for i in range(9,-1, -1):
			# To make generic, str(i) can occur once and twice
			# The current palindrome
			curPal = int(str(k) + str(j) + str(i) + str(i) + str(j) + str(k))
			
			nCount += 1

			# is it dividable by a 3 digit number
			for q in range(999,0,-1):
				if (curPal / q) > 1000:
					# No 3 factor for curPal
					break

				if (curPal / q) < 100:
					# No 3 factor for curPal
					continue

				if curPal %q == 0:
					# Found it!
					foundIt = q
					break

			if foundIt != []:
				break

			if nCount == nlimit:
				# Just to avoid going forever
				print('limit reached. Change nlimit, or make code more efficient.')
				break
		if foundIt != []:
			break
	if foundIt != []:
		break

# Print the time
toc(t)

oth = curPal / foundIt

print('The palinderome <%d> consists of the factors <%d> and <%d>.' %(curPal, foundIt, oth))
exit()