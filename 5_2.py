file = open('5_input.txt', 'r')
lines = file.readlines()

#BBFFBFB LLR

highest = 0
seat_ids = []
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

    seat_ids.append(result)

seat_ids.sort()
print (seat_ids)

last = 0
cur = 0
next_id = 0
for i in seat_ids:
    last = cur
    cur = i
    # next_id = i
    if (cur - last) == 2:
        print (cur)
        print (last)

