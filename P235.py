import time

def s(r):
    total = 0
    for k in xrange(1, 5001):
        total += (900-(3*k))*(r**(k-1))
    return total

def run():
    goal = -600000000000
    r = 1
    move = .1
    while move >= (10**-15):
        best_guess = s(r)
        if best_guess < goal:
            r -= move
            move /= 10.0
        r += move
    return r
        
    

if __name__ == '__main__':
    r = run()
    print r
    print int(r*(10000000000000000))

