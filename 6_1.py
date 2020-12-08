file = open('6_input.txt', 'r')
lines = file.readlines()

#BBFFBFB LLR

count = 0

bla = []
for line in lines:

    line = line.strip()
    if line:
        for a in line:
            bla.append(a)

    else:
        # empty line, count old set
        count = count + len(set(bla))
        bla = []

count = count + len(set(bla))
print (count)