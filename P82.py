import time
import copy

test_matrix = [[131, 673, 234, 103, 18],
               [201, 96, 342, 965, 150],
               [630, 803, 746, 422, 111],
               [537, 699, 497, 121, 956],
               [805, 732, 524, 37, 331]]

best_paths = []
for i in xrange(80):
    best_paths.append([-1]*80)


#Rows are i, columns are j

def f(i, j, prev=None):
    if i > 79 or i < 0:
        return 1000000000
    if best_paths[i][j] != -1:
        return best_paths[i][j]
    if j == 79:
        best_paths[i][j] = matrix[i][j]
        return matrix[i][j]
    #Can't move down if previous move was up or past end of matrix
    if prev == 'u' or i == 79:
        return min(f(i-1, j, 'u'), f(i, j+1)) + matrix[i][j]
    #Can't move up if previous move was down or past end of matrix
    if prev == 'd' or i == 0:
        return min(f(i+1, j, 'd'), f(i, j+1)) + matrix[i][j]
    return min(f(i+1, j, 'd'), f(i-1, j, 'u'), f(i, j+1)) + matrix[i][j]

results = []

if __name__ == '__main__':
    file_location = '/Users/aphillips/Desktop/Programming/Python/Project Euler/matrix.txt'

    with open(file_location, 'r') as raw_file:
        read_file = raw_file.read().splitlines()
        matrix = []
        for line in read_file:
            matrix.append(line.split(','))
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[i])):
                matrix[i][j] = int(matrix[i][j])


    t0 = time.time()
    for j in xrange(79, -1, -1):
        for i in xrange(79, -1, -1):
            best_paths[i][j] = f(i, j)


    results = []
    for i in xrange(80):
        results.append(best_paths[i][0])
    print time.time()-t0
    print min(results)





"""
    t0 = time.time()
    for i in xrange(5):
        results.append(f(i, 0))
    print time.time()-t0
    print results
"""