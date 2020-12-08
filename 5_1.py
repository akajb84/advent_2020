file = open('5_input.txt', 'r')
lines = file.readlines()

#BBFFBFB LLR

highest = 0

for line in lines:

    # 0 - 127
    # = 1 - 128
    i = 0
    seat = 0
    upper = 0
    lower = 127
    change = 64
    while (i < 6):
        if line[i] == "F":
            lower = lower - change
        else:
            upper = upper + change

        change = int(change / 2)
        i = i + 1

    if line[i] == "F":
        seat = upper
    else:
        seat = lower

    seat = seat
    i = 7

    upper = 0
    lower = 7
    change = 4
    while (i < 9):
        if line[i] == "L":
            lower = lower - change
        else:
            upper = upper + change

        change = int(change / 2)
        i = i + 1

    if line[i] == "L":
        spot = upper
    else:
        spot = lower


    result = (seat * 8) + spot
    print (line.strip() + " " + str(seat) + " " + str(spot) + " " + str(result))

    if result > highest:
        highest = result

print (highest)
