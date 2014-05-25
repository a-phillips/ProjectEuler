def check(n):
    total = 0
    temp = n
    while temp > 0:
        total += temp%10
        temp /= 10
    product = 1
    if total == 1:
        return False
    while product <= n:
        if product * total == n:
            return True
        product *= total
    return False

def run(limit):
    num = 10
    results = []
    while len(results) < limit:
        if check(num):
            print num
            results.append(num)
        num += 1

if __name__ == '__main__':
    run(30)


