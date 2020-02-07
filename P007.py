import time

def check_prime(num):
	i = 2
	while i**2 <= num:
		if num % i == 0:
			return False
		i += 1
	return True

def get_nth_prime(n):
	if n == 1:
		return 2
	elif n == 2:
		return 3
	else:
		num_primes = 2
		check_num = 5
		inc_by = 2
		while True:
			if check_prime(check_num):
				num_primes += 1
				if num_primes == n:
					return check_num
			check_num += inc_by
			if inc_by == 2:
				inc_by == 5
			else:
				inc_by == 2

if __name__ == "__main__":
	t0 = time.time()
	answer = get_nth_prime(10001)
	print(time.time() - t0)
	print(answer)