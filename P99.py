import math
import time

t0 = time.time()

with open('base_exp.txt','r') as fileOpen:
    base_exp = []
    for line in fileOpen:
        nums = line.rstrip().split(',')
        nums[0], nums[1] = int(nums[0]), int(nums[1])
        base_exp.append(nums)

largest_log = 0
largest_pos = 0
for i, base_exp_pair in enumerate(base_exp):
    base_exp_log = base_exp_pair[1]*math.log(base_exp_pair[0])
    if base_exp_log > largest_log:
        largest_log = base_exp_log
        largest_pos = i

print ''
print time.time() - t0
print largest_pos
print largest_log

