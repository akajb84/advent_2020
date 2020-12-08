file = open('1_1input.txt', 'r')
lines = file.readlines()

nums = [int(line.strip()) for line in lines]

for n in nums:
    if (2020 - n) in nums:
        print (n * (2020-n))
        break