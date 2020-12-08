file = open('2_1_input.txt', 'r')
lines = file.readlines()

# example input: 1-4 j: jjjqzmgbjwpj
valid = 0
for line in lines:
    rules, pw = line.split(':')
    pw = pw.strip()
    count, letter = rules.split()
    letter = letter.strip(":")
    min_count, max_count = count.split('-')
    min_count = int(min_count)
    max_count = int(max_count)

    if (pw[min_count-1] == letter) ^ (pw[max_count-1] == letter):
        valid = valid + 1

print (valid)
