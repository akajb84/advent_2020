file = open('1_1input.txt', 'r')
lines = file.readlines()

nums = [int(line.strip()) for line in lines]

for n in nums:
    for n2 in nums:
        if (n + n2 < 2020) and (2020 - n - n2) in nums:
            print (n * n2 * (2020 - n - n2))
            exit()
