import time

def is_pal(num):
	return str(num)[::-1] == str(num)

def prod_three(num):
	i = 999
	while i > (num/1000):
		if num % i == 0:
			return True
		i -= 1
	return False

if __name__ == "__main__":
	t0 = time.time()
	for i in xrange(999*999, 100*100, -1):
		if is_pal(i) and prod_three(i):
			print time.time() - t0
			print i
			break
		
	