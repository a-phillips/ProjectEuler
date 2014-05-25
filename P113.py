import time
str_digits = ['0','1','2','3','4','5','6','7','8','9']

def make_hundreds():
    non_bouncy = []
    for num in xrange(100,1000):
        #Check all identical
        if num%111 == 0:
            non_bouncy.append('n'+str(num))
        #Check decreasing
        elif num%10 <= (num/10)%10 <= (num/100):
            non_bouncy.append('d'+str(num))
        #Check increasing
        elif num%10 >= (num/10)%10 >= (num/100):
            non_bouncy.append('i'+str(num))
    #print '\n'.join([num for num in non_bouncy])
    return non_bouncy

def make_next(base_list):
    next_list = []
    for str_num in base_list:
        #Modify decreasing number
        if str_num[0] == 'd':
            #Add digits to beginning, anything >= current first digit
            for i in xrange(int(str_num[1]), 10):
                next_list.append('d'+str_digits[i]+str_num[1:])
            #Add digits to end, anything <= current first digit
            for i in xrange(0, int(str_num[-1])+1):
                next_list.append(str_num + str_digits[i])

        #Modify increasing number
        elif str_num[0] == 'i':
            #Add digits to beginning, excluding 0s
            for i in xrange(1, int(str_num[1])+1):
                next_list.append('i'+str_digits[i]+str_num[1:])
            #Add digits to end
            for i in xrange(int(str_num[-1]), 10):
                next_list.append(str_num + str_digits[i])

        #Modify number of all identical digits
        elif str_num[0] == 'n':
            #Add another identical digit
            next_list.append(str_num + str_num[1])
            #Add new first digit which makes it increasing, exclude 0s
            for i in xrange(1, int(str_num[1])):
                next_list.append('i'+str_digits[i]+str_num[1:])
            #Add new first digit which makes it decreasing
            for i in xrange(int(str_num[1])+1, 10):
                next_list.append('d'+str_digits[i]+str_num[1:])
            #Add new last digit which makes it increasing
            for i in xrange(int(str_num[-1])+1, 10):
                next_list.append('i'+str_num[1:]+str_digits[i])
            #Add new last digit which makes it decreasing
            for i in xrange(1, int(str_num[-1])):
                next_list.append('d'+str_num[1:]+str_digits[i])

    next_list.sort()
    seen = set()
    return [num for num in next_list if num not in seen and not seen.add(num)]


def run(n):
    t0 = time.time()
    n -= 3
    base_list = make_hundreds()
    count = 99 + len(base_list) #All numbers below 100 are not bouncy
    for i in xrange(n):
        print i
        next_list = make_next(base_list)
        count += len(next_list)
        base_list = next_list
    print time.time()-t0
    print count

if __name__ == '__main__':
    run(100)
