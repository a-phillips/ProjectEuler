import time

def make_phis(limit):
    t0 = time.time()
    phi = range(2, limit+1)
    for i in xrange(len(phi)):
        if phi[i] == (i+2): #since phis starts at 2 and index starts at 0
            num = (i+2)+(i+2)  #this number will change
            while num <= limit:
                phi[num-2] *= (1-(1.0/(i+2))) #num-2 because of index/number diff
                num += (i+2)
            phi[i] -= 1
    print time.time() - t0
    print sum(phi)
            


if __name__ == '__main__':
    make_phis(1000000)
        
