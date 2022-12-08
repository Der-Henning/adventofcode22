import pandas as pd

df = pd.read_fwf('input_board.txt', header=None)
df.columns = df.iloc[-1].values
df = df.drop(df.index.values[-1])

board = dict()

for col in df.columns:
    board[col] = df[col].dropna().to_list()
    board[col].reverse()

with open('input_moves.txt', 'r') as file:
    for line in file.readlines():
        arr = line.split(' ')
        for i in range(int(arr[1])):
            board[arr[5].strip()].append(board[arr[3]].pop())


answer = ''.join([board[key][-1] for key in board.keys()]
                 ).replace('[', '').replace(']', '')

print('After the rearrangement procedure completes, what crate ends up on top of each stack?')
print(f'Answer: {answer}')


# part 2
board = dict()

for col in df.columns:
    board[col] = df[col].dropna().to_list()
    board[col].reverse()

with open('input_moves.txt', 'r') as file:
    for line in file.readlines():
        arr = line.split(' ')
        tmp = []
        for i in range(int(arr[1])):
            tmp.append(board[arr[3]].pop())
        for i in range(int(arr[1])):
            board[arr[5].strip()].append(tmp.pop())

answer = ''.join([board[key][-1] for key in board.keys()]
                 ).replace('[', '').replace(']', '')

print('After the rearrangement procedure completes, what crate ends up on top of each stack?')
print(f'Answer: {answer}')
