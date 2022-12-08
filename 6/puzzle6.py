def find_start(message: str, marker_length: int = 4) -> int:
    for idx, x in enumerate(message):
        if len(set(message[idx-marker_length:idx])) == marker_length:
            return idx


with open('input.txt', 'r') as file:
    message = file.readline()

print('How many characters need to be processed before the first start-of-packet marker is detected?')
print(f'Answer: {find_start(message)}')

# part 2

print('How many characters need to be processed before the first start-of-message marker is detected?')
print(f'Answer: {find_start(message, 14)}')
