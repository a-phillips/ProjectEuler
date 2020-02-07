import time

#Original
def get_primes(limit):
	prime_index = [0]*(limit+1)
	primes = []
	for i in range(2, int(limit**.5)+1):
		if prime_index[i] == 0:
			j = 2*i
			while j < (limit+1):
				prime_index[j] = 1
				j += i
	for i, idx in enumerate(prime_index):
		if idx == 0 and i > 1:
			primes.append(i)
	return primes

def use_prime_list(num):
	t0 = time.time()
	primes = get_primes(int(num**.5)+1)
	i = 0
	while num != 1:
		while num % primes[i] == 0:
			num /= primes[i]
		i += 1
	print(time.time() - t0)
	print(primes[i-1])

#Faster
def use_check_all(num):
	t0 = time.time()
	i = 2
	while num != 1:
		while num % i == 0:
			num /= i
		i += 1
	print(time.time() - t0)
	print(i-1)

if __name__ == "__main__":
	limit = 600851475143
	use_prime_list(limit)
	use_check_all(limit)