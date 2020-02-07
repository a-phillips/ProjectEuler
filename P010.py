import time
from P3 import get_primes

if __name__ == "__main__":
	t0 = time.time()
	answer = sum(get_primes(2000000))
	print time.time() - t0
	print answer