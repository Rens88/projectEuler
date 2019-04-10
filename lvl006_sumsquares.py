from supportScripts.tictoc import tic, toc
t = tic()
sumsquares = 0
squaredsum = 0
for i in range(1,101):
	sumsquares += i**2
	squaredsum += i

squaredsum = squaredsum**2
answer = squaredsum - sumsquares
toc(t)

print('squaredsum = %d' %squaredsum)
print('sumsquares = %d' %sumsquares)

print('answer = %d' %answer)
