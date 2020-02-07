import numpy as np

def naive(limit, mults):
	"""Sum of all numbers less than limit that are multiples of [mults]"""
	total = 0
	for i in range(2, limit):
		for mult in mults:
			if i % mult == 0:
				total += i
				break
	return total


def faster(limit, mults):
    # Use the fact that sum of multiples of x below n can be written as
    # x * (1 + 2 + ... + floor(n/x)). With more than one multiple, though, we
    # need to remove cross products for double counting (i.e. 3 * 5 if using 3 and 5),
    # and with more than two multiples we need to add back 3-way multiples, etc.
    # The below uses binary representation to get all cross-products of multiples
    # then uses the sequential sum shortcut to add/subtract from the total.
    
    num_mults = len(mults)
    
    def get_combos(mults):
        # Get binary numbers to represent all combos of elements in mults
        bins = ['{:0{}b}'.format(i, num_mults) for i in range(1, (2 ** num_mults))]
        
        # Create lists for all combos. Also keep track of whether we are using
        # the combo to add or subtract from our total. Combos with odd number
        # of base multipliers add ot the total, even subtracts.
        combos = []
        signs = []
        for b in bins:
            use = [mults[i] for i in range(len(b)) if b[i] == '1']
            combos.append(np.product(use))
            signs.append(((-1)** (b.count('1') + 1)))
        return combos, signs
    
    combos, signs = get_combos(mults)
    total = 0
    
    for i in range(len(combos)):
        upper = np.floor(float(limit - 1) / combos[i])
        seq_sum = (upper * (upper + 1)) / 2
        total += signs[i] * (combos[i] * seq_sum)
    
    return total
        
        
    

if __name__ == "__main__":
	print(faster(1000, [3,5]))
    