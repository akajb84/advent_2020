file = open('7_input.txt', 'r')
lines = file.readlines()

count = 0

bags = {}

for line in lines:

    line = line.strip()
    # dark gray bags contain 5 dim bronze bags.
    # plaid tan bags contain 4 light coral bags, 2 dim fuchsia bags, 3 mirrored coral bags.
    # dotted black bags contain no other bags.
    if "contain no other bags" in line:
        tokens = line.split("bags")
        bags[tokens[0]] = {}

    else:
        tokens = line.split ("bags contain")
        key = tokens[0]
        # print(key)
        colours = tokens[1].strip().split(" ")
        i = 0
        # print(colours)
        bags[key] = {}
        while (i < len(colours)):
            count = int(colours[i])
            i = i + 1
            parts = []
            while ("bag" not in colours[i]):
                parts.append(colours[i])
                i = i + 1
            ind_key = " ".join(parts)
            # print (ind_key)
            # print(bags[key])
            bags[key][ind_key] = count
            i = i + 1


colour_set = []
seen = []
# seen.add("shiny gold")
new_colours = []
cur_colour = "shiny gold"
keep = True
while keep:
    # print(cur_colour)
    for a in bags:
        if cur_colour in bags[a].keys():
            colour_set.append(a.strip())

    new_colours = set(new_colours) | (set(colour_set) - set(seen))
    seen = set(seen) | set(colour_set)
    colour_set = []

    if new_colours:
        cur_colour = new_colours.pop()
    else:
        keep = False


print (seen)
print (len(seen))
