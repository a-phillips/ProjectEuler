import time

def collatz(num, check):
	length = 1
	while num != 1:
		if num % 2 == 0:
			num /= 2
		else:
			num = (3 * num) + 1
		if check.get(num):
			length += check[num]
			break
		else:
			length += 1
	return length
	
def longest_collatz(limit):
	check = {}
	max_len = 0
	max_num = 0
	for i in xrange(2, limit):
		curr_len = collatz(i, check)
		if curr_len > max_len:
			max_len = curr_len
			max_num = i
		check[i] = curr_len
	return max_num, max_len
	
if __name__ == "__main__":
	t0 = time.time()
	answer = longest_collatz(1000000)
	print time.time() - t0
	print answer