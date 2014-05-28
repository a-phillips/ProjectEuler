import time

def get(n):
    t0 = time.time()
    base = 2
    if n == 1:
        print base
        return None
    seq = [base]
    counter = 0
    k = 1
    for i in xrange(1, n):
        if counter == 1:
            seq.append(2*k)
            k += 1
        else:
            seq.append(1)
        if counter == 2:
            counter = 0
        else:
            counter += 1
    print seq
    print len(seq)
    num = 1
    den = seq[-1]
    for i in xrange(len(seq)-2, 0, -1):
        new = seq[i]
        #Convert to mixed fraction
        num += (den*new)
        #Invert
        num, den = den, num
    num += (base*den)
    print '%s/%s' % (num, den)
    total = 0
    while num > 0:
        total += num%10
        num /= 10
    print total
    print time.time()-t0

if __name__ == '__main__':
    get(100)
        
    
