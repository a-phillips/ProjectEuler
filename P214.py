import time

def make_phis(limit):
    phi = dict(zip(range(2, limit+1), range(2, limit+1)))
    print 'base dict made'
    for i in xrange(2, limit+1):
        if phi[i] == i: #since phis starts at 2 and index starts at 0
            num = i+i  #this number will change
            while num <= limit:
                phi[num] *= (1-(1.0/i)) #num-2 because of index/number diff
                phi[num] = int(phi[num])
                num += i
            phi[i] -= 1
    return phi


def check_prime(n):
    for div in xrange(2, int((n**.5)+1)):
        if n%div == 0:
            return False
    return True


def run(chain, limit):
    t0 = time.time()
    
    chain_length = dict()
    chain_length[2] = 2
    
    phi = make_phis(limit)
    t1 = time.time()
    print t1-t0
    print 'phis made'
    print ''
    
    primes = []
    for num in xrange(3, limit+1):
        chain_length[num] = 1 + chain_length[phi[num]]
        if chain_length[num] == chain and check_prime(num) == True:
            primes.append(num)
            
    print time.time()-t1
    print primes
    print sum(primes)
    
    
if __name__ == '__main__':
    run(25, 40000000)
        
