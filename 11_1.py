def count_occupied(row, col, cur_seats):
    count = 0
    for i in range(max(0, row-1), min(row+2, NUM_ROW)):
        for j in range(max(0, col-1), min(col+2, NUM_COL)):
            if i == row and j == col:
                # skip
                pass
            elif cur_seats[i][j] == 1:
                count = count + 1

    return count


file = open('11_input.txt', 'r')
lines = file.readlines()

lines = [l.strip() for l in lines]

NUM_ROW = len(lines)
NUM_COL = len(lines[0])

seats = [[0 for i in range(0, NUM_COL)] for j in range(0, NUM_ROW)]


i = 0
while i < len(lines):
    line = lines[i]

    for l in range(0,NUM_COL):
        if line[l] == "#":
            seats[i][l] = 1 # occupied
        elif line[l] == ".":
            seats[i][l] = -1 # floor

    i = i + 1

print (seats)

made_changes = True

while made_changes:
    print ("path")
    made_changes = False
    new_seats = [[0 for i in range(0, NUM_COL)] for j in range(0, NUM_ROW)]
    for i in range (0, NUM_ROW):
        for j in range(0, NUM_COL):
            if seats[i][j] == -1:
                # floor, can never be filled
                new_seats[i][j] = -1
            else:
                count = count_occupied(i, j, seats)
                if count == 0 and seats[i][j] != 1:
                    # become filled
                    new_seats[i][j] = 1
                    made_changes = True
                elif count >= 4 and seats[i][j] == 1:
                    # become empty
                    new_seats[i][j] = 0
                    made_changes = True
                else:
                    # stay the same
                    new_seats[i][j] = seats[i][j]

    seats = new_seats

print (seats)
num_seats = 0
for i in range (0, NUM_ROW):
    for j in range(0, NUM_COL):
        if seats[i][j] == 1:
            num_seats = num_seats + 1

print (num_seats)
