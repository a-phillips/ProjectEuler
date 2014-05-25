lamina_count = {}
ext_square = 8
while ext_square <= 1000000:
    lamina_count[ext_square] = lamina_count.get(ext_square,0) + 1
    int_square = ext_square - 8
    lamina_size = int_square + ext_square
    while int_square > 4 and lamina_size <= 1000000:
        lamina_count[lamina_size] = lamina_count.get(lamina_size,0) + 1
        int_square -= 8
        lamina_size += int_square
    ext_square += 4

N = {}
for value in lamina_count.values():
    N[value] = N.get(value, 0) + 1

total = 0
for i in xrange(10):
    total += N.get(i+1,0)

print 'Total is %s' % total

