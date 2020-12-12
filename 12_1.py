file = open('12_input.txt', 'r')
lines = file.readlines()

lines = [l.strip() for l in lines]

facing = "E" # east
face_int = 1 # n 0, e 1, s, 2, w 3
north = 0
east = 0

move = {"N": 0, "S": 0, "E": 0, "W":0}

for line in lines:

    direction = line[0]
    count = int(line[1:])

    if direction == "F":
        move[facing] = move[facing] + count
    if direction == "R" or direction == "L":
        # turn
        num = int(count / 90)

        if direction == "L":
            face_int = face_int - num
        else:
            face_int = face_int + num

        face_int = abs(int(face_int % 4))
        if face_int == 0:
            facing = "N"
        elif face_int == 1:
            facing = "E"
        elif face_int == 2:
            facing = "S"
        else:
            facing = "W"

    if direction == "N":
        move["N"] = move["N"] + count
    if direction == "S":
        move["S"] = move["S"] + count
    if direction == "E":
        move["E"] = move["E"] + count
    if direction == "W":
        move["W"] = move["W"] + count


print (move)
print (facing)

north_south = abs(move["N"] - move["S"])
east_west = abs(move["E"] - move["W"])
print(north_south + east_west)