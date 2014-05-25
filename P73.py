import time

def find(d):
    t0 = time.time()
    fractions = dict()
    for denom in xrange(2,d+1):
        lbound = (denom/3)+1
        ubound = int(round(denom/2.0))
        for num in xrange(lbound, ubound):
            check_num = float(num)/denom
            fractions[check_num] = 1
    print time.time()-t0
    print len(fractions.keys())
                
            
            


if __name__ == '__main__':
    find(12000)
        
