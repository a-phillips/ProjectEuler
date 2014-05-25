import time

def check_num(n):
    str_num = str(n)
    if str_num == str_num[::-1]:
        for start_square in xrange(int(n**.5)):
            square_sum = 0
            add_square = start_square+1
            count = 0
            while square_sum < n:
                square_sum += add_square**2
                count += 1
                if square_sum == n and count > 1:
                    return True
                add_square += 1
        return False
    return False

def run(n):
    t0 = time.time()
    count = 0
    total_sum = 0
    for i in xrange(n):
        if i > 0:
            if check_num(i) == True:
                total_sum += i
    print time.time()-t0
    print total_sum

if __name__ == '__main__':
    run(100)
    run(1000)
    run(10000)
    run(100000)
    run(1000000)
    run(10000000)
    run(100000000)


