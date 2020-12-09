file = open('9_input.txt', 'r')
lines = file.readlines()

lines = [int(l.strip()) for l in lines]
pointer = 25
valid = True

while valid:
    valid = False
    for i in range(pointer-25, pointer):
        for j in range(pointer-24, pointer):
            if i != j:
                if lines[i] + lines[j] == lines[pointer]:
                    valid = True

    pointer = pointer + 1

check_val = lines[pointer-1]

start = 0
total = 0
smallest = 0
largest = 0
while start < len(lines):

    end = start
    smallest = lines[start]
    largest = lines[start]
    while total < check_val:
        total = total + lines[end]
        if lines[end] < smallest:
            smallest = lines[end]
        if lines[end] > largest:
            largest = lines[end]
        end = end + 1

    if total == check_val:

        print(smallest + largest)
        break

    start = start + 1

    total = 0