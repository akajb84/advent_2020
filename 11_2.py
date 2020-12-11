def count_occupied(row, col, cur_seats):
    count = 0
    changes = [[-1,-1],[-1,0],[-1,1], [0,-1],[0,1], [1,-1], [1,0], [1,1]]

    for i in range (0, len(changes)):
        row_change = changes[i][0]
        col_change = changes[i][1]
        check_row = row + row_change
        check_col = col + col_change
        while (0 <= check_col < NUM_COL) and (0 <= check_row < NUM_ROW):
            if cur_seats[check_row][check_col] == 1:
                count = count + 1
                break
            elif cur_seats[check_row][check_col] == 0:
                break
            else:
                # floor, so need to look a row/col further
                check_col = check_col + col_change
                check_row = check_row + row_change

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
                elif count >= 5 and seats[i][j] == 1:
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
