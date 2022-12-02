import numpy as np

data = np.genfromtxt('input.txt', delimiter=' ',
                     dtype='S').view(np.uint8).astype(int)

total_score = (3 * ((data[:, 1] - data[:, 0] - 25) % 3)
               + data[:, 1] - 87).sum()

print('1. What would your total score be if everything goes exactly according to your strategy guide?')
print(f'Answer: {total_score}')

total_score2 = ((data[:, 1] + data[:, 0] - 22) % 3 + 1
                + 3 * (data[:, 1] - 88)).sum()

print('2. What would your total score be if everything goes exactly according to your strategy guide?')
print(f'Answer: {total_score2}')
