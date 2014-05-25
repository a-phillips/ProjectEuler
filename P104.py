import time

nums = ['1','2','3','4','5','6','7','8','9']

def check(f):
    first_9 = f[:9]
    last_9 = f[-9:]
    for num in nums:
        if num not in last_9 or num not in first_9:
            return False
    else:
        return True




def run():
    t0 = time.time()
    index = 3
    n2 = 1
    n1 = 1
    while True:
        f = n1 + n2
        check_f = str(f)
        if len(check_f) >= 9:
            if check(check_f):
                print time.time()-t0
                print f
                print index
                break
        index += 1
        n2, n1 = f, n2

if __name__ == '__main__':
    run()

