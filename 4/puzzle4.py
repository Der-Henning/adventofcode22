import numpy as np
import csv

pairs = []
with open('input.txt', 'r') as file:
    for line in csv.reader(file, delimiter=','):
        pairs.append([np.arange(int(assignment.split('-')[0]),
                     int(assignment.split('-')[1]) + 1) for assignment in line])


num_of_pairs = np.sum([np.any([np.array_equal(np.intersect1d(
    *pair), assignment) for assignment in pair]) for pair in pairs])

print('In how many assignment pairs does one range fully contain the other?')
print(f'Answer: {num_of_pairs}')

num_of_pairs = np.sum([len(np.intersect1d(*pair)) > 0 for pair in pairs])

print('In how many assignment pairs do the ranges overlap?')
print(f'Answer: {num_of_pairs}')
