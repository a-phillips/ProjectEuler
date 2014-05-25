import time

def make_phis(limit):
    phi = range(2, limit+1)
    for i in xrange(limit-1):
        num = i+2
        if phi[i] == num:
            multiple = (num*2)
            while multiple <= limit:
                phi[multiple-2] *= (1-(1.0/num)) #multiple-2 because of index/number diff
                phi[multiple-2] = int(phi[multiple-2])
                multiple += num
            phi[i] -= 1
    return phi


def run(limit, max_d):
    t0 = time.time()
    min_ratio = 1
    phi = make_phis(limit)
    print 'phis made'
    for i in xrange(limit-1):
        ratio = phi[i]/float((i+2)-1)
        if ratio < min_ratio:
            min_ratio = ratio
        if ratio < max_d:
            print time.time()-t0
            print i+2
            print ratio
            return None
    print max_d
    print min_ratio
    print time.time()-t0

if __name__ == '__main__':
    run(1000000000, float(15499)/94744)
