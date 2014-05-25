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

def find_first(limit):
    primes = make_primes(1000000)
    for n, prime in enumerate(primes):
        num = ((prime-1)**n)+((prime+1)**n)
        den = prime**2
        rem = num%den
        if rem > limit:
            print num, den, n, prime, rem
            break

if __name__ == '__main__':
    t0 = time.time()
    find_first(10**10)
    print time.time()-t0
