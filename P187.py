import time

def make_primes(limit):
    primes = [0]*(limit+1)
    primes[0],primes[1] = 1,1
    prime_list = []
    for i in xrange(2,(limit/2)+1):
        if primes[i] == 0:
            prime_list.append(i)
            x = 2*i
            while x <= limit:
                primes[x] = 1
                x += i
    for i in xrange((limit/2)+1, limit+1):
        if primes[i] == 0:
            prime_list.append(i)
    return prime_list


def get_semiprimes(limit):
    primes = make_primes(limit/2)
    count = 0
    for i, base in enumerate(primes):
        for j in xrange(i, len(primes)):
            if base*primes[j] > limit:
                break
            count += 1
    return count

if __name__ == '__main__':
    t0 = time.time()
    count = get_semiprimes(10**8)
    print count
    print time.time()-t0

