import time

def sum_of_squares(limit):
	return sum([x**2 for x in range(limit+1)])

def square_of_sum(limit):
	return sum(range(limit+1))**2

if __name__ == "__main__":
	t0 = time.time()
	limit = 100
	a = sum_of_squares(limit)
	b = square_of_sum(limit)
	print(time.time() - t0)
	print(b - a)