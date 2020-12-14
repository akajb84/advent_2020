import copy
def create_mask(line):
    _,_, mask = line.split()
    mask = list(mask)
    mask.reverse()
    return mask

def get_addresses(mask, mem):
    addresses = []
    bin_val = [int(m) for m in list(bin( mem )[2:])]
    bin_val.reverse()

    x_addr = []
    new_val = [0] * 36
    for i, num in enumerate(mask):
        if num == "0":
            if i < len(bin_val):
                new_val[i] = bin_val[i]
        elif num == "1":
            new_val[i] = 1
        else:
            new_val[i] = -1
            x_addr.append(i)

    for i in range(0, 2 ** len(x_addr)):
        cur_vals = [int(m) for m in list(bin( i )[2:])]
        if len(cur_vals) < len(x_addr):
            cur_vals = [0] * (len(x_addr) - len(cur_vals)) + cur_vals
        cur_vals.reverse()
        addr = copy.deepcopy(new_val)
        for j, x in enumerate(x_addr):
            addr[x] = cur_vals[j]

        addr.reverse()
        value = [str(m) for m in addr]
        val = "".join(value)
        num = int(val, 2)
        addresses.append(num)

    return addresses


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

        mem_addresses = get_addresses(mask, mem)

        for a in mem_addresses:
            memory[a] = val

# print (memory)
total = 0
for key in memory:
    total = total + memory[key]

print (total)

