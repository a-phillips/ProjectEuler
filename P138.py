def check(b):
    h1 = b-1
    h2 = b+1
    b = b/2
    L1 = ((h1**2)+(b**2))**.5
    if L1 == int(L1):
        return L1
    L2 = ((h2**2)+(b**2))**.5
    if L2 == int(L2):
        return L2
    return 0

def run():
    b = 2
    Ls = []
    while len(Ls) < 12:
        result = check(b)
        if result:
            Ls.append(result)
            print result
        b += 2
    print Ls
    print sum(Ls)

if __name__ == '__main__':
    run()
