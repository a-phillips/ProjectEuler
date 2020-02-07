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


def find_min_X(D):
    X = 2
    while True:
        Y = 1
        possible = True
        while possible:
            diff = (X**2) - (D*(Y**2))
            if diff == 1:
                return X
            if diff < 1:
                possible = False
            Y += 1
        X += 1


def run(limit):
    t0 = time.time()
    primes = make_primes(limit)
    Xs = []
    for D in primes:
        results = find_min_X(D)
        Xs.append(results)
        D += 1
    print time.time() - t0
    print max(Xs)
    print primes[Xs.index(max(Xs))]


if __name__ == '__main__':
    run(200)

