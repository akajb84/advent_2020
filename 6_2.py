file = open('6_input.txt', 'r')
lines = file.readlines()

count = 0

bla = {}
people = 0
for line in lines:

    line = line.strip()
    if line:
        for a in line:
            if a in bla:
                bla[a] =  bla[a] + 1
            else:
                bla[a] = 1
        people = people + 1

    else:
        # print(bla)
        # print(people)
        # empty line, count old set
        num = 0
        for a in bla:
            if bla[a] == people:
                num = num + 1

        count = count + num
        people = 0
        bla = {}

num = 0
for a in bla:
    if bla[a] == people:
        num = num + 1

count = count + num
people = 0
bla = {}

print (count)