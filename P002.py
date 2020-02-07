def sum_even_fib(limit):
    # Every 3rd term is even
	total = 0
	a, b = 1, 1
	count = 0
	while a + b < limit:
		if count == 0:
			total += (a+b)
		if count == 2:
			count = 0
		else:
			count += 1
		a, b = b, a + b
		
	print(total)
	
if __name__ == "__main__":
	sum_even_fib(4000000)