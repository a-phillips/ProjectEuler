import time

def primes(limit):
    prime_list = []
    sieve = [0]*(limit+1)
    for i in xrange(2, len(sieve)):
        if sieve[i] == 0:
            prime_list.append(i)
        j = 2*i
        while j <= limit:
            sieve[j] = 1
            j += i
    return prime_list

def M(p, q, N):
    max_num = 0
    p_fac = p
    while p_fac <= N:
        q_fac = q
        while p_fac*q_fac <= N:
            max_num = max(max_num, p_fac*q_fac)
            q_fac *= q
        p_fac *= p
    return max_num

def run(limit):
    t0 = time.time()
    prime_list = primes(limit/2)
    print 'Primes generated in', time.time()-t0
    S = 0
    for i in xrange(len(prime_list)-1):
        p = prime_list[i]
        if p**2 > limit:
            break
        for j in xrange(i+1, len(prime_list)):
            q = prime_list[j]
            if p*q > limit:
                break
            result = M(p, q, limit)
            #print prime_list[i], prime_list[j], result
            S += result
    print time.time()-t0
    print S
    

if __name__=='__main__':
    run(10000000)
