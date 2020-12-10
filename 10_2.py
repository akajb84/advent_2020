file = open('10_input.txt', 'r')
lines = file.readlines()

nums = [int(l.strip()) for l in lines]

nums.sort()
nums = [0] + nums + [nums[-1] + 3]

# print (nums)
ordering = []
for n in range (1, len(nums)):
    ordering.append(nums[n] - nums[n-1])

# print(ordering)

# count # of 1s in order
# must always keep first and last 1, and then the 3
# so anything of form: 3 3, 3 1 3, 1 1 3 can only have 1 option

# if length 4 (1 1 1 3) -- 2 possible options
# 0 1 2 5
# 0 2 5

# if length 5 (1 1 1 1 3) -- 4 possible options
# 0 1 2 3 6
# 0 1 3 6
# 0 2 3 6
# 0 3 6

# if length 6 (1 1 1 1 1 3) -- 7 possible options
# 0 1 2 3 4 7
# 0 1 2 4 7
# 0 1 3 4 7
# 0 1 4 7
# 0 2 3 4 7
# 0 2 4 7
# 0 3 4 7

# nothing is longer than that.

cur_count = 1 # start at 1, because we include initial value
total = 1
# these are number of combinations for different lengths of 1s
val = {0:1, 1: 1, 2:1, 3:1, 4: 2, 5: 4, 6: 7}
for a in ordering:
    if a == 3:
        cur_count = cur_count + 1
        total = total * val[cur_count]
        cur_count = 1
    else:
        cur_count = cur_count + 1

print (total)
