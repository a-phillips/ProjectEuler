def max_mod(a):
    n=1
    mod = -1
    max_n = 0
    while True:
        check_mod = (((a+1)**n)+((a-1)**n))%(a**2)
        if check_mod == mod:
            return mod
        if check_mod > mod:
            mod = check_mod
            max_n = n
        n += 1

if __name__ == '__main__':
    results = []
    limit = 1000
    for i in xrange(3,limit+1):
        results.append(max_mod(i))
        if i%100 == 0:
            print i
    print results[:10]
    print 'Sum of first %s: %s' % (limit, sum(results))
