import time

def run(move_string, limit):
    t0 = time.time()
    a_end = 1
    while True:
        a_start = a_end
        for i in xrange(len(move_string)-1, -1, -1):
            move = move_string[i]
            if move == 'd':
                a_start = ((3*a_start)+1)/2.0
                if a_start % 3 != 2:
                    break
            elif move == 'U':
                a_start = ((3*a_start)-2)/4.0
                if a_start % 3 != 1:
                    break
            else:
                a_start *= 3
        else:
            if a_start > limit:
                print time.time()-t0
                print int(a_start), a_end
                print get_string(a_start)
                return None
        a_end += 1
        
def get_string(a):
    string = ''
    while a > 1 and len(string) < 30:
        rem = a%3
        if rem == 2:
            a = ((2*a)-1)/3
            string += 'd'
        elif rem == 1:
            a = ((4*a) + 2)/3
            string += 'U'
        else:
            a /= 3
            string += 'D'
    return string
            
            


if __name__ == '__main__':
    run('UDDDUdddDDUDDddDdDddDDUDDdUUDd', 10**15)
    #run('DdDddUUdDD', 10**6)

    
                
            
            
