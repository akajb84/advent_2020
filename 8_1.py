file = open('8_input.txt', 'r')
lines = file.readlines()

pointer = 0
seen = []
count = 0
while pointer not in seen:
    seen.append(pointer)
    action = lines[pointer]
    print (action)
    action = action.strip()
    acc, change = action.split(" ")
    if acc == "nop":
        pointer = pointer + 1
    elif acc == "acc":
        count = count + int(change)
        pointer = pointer + 1
    elif acc == "jmp":
        pointer = pointer + int(change)

print (count)
