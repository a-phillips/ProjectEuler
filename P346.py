import time

def get_reps(b, limit):
    reps = []
    n = 2
    num = (b**n) + b + 1
    while num < limit:
        reps.append(num)
        n += 1
        num += (b**n)
    return reps

def run(limit):
    t0 = time.time()
    vals = {}
    b = 2
    while (b**2) + b + 1 < limit:
        reps = get_reps(b, limit)
        for rep in reps:
            vals[rep] = 1
        b += 1
    print time.time()-t0
    print sum(vals.keys())+1
            

if __name__ == '__main__':
    run(10**12)
    
