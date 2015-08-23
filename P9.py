import time

def get_pythag_triplet(total):
	for a in xrange(1, 333):
		for b in xrange(a, 1000-a):
			c = 1000 - a - b
			#print a, b, c
			if c < b:
				break
			elif (a**2) + (b**2) == (c**2):
				return a*b*c

if __name__ == "__main__":
	t0 = time.time()
	answer = get_pythag_triplet(1000)
	print time.time() - t0
	print answer