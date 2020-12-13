file = open('13_input.txt', 'r')
lines = file.readlines()

buses = lines[1].strip().split(",")

bus = 0
count = 0
bus_times = {}
time_set = []
biggest = 0
offset = 0
for b in buses:
    if b == "x":
        # out of service, skip
        pass
    else:
        b = int(b)
        bus_times[b] = count
        if count > 0:
            time_set.append(count)
        else:
            bus = b

        if b > biggest:
            biggest = b
            offset = count
    count = count + 1


print (bus_times)
print (bus)

bus_times.pop(bus)
keys = sorted(bus_times, reverse=True)
print (keys)
offset = bus
inc = bus
for key in keys:
    while (offset + bus_times[key]) % key != 0:
        # this finds first time values line up for initial bus at t=0
        # and key (current bus)
        offset = offset + inc

    # print(key)
    # print(offset)
    # after this point, they will cross every bus times of the current increment
    inc = inc * key
    bus = key
    # print (inc)
    # print("-----")

print(offset)

# 18313046126121062 TOO HIGH
# 825305207525452 <-- right answer. Mind to dead to explain why
# 18178703590270 TOO LOW
# 100000000000000
