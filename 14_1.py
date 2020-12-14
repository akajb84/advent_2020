def create_mask(line):
    _,_, mask = line.split()
    mask = list(mask)
    mask.reverse()
    return mask

file = open('14_input.txt', 'r')
lines = file.readlines()

lines = [line.strip() for line in lines]

memory = {}

for l in lines:
    if "mask" in l:
        mask = create_mask(l)
    else:
        mem, _, val = l.split()
        mem = mem[4:]
        mem = int(mem[:-1])
        val = int(val)

        bin_val = [int(m) for m in list(bin( val )[2:])]
        bin_val.reverse()

        new_val = [0] * 36
        for i, num in enumerate(mask):
            if num == "X":
                if i < len(bin_val):
                    new_val[i] = bin_val[i]
            else:
                new_val[i] = int(mask[i])

        memory[mem] = new_val

# print (memory)
total = 0
for key in memory:
    value = memory[key]
    value.reverse()
    value = [str(m) for m in value]
    val = "".join(value)
    num = int(val, 2)
    total = total + num

print (total)

