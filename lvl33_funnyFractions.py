from supportScripts.tictoc import tic, toc
t = tic()
for b in range(1,10):
	for d in range(1,10):		
		for a in range(1,d):

			if 9*a*d + (-10*a + d) * b  == 0:
				print("%d%d/%d%d"%(a,b,b,d))

			if 9*a*d + (10*b-a)*b == 0:
				print("%d%d/%d%d"%(b,a,d,b))
toc(t)