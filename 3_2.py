"""
Right 1, down 1.
Right 3, down 1. (This is the slope you already checked.)
Right 5, down 1.
Right 7, down 1.
Right 1, down 2.
"""

file = open('3_1_input.txt', 'r')
lines = file.readlines()

lines = [line.strip() for line in lines]

length = len(lines[0].strip())
print(length)

over = [1, 3, 5, 7, 1]
down = [1, 1, 1, 1, 2]
trees = [0, 0, 0, 0, 0]

c = 0
while c < len(over):
    x = 0 + over[c]
    y = 0 + down[c]
    while y < len(lines):
        if (x >= length):
            x = x - length
        if lines[y][x] == "#":
            trees[c] = trees[c] + 1

        x = x + over[c]
        y = y + down[c]

    c = c + 1

print (trees)
total = 0
for a in trees:
    if total == 0:
        total = a
    else:
        total = total * a

print (total)
