"""A Hamming number is a positive number which has no prime factor larger than 5.
So the first few Hamming numbers are 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15.
There are 1105 Hamming numbers not exceeding 10^8.

We will call a positive number a generalised Hamming number of type n, if
it has no prime factor larger than n.
Hence the Hamming numbers are the generalised Hamming numbers of type 5.

How many generalised Hamming numbers of type 100 are there which don't exceed 10^9?

Answer: 2944730
Time: 17.7189998627s
"""

import time

def rec_thru(primes, i, product, limit, count):
    n = 0
    temp_product = product*(primes[i]**n)
    while temp_product <= limit:
        if i+1 < len(primes):
            count = rec_thru(primes, i+1, temp_product, limit, count)
        elif i+1 == len(primes):
            count += 1
        n += 1
        temp_product = product*(primes[i]**n)
    return count


def get_primes(limit):
    bin_primes = [0]*(limit+1)
    primes = []
    for i in xrange(2, limit+1):
        if bin_primes[i] == 0:
            primes.append(i)
            elim = i*2
            while elim <= limit:
                bin_primes[elim] = 1
                elim += i
    return primes

def run(hamm_type, limit):
    t0 = time.time()
    primes = get_primes(hamm_type)
    result = rec_thru(primes, 0, 1, limit, 0)
    print time.time()-t0
    print result

if __name__ == '__main__':
    run(100, 10**9)
