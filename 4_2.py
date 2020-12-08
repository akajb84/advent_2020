import string

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

doc = {}

count = 0
for line in lines:
    #print (line)
    if line == "\n":
        # starting new passport
        # check if previous is valid:
        doNext = False
        if "byr" in doc:
            # four digits; at least 1920 and at most 2002
            doNext = 1920 <= int(doc["byr"]) <= 2002
            if not doNext:
                print ("BYR")
        else:
            doNext = False
        if doNext and "iyr" in doc:
            # four digits; at least 2010 and at most 2020.
            doNext = 2010 <= int(doc["iyr"]) <= 2020
            if not doNext:
                print ("IYR")
        else:
            doNext = False
        if doNext and "eyr" in doc:
            # four digits; at least 2020 and at most 2030.
            doNext = 2020 <= int(doc["eyr"]) <= 2030
            if not doNext:
                print ("EYR")
        else:
            doNext = False
        if doNext and "hgt" in doc:
            # a number followed by either cm or in:
            # If cm, the number must be at least 150 and at most 193.
            # If in, the number must be at least 59 and at most 76.
            if len(doc["hgt"]) >= 4:
                height = int(doc["hgt"][:-2])
                if "cm" == doc["hgt"][-2:]:
                    doNext = 150 <= height <= 193
                elif "in" == doc["hgt"][-2:]:
                    doNext = 59 <= height <= 76
                else:
                    doNext = False
            else:
                doNext = False
            if not doNext:
                print ("HGT")
        else:
            doNext = False
        if doNext and "hcl" in doc:
            # a # followed by exactly six characters 0-9 or a-f.
            doNext = doc["hcl"][0] == "#"
            if doNext:
                doNext = all(c in string.hexdigits for c in doc["hcl"][1:])
            if not doNext:
                print ("HCL")
        else:
            doNext = False
        if doNext and "ecl" in doc:
            # exactly one of: amb blu brn gry grn hzl oth.
            doNext = doc["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
            if not doNext:
                print ("ECL")
        else:
            doNext = False
        if doNext and "pid" in doc:
            # a nine-digit number, including leading zeroes.
            val = doc["pid"]
            doNext = len(val) == 9 and val.isnumeric()
            if not doNext:
                print ("PID")
        else:
            doNext = False


        if doNext:
            count = count + 1
            # print("VALID")
        else:
            print (doc)
            print ("INVALID")

        #reset
        doc = {}

    else:
        line = line.strip()
        tokens = line.split()
        for t in tokens:
            key, value = t.split(":")
            doc[key] = value



print (count)