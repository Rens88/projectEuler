from supportScripts.tictoc import tic, toc

t = tic()

prev0 = 1
prev1 = 1

fiboSum = 0

while True:
	cur = prev0 + prev1

	if cur %2 == 0:
		fiboSum += cur
		
	prev0 = prev1
	prev1 = cur

	if cur > 4000000:

		break
toc(t)

print('cur = %d' %cur)
print('fiboSum = %d' %fiboSum)