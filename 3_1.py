file = open('3_1_input.txt', 'r')
lines = file.readlines()

first = lines.pop(0) # skip first row

over = 3
length = len(first.strip())
print(length)
valid = 0
trees = 0
spot = over
for line in lines:
    line = line.strip()
    print(line)
    if spot >= length:
        print ("adjusting " + str(spot))
        bla = line + line
        print(bla)
        print(bla[spot])
        spot = spot - length
        # print(spot)

    print (line[spot])
    print(spot)
    if (line[spot]) == "#":
        trees = trees + 1

    spot = spot + over

print (trees)

"""
31 spots, 30 indexes (0 - 30)

spot == 31
spot = 0
31 -> 0
32 -> 1
33 -> 2
"""