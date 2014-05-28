import time

def run(limit):
    t0 = time.time()
    grid = {(0, 0): 0} #0 indicates white
    x = 0
    y = 0
    move = {'u':(0, 1),
            'r':(1, 0),
            'd':(0, -1),
            'l':(-1, 0)}
    direct = ['r', 'd', 'l', 'u']
    dir_index = 0
    for step in xrange(limit):
        color = grid.get((x, y), 0)
        if color == 1: #square is black, move counterclockwise
            grid[(x, y)] = 0
            dir_index = (dir_index-1)%4
        else: #square is white, move clockwise
            grid[(x, y)] = 1
            dir_index = (dir_index+1)%4
        curr_move = move[direct[dir_index]]
        x += curr_move[0]
        y += curr_move[1]
    print time.time()-t0
    print grid.values().count(1)


if __name__ == '__main__':
    run(10**8)
        
            
