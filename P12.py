import time

def calc_num_divisors(number):
	max_check = int(number**.5)+1
	num_divs = 2
	for i in xrange(2, max_check):
		if number % i == 0:
			num_divs += 2
			if number == i*i:
				num_divs -= 1
	return num_divs
	
def first_tri(limit):
	tri = 3
	inc_by = 3
	while calc_num_divisors(tri) < limit:
		tri += inc_by
		inc_by += 1
	return tri

if __name__ == "__main__":
	t0 = time.time()
	answer = first_tri(500)
	print time.time() - t0
	print answer
	
	