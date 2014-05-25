"""Not solved!"""

import math
import time

def make_terms(N):
    terminal_denoms = []
    for exp_2 in xrange(int(math.log(N)/math.log(2))+1):
        for exp_5 in xrange(int(math.log(N)/math.log(5))+1):
            num = (2**exp_2) * (5**exp_5)
            if num <= N:
                terminal_denoms.append(num)
    return terminal_denoms


def D(N, terminal_denoms):
    Pmax = 0
    for i in xrange(N-1):
        Pnew = (N/(i+1.0))**(i+1) 
        if Pnew > Pmax:
            Pmax = Pnew
            denom = i+1
            if denom in terminal_denoms:
                coeff = -1
            else:
                coeff = 1
    return N*coeff


def run(N):
    terminal_denoms = make_terms(N**2)
    print terminal_denoms
    total = 0
    for i in xrange(N+1):
        if i >= 5:
            print i
            result = D(i, terminal_denoms)
            total += result
    print total


if __name__ == '__main__':
    run(10000)
