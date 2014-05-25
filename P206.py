import time

t0 = time.time()
for i in xrange(1010101010, 1389026624):
    sq_str = str(i**2)
    if sq_str[0] == '1':
        if sq_str[2] == '2':
            if sq_str[4] == '3':
                if sq_str[6] == '4':
                    if sq_str[8] == '5':
                        if sq_str[10] == '6':
                            if sq_str[12] == '7':
                                if sq_str[14] == '8':
                                    if sq_str[16] == '9':
                                        if sq_str[18] == '0':
                                            print time.time() - t0
                                            print i
                                            print sq_str

