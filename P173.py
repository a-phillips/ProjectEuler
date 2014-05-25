lamina_count = 0
ext_square = 8
while ext_square <= 1000000:
    lamina_count += 1
    int_square = ext_square - 8
    lamina_size = int_square + ext_square
    while int_square > 4 and lamina_size <= 1000000:
        lamina_count += 1
        int_square -= 8
        lamina_size += int_square
    ext_square += 4

print 'Total is %s' % lamina_count

