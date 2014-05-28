"""For a positive integer n, define f(n) as the least positive multiple of
n that, written in base 10, uses only digits  2.

Thus f(2)=2, f(3)=12, f(7)=21, f(42)=210, f(89)=1121222.

Sum from 1 to 100 of f(n)/n = 11363107

Find sum to 10000
"""

import time

def run(limit):
    t0 = time.time()
    base_checks = [0, 1, 2]
    factors = [10, 20]
    nums_left = range(3, limit+1)
    total = 2
    while len(nums_left) > 0:
        print len(nums_left), len(base_checks)
        new_checks = []
        for factor in factors:
            for base in base_checks:
                check = factor + base
                new_checks.append(check)
                i = 0
                while i < len(nums_left):
                    num = nums_left[i]
                    if num > check:
                        break
                    elif check % num == 0:
                        total += check/num
                        #print check, num
                        nums_left.remove(num)
                    else:
                        i += 1
        print 'Add to base checks'
        base_checks += new_checks
        factors[0] *= 10
        factors[1] *= 10
        #print 'next factor'
        #raw_input()
    print time.time() - t0
    print total


if __name__ == '__main__':
    run(10000)
                    
    
            
