import time
import math

def check_total(n):
    c = -.5*((n**2)-n)
    b = 1
    a = 1
    num_blues = (b+math.sqrt((b**2)-(4*a*c)))/(2*a)
    if num_blues == int(num_blues):
        return num_blues
    return False


def run(n):
    t0 = time.time()
    while True:
        result = check_total(n)
        if result:
            print time.time()-t0
            print int(result)
            break
        n += 1

if __name__ == '__main__':
    run (22)
    run(10**11)
    run(10**13)
