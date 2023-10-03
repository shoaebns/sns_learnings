
ROWS = 26
for count in range(1, ROWS + 1):
    star = '*' * count
    alphabet = chr(96 + count)  
    print(f'{count} {star}{alphabet * count}')


    
