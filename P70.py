import time

def make_phis(limit):
    t0 = time.time()
    phi = range(2, limit+1)
    for i in xrange(len(phi)):
        if phi[i] == (i+2): #since phis starts at 2 and index starts at 0
            num = (i+2)+(i+2)  #this number will change
            while num <= limit:
                phi[num-2] *= (1-(1.0/(i+2))) #num-2 because of index/number diff
                phi[num-2] = int(phi[num-2])
                num += (i+2)
            phi[i] -= 1
    return phi

def check_perm(n, m):
    n_nums = []
    m_nums = []
    while n > 0:
        n_nums.append(n%10)
        m_nums.append(m%10)
        n, m = n/10, m/10
        if n > 0 and m == 0:
            return False
    n_nums.sort()
    m_nums.sort()
    if n_nums == m_nums:
        return True
    return False

def run(limit):
    t0 = time.time()
    phis = make_phis(limit)
    print 'phis made'
    min_ratio = 10
    answer = 0
    for i, num_phi in enumerate(phis):
        num = i+2 #Since the index starts at 0 and phis started at 2
        ratio = float(num)/num_phi
        if num_phi == num-1: #Then it's prime and can't be perm
            pass
        elif ratio > min_ratio: #Then it doesn't matter if it's a perm
            pass
        elif check_perm(num, num_phi):
            min_ratio = ratio
            answer = num
            answer_phi = num_phi
    print time.time()-t0
    print answer, answer_phi

if __name__ == '__main__':
    run(10000000)
