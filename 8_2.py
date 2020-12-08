def do_instruction(pointer, count, seen, changed):
    if pointer in seen:
        # print("seen before " + str(pointer))
        return

    seen.append(pointer)

    if (pointer >= len(lines)):
        # print (pointer)
        print("changed " + str(changed))
        print(count)
        print(seen)
        return

    action = lines[pointer]
    acc, change = action.strip().split(" ")
    if acc == "nop":
        do_instruction(pointer + 1, count, seen, changed)
        if changed < 0:
            # print("change to jump " + str(pointer))
            do_instruction(pointer + int(change), count, seen, pointer)


    elif acc == "acc":
        count = count + int(change)
        do_instruction(pointer + 1, count, seen, changed)
    elif acc == "jmp":
        do_instruction(pointer + int(change), count, seen, changed)
        if changed < 0:
            # print("change to nop " + str(pointer))
            do_instruction(pointer + 1, count, seen, pointer)

    # print (count)
    # print(seen)
    return


file = open('8_input.txt', 'r')
lines = file.readlines()

do_instruction(0, 0, [], -1)
