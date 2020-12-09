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
print(lines[pointer - 1])
