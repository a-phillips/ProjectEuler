"""
This solution takes WAY longer than 1 minute. Should consider optimizing
"""

def consec_same_divs(n):
    prev = 2
    prev_divs = 2
    curr = 3
    curr_divs = 2
    count = 0
    while curr <= n:
        if curr_divs == prev_divs:
            count += 1
        prev, prev_divs = curr, curr_divs
        curr += 1
        curr_divs = 0
        for i in xrange(int(curr**.5)):
            if curr % (i+1) == 0:
                if (i+1)**2 == curr:
                    curr_divs += 1
                else:
                    curr_divs += 2
    return count


if __name__ == '__main__':
    print consec_same_divs(10000000)

