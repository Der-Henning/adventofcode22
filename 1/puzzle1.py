import csv

elves = []
with open('input.txt', 'r') as file:
    elf = []
    for line in csv.reader(file):
        if len(line) == 0:
            elves.append(elf)
            elf = []
        else:
            elf.append(int(line[0]))

calories = []
for elf in elves:
    calories.append(sum(elf))

print('How many total Calories is that Elf carrying?')
print(f'Answer: {max(calories)}')

print('How many Calories are those Elves carrying in total?')
print(f'Answer: {sum(sorted(calories)[-3:])}')
