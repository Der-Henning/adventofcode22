import numpy as np
import csv
from functools import reduce

backpacks = []
with open('input.txt', 'r') as file:
    for line in csv.reader(file):
        arr = (np.array(list(line[0]), dtype='S')
               .view(np.uint8)
               .astype(int))
        arr = np.where(arr > 96, arr - 96, arr - 38)
        backpacks.append(arr)

intersections = []
for backpack in backpacks:
    compartments = [np.array(x) for x in np.array_split(backpack, 2)]
    intersection = np.intersect1d(*compartments)
    intersections.append(intersection[0])

print('What is the sum of the priorities of those item types?')
print(f'Answer: {sum(intersections)}')

priorities = []
for group in np.array_split(np.array(backpacks, dtype=object), len(backpacks)/3):
    priorities.append(reduce(np.intersect1d, group)[0])

print('What is the sum of the priorities of those item types?')
print(f'Answer: {sum(priorities)}')
