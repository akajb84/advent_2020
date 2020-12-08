def num_of_colour(colour):
    total = 1
    if colour in bags:
        # print ("here")
        # print(colour)
        for b in bags[colour]:
            # print (bags[colour])
            total = total + (bags[colour][b] * num_of_colour(b))
            # print (total)
    return total

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
        key = tokens[0].strip()
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
            bags[key][ind_key.strip()] = count
            i = i + 1


bla = num_of_colour("shiny gold")
print (bla - 1)

