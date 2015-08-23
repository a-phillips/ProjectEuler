def get_sum(limit, mults):
	"""Sum of all numbers less than limit that are multiples of [mults]"""
	total = 0
	for i in xrange(2, limit):
		for mult in mults:
			if i % mult == 0:
				total += i
				break
	return total

if __name__ == "__main__":
	print get_sum(1000, [3, 5])