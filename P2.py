def sum_even_fib(limit):
	total = 0
	a, b = 1, 1
	count = 0
	while a + b < limit:
		#print a + b, count
		if count == 0:
			total += (a+b)
			#print "Adding: ",(a+b), total
		if count == 2:
			count = 0
		else:
			count += 1
		a, b = b, a + b
		
	print total
	
if __name__ == "__main__":
	sum_even_fib(4000000)