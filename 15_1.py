file = open('15_input.txt', 'r')
lines = file.readlines()

line = lines[0].strip()
numbers = line.split(",")
numbers = [int(n) for n in numbers]

seen = {}
turn = 1
last_seen = numbers.pop(0)
order = []
for n in numbers:
    seen[last_seen] = turn
    last_seen = n
    turn = turn + 1
    order.append(last_seen)

print (seen)
print(last_seen)
# for part 1 change to 2020 below
for i in range (turn, 30000000):
    if last_seen not in seen:
        seen[last_seen] = turn
        last_seen = 0
    else:
        old_turn = seen[last_seen]
        seen[last_seen] = turn
        last_seen = turn - old_turn

    order.append(last_seen)
    turn = turn + 1

# print(order)
print(last_seen)
