numbers = [6, 7, -7, -6]
for position, number in enumerate(numbers):
    if number < 0:
        print(f'{position} {number}')
    else:
        print(f'{position} x')