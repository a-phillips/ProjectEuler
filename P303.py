"""For a positive integer n, define f(n) as the least positive multiple of
n that, written in base 10, uses only digits  2.

Thus f(2)=2, f(3)=12, f(7)=21, f(42)=210, f(89)=1121222.

Sum from 1 to 100 of f(n)/n = 11363107

Find sum to 10000
"""

"""
This algorithm attempts to find the solution in reverse - create each possible
combination of (0, 1, 2) for 2 digits, eliminate all solutions, then expand to
3 digits, eliminate all remaining, etc. I get to 1 number remaining well within
the 1-minute threshold, but 9999 keeps f*cking with me.
"""

import time
import itertools

def run(limit):
    t0 = time.time()
    
    #These are numbers that will be added to factors list
    #representing the n-1 digits of the n-digit numbers being checked
    base_checks = [0, 1, 2]
    
    #These are what we use to scale up our checks
    #All numbers will begin with 1 or 2 - these get multiplied by 10
    #with each iteration
    factors = [10, 20]
    
    #nums_left represents numbers we haven't found yet.
    nums_left = range(3, limit+1)
    total = 2
    
    while len(nums_left) > 0:
    	#status update
        print len(nums_left), len(base_checks)
        #print the horrible number that is keeping me over 1 minute!
        if len(nums_left) == 1:
        	for num in nums_left:
        		print num
        		
        #will contain each new combo of (factor + base)
        new_checks = []
        
        #loop through each factor/base combo
        for factor in factors:
            for base in base_checks:
                check = factor + base
                new_checks.append(check)
                i = 0
                
                #check all remaining numbers against current 1&2 number
                while i < len(nums_left):
                    num = nums_left[i]
                    
                    #break if impossible
                    if num > check:
                        break
                        
                    elif check % num == 0:
                    	#found one! add f(n)/n to the total, remove from remaining
                        if num == 999:
                        	print "999: ", num
                        total += check/num
                        nums_left.remove(num)
                        
                    else:
                        i += 1
        #status update: completed looping through all factor/base combos
        #we now add all of the new "base" numbers to base_checks and 
        #increase our factors by 1 digit.
        #FTR: len(base_checks) increases by a power of 3 with each iteration
        #it gets ugly fast.
        print 'Add to base checks'
        base_checks += new_checks
        factors[0] *= 10
        factors[1] *= 10
    
    #someday this will stop running...
    print time.time() - t0
    print total


if __name__ == '__main__':
    run(10000)
                    
    
            
