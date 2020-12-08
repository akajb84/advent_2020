file = open('4_input.txt', 'r')
lines = file.readlines()

"""
byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid
"""

checked = [False, False, False, False, False, False, False]

count = 0
for line in lines:
    print (line)
    if line == "\n":
        # starting new passport
        # check if previous is valid:
        if False not in checked:
            count = count + 1
            print("valid")
        else:
            print ("invalid")

        #reset
        checked = [False, False, False, False, False, False, False]

    else:
        if "byr" in line:
            checked[0] = True
        if "iyr" in line:
            checked[1] = True
        if "eyr" in line:
            checked[2] = True
        if "hgt" in line:
            checked[3] = True
        if "hcl" in line:
            checked[4] = True
        if "ecl" in line:
            checked[5] = True
        if "pid" in line:
            checked[6] = True

print (count)