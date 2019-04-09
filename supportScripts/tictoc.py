# Stolen from Dirk
# https://github.com/data-flux/project-euler/blob/master/Euler/tictoc.py

from time import time, sleep

def tic(tsleep = 0.000000000000001):

	t = time()
	sleep(tsleep)

	return (t, tsleep)

def toc(t):

	elapsed = time() - t[0] - t[1]

	print("Elapsed time is %.8f seconds." %elapsed)

	return elapsed