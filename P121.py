win_probs = []
count = 0
for blue1 in xrange(2):
    p1 = 1/2.0
    if not blue1: p1 = 1-p1
    for blue2 in xrange(2):
        p2 = 1/3.0
        if not blue2: p2 = 1-p2
        for blue3 in xrange(2):
            p3 = 1/4.0
            if not blue3: p3 = 1-p3
            for blue4 in xrange(2):
                p4 = 1/5.0
                if not blue4: p4 = 1-p4
                for blue5 in xrange(2):
                    p5 = 1/6.0
                    if not blue5: p5 = 1-p5
                    for blue6 in xrange(2):
                        p6 = 1/7.0
                        if not blue6: p6 = 1-p6
                        for blue7 in xrange(2):
                            p7 = 1/8.0
                            if not blue7: p7 = 1-p7
                            for blue8 in xrange(2):
                                p8 = 1/9.0
                                if not blue8: p8 = 1-p8
                                for blue9 in xrange(2):
                                    p9 = 1/10.0
                                    if not blue9: p9 = 1-p9
                                    for blue10 in xrange(2):
                                        p10 = 1/11.0
                                        if not blue10: p10 = 1-p10
                                        for blue11 in xrange(2):
                                            p11 = 1/12.0
                                            if not blue11: p11 = 1-p11
                                            for blue12 in xrange(2):
                                                p12 = 1/13.0
                                                if not blue12: p12 = 1-p12
                                                for blue13 in xrange(2):
                                                    p13 = 1/14.0
                                                    if not blue13: p13 = 1-p13
                                                    for blue14 in xrange(2):
                                                        p14 = 1/15.0
                                                        if not blue14: p14 = 1-p14
                                                        for blue15 in xrange(2):
                                                            p15 = 1/16.0
                                                            if not blue15: p15 = 1-p15
                                                            blue_count = blue1+blue2+blue3+blue4+blue5+\
                                                                         blue6+blue7+blue8+blue9+blue10+\
                                                                         blue11+blue12+blue13+blue14+blue15
                                                            if blue_count >= 8:
                                                                count += 1
                                                                prob = p1*p2*p3*p4*p5*\
                                                                       p6*p7*p8*p9*p10*\
                                                                       p11*p12*p13*p14*p15
                                                                win_probs.append(prob)
print count
total_prob = sum(win_probs)
fund_prize = 1/total_prob
print fund_prize




