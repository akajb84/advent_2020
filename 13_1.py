file = open('13_input.txt', 'r')
lines = file.readlines()

earliest = int(lines[0].strip())

buses = lines[1].strip().split(",")

bus = 0
time = 0

for b in buses:
    if b == "x":
        # out of service, skip
        pass
    else:
        val = int(b)
        time_offset = int(earliest % val)
        if time_offset == 0:
            # bus is going to arrive on time
            bus = val
            time = earliest
        else:
            next_time = earliest + (val - time_offset)
            if time == 0 or next_time < time:
                time = next_time
                bus = val

print (bus)
print(time)

print (bus * (time - earliest))