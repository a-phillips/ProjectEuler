"""Not very elegant, and requires inspection of the results to actually
determine which one it is, but it gets the job done!"""

#Generate the numbers
tri = []
sq = []
pent = []
hexa = []
hept = []
octa = []
n = 1
while n*(n+1)/2 < 10000:
    tri.append(n*(n+1)/2)
    sq.append(n**2)
    pent.append(n*((3*n)-1)/2)
    hexa.append(n*((2*n)-1))
    hept.append(n*((5*n)-3)/2)
    octa.append(n*((3*n)-2))
    n += 1
#Filter on 4-digit numbers which don't end in 0
tri = filter(lambda x: x > 1000 and x < 10000 and x%100 > 9, tri)
sq = filter(lambda x: x > 1000 and x < 10000 and x%100 > 9, sq)
pent = filter(lambda x: x > 1000 and x < 10000 and x%100 > 9, pent)
hexa = filter(lambda x: x > 1000 and x < 10000 and x%100 > 9, hexa)
hept = filter(lambda x: x > 1000 and x < 10000 and x%100 > 9, hept)
octa = filter(lambda x: x > 1000 and x < 10000 and x%100 > 9, octa)

#88 = len(tri)
#53 =  len(sq)
#47 = len(pent)
#44 = len(hexa)
#40 = len(hept)
#30 = len(octa)

uniques = []
temp = [num for num in tri if num not in uniques]
uniques += temp
temp = [num for num in sq if num not in uniques]
uniques += temp
temp = [num for num in pent if num not in uniques]
uniques += temp
temp = [num for num in hexa if num not in uniques]
uniques += temp
temp = [num for num in hept if num not in uniques]
uniques += temp
temp = [num for num in octa if num not in uniques]
uniques += temp

uniques.sort()

num_types = dict(zip(uniques,['']*len(uniques)))

for num in num_types.keys():
    if num in tri: num_types[num] += '3'
    if num in sq: num_types[num] += '4'
    if num in pent: num_types[num] += '5'
    if num in hexa: num_types[num] += '6'
    if num in hept: num_types[num] += '7'
    if num in octa: num_types[num] += '8'


def check_solution(cycle):
    type_string = ''
    for num in cycle:
        type_string += num_types[num]
    if set('345678') == set(type_string):
        return type_string
    return False

def run():
    for num1 in uniques:
        suff1 = num1 % 100
        second_nums = filter(lambda x: x/100 == suff1, uniques)
        for num2 in second_nums:
            suff2 = num2 % 100
            third_nums = filter(lambda x: x/100 == suff2, uniques)
            for num3 in third_nums:
                suff3 = num3 % 100
                fourth_nums = filter(lambda x: x/100 == suff3, uniques)
                for num4 in fourth_nums:
                    suff4 = num4 % 100
                    fifth_nums = filter(lambda x: x/100 == suff4, uniques)
                    for num5 in fifth_nums:
                        suff5 = num5 % 100
                        sixth_nums = filter(lambda x: x/100 == suff5, uniques)
                        for num6 in sixth_nums:
                            if num6 % 100 == num1 / 100:
                                cycle = [num1, num2, num3, num4, num5, num6]
                                result = check_solution(cycle)
                                if result:
                                    print cycle, result, sum(cycle)

if __name__ == '__main__':
    run()




