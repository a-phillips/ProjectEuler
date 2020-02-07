import time
import itertools

#Test - 3-gon
t0 = time.time()
perms = itertools.permutations(range(1, 7))
largest = 0
for perm in perms:
    leg1 = [perm[0], perm[1], perm[2]]
    leg2 = [perm[3], perm[2], perm[4]]
    leg3 = [perm[5], perm[4], perm[1]]  
    if sum(leg1) == sum(leg2) == sum(leg3):
        gon = [leg1, leg2, leg3]
        nodes = [line[0] for line in gon]
        sort_index = nodes.index(min(nodes))
        sorted_gon = gon[sort_index:] + gon[:sort_index]
        str_num = ''.join([str(num) for line in sorted_gon for num in line])
        num = int(str_num)
        if num > largest:
            largest = num
print time.time()-t0
print largest


#Actual - 5-gon
t0 = time.time()
perms = itertools.permutations(range(1, 11))
largest = 0
for perm in perms:
    leg1 = [perm[0], perm[1], perm[2]]
    leg2 = [perm[3], perm[2], perm[4]]
    leg3 = [perm[5], perm[4], perm[6]]
    leg4 = [perm[7], perm[6], perm[8]]
    leg5 = [perm[9], perm[8], perm[1]]
    if sum(leg1) == sum(leg2) == sum(leg3) == sum(leg4) == sum(leg5):
        gon = [leg1, leg2, leg3, leg4, leg5]
        nodes = [line[0] for line in gon]
        sort_index = nodes.index(min(nodes))
        sorted_gon = gon[sort_index:] + gon[:sort_index]
        str_num = ''.join([str(num) for line in sorted_gon for num in line])
        if len(str_num) == 16:
            num = int(str_num)
            if num > largest:
                largest = num
print time.time()-t0
print largest
        
