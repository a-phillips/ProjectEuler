import copy
import time

def BF(matrix, min_sums, start):
    y = start[0]
    x = start[1]
    """
    print y, x
    for i in xrange(5):
        print matrix[i]
    for i in xrange(5):
        print min_sums[i]
    """
    if y == len(matrix) and x == len(matrix[0]):
        #print 'in 4s'
        return matrix, min_sums
    if x-1 >= 0:
        if min_sums[y][x] + matrix[y][x-1] < min_sums[y][x-1]:
            min_sums[y][x-1] = min_sums[y][x] + matrix[y][x-1]
            #print 'going to bf x-1' , y, x-1
            matrix, min_sums = BF(matrix, min_sums, (y, x-1))
    if y-1 >= 0:
        if min_sums[y][x] + matrix[y-1][x] < min_sums[y-1][x]:
            min_sums[y-1][x] = min_sums[y][x] + matrix[y-1][x]
            #print 'going to bf y-1' , y-1, x
            matrix, min_sums = BF(matrix, min_sums, (y-1, x))
    try:
        if min_sums[y][x] + matrix[y][x+1] < min_sums[y][x+1]:
            min_sums[y][x+1] = min_sums[y][x] + matrix[y][x+1]
            #print 'going to bf x+1' , y, x+1
            matrix, min_sums = BF(matrix, min_sums, (y, x+1))
    except:
        pass
    try:
        if min_sums[y][x] + matrix[y+1][x] < min_sums[y+1][x]:
            min_sums[y+1][x] = min_sums[y][x] + matrix[y+1][x]
            #print 'going to bf y+1' , y+1, x
            matrix, min_sums = BF(matrix, min_sums, (y+1, x))
    except:
        pass
    return matrix, min_sums


def test():
    t0 = time.time()
    test_matrix = [[131, 673, 234, 103, 18],
                   [201, 96, 342, 965, 150],
                   [630, 803, 746, 422, 111],
                   [537, 699, 497, 121, 956],
                   [805, 732, 524, 37, 331]]
    end = (5, 5)
    min_sums = []
    min_row = [10**10]*5
    for i in xrange(5):
        min_sums.append(copy.deepcopy(min_row))
    min_sums[0][0] = test_matrix[0][0]
    BF(test_matrix, min_sums, (0, 0))
    print time.time()-t0
    print min_sums[4][4]


def real():
    t0 = time.time()
    filename = 'C:\Documents and Settings\zq5586\Desktop\Personal\Coding\matrix.txt'
    with open(filename, 'r') as raw_file:
        test = raw_file.read().splitlines()
        matrix = []
        for line in test:
            matrix.append([int(item) for item in line.split(',')])
    end = (len(matrix), len(matrix[0]))
    min_sums = []
    min_row = [10**10]*len(matrix[0])
    for i in xrange(len(matrix)):
        min_sums.append(copy.deepcopy(min_row))
    min_sums[0][0] = matrix[0][0]
    BF(matrix, min_sums, (0, 0))
    print time.time()-t0
    print min_sums[79][79]
    

if __name__ == '__main__':
    test()
    real()
        
        
	
