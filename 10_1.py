file = open('10_input.txt', 'r')
lines = file.readlines()

nums = [int(l.strip()) for l in lines]

nums.sort()
nums = [0] + nums

count_3 = 1 # device is 3 over last one
count_1 = 0
for n in range (1, len(nums)):
    if (nums[n] - nums[n-1]) == 1:
        count_1 = count_1 + 1
    elif (nums[n] - nums[n-1]) == 3:
        count_3 = count_3 + 1

print (count_3)
print (count_1)
print (count_3 * count_1)
