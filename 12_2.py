file = open('12_input.txt', 'r')
lines = file.readlines()

lines = [l.strip() for l in lines]

facing = "E" # east
face_int = 1 # n 0, e 1, s, 2, w 3
north = 0
east = 0

ship_move = {"N": 0, "S": 0, "E": 0, "W":0}
waypoint_move = {"N": 1, "S": 0, "E": 10, "W":0}

for line in lines:

    direction = line[0]
    count = int(line[1:])

    if direction == "F":
        ship_move["N"] = ship_move["N"] + int(count * waypoint_move["N"])
        ship_move["E"] = ship_move["E"] + int(count * waypoint_move["E"])
        ship_move["S"] = ship_move["S"] + int(count * waypoint_move["S"])
        ship_move["W"] = ship_move["W"] + int(count * waypoint_move["W"])

    if direction == "R" or direction == "L":
        # turn right
        num = int(count / 90)

        if direction == "L":
            num = 4 - num

        if num == 1:
            n = waypoint_move["N"]
            s = waypoint_move["S"]
            e = waypoint_move["E"]
            w = waypoint_move["W"]
            waypoint_move["N"] = w
            waypoint_move["E"] = n
            waypoint_move["S"] = e
            waypoint_move["W"] = s

        elif num == 2:
            n = waypoint_move["N"]
            s = waypoint_move["S"]
            e = waypoint_move["E"]
            w = waypoint_move["W"]
            waypoint_move["N"] = s
            waypoint_move["E"] = w
            waypoint_move["S"] = n
            waypoint_move["W"] = e
        elif num == 3:
            n = waypoint_move["N"]
            s = waypoint_move["S"]
            e = waypoint_move["E"]
            w = waypoint_move["W"]
            waypoint_move["N"] = e
            waypoint_move["E"] = s
            waypoint_move["S"] = w
            waypoint_move["W"] = n


    if direction == "N":
        waypoint_move["N"] = waypoint_move["N"] + count
    if direction == "S":
        waypoint_move["S"] = waypoint_move["S"] + count
    if direction == "E":
        waypoint_move["E"] = waypoint_move["E"] + count
    if direction == "W":
        waypoint_move["W"] = waypoint_move["W"] + count


print (ship_move)
print(waypoint_move)

north_south = abs(ship_move["N"] - ship_move["S"])
east_west = abs(ship_move["E"] - ship_move["W"])
print(north_south + east_west)