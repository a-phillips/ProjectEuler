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

def get_next_prime(num):
    if num%2==0:
        num += 1
    else:
        num += 2
    prime = False
    while not prime:
        for i in xrange(3,int(num**.5)+2,2):
            if num%i == 0:
                break
        else:
            return num
        num += 2


def semidivisible_sum(limit):
    max_prime = get_next_prime(int(limit**.5))
    primes = make_primes(max_prime)
    total = 0
    count = 0
    for i in xrange(len(primes)-1):
        lps = primes[i]
        lower_bound = (lps**2)
        ups = primes[i+1]
        upper_bound = (ups**2)
        #Using two different processes for numbers that may potentially
        #exceed the limit. Didn't want to have to check size every time.
        if upper_bound < limit:
            to_add = lower_bound + lps
            while to_add < upper_bound:
                total += to_add
                count+= 1
                to_add += lps
            to_add = upper_bound - ups
            while to_add > lower_bound:
                total += to_add
                count += 1
                to_add -= ups
            total -= (lps*ups)*2
            count -= 2
        else:
            print 'In excessive'
            to_add = lower_bound + lps
            while to_add <= limit:
                total += to_add
                count += 1
                to_add += lps
            to_add = upper_bound - ups
            while to_add > lower_bound:
                if to_add <= limit:
                    total += to_add
                    count += 1
                to_add -= ups
            if (lps*ups) <= limit:
                total -= (lps*ups)*2
                count -= 2
    return total



if __name__ == '__main__':
    t0 = time.time()
    total = semidivisible_sum(999966663333)
    print time.time()-t0
    print total
    print 'Finished!'

