num_rows = int(input())
num_cols = int(input())

curr_row = 0

for row in range(num_rows):
    curr_col_let = 'A'
    curr_row = curr_row + 1
    for col in range(num_cols):

        print (f'{curr_row}{curr_col_let}', end=' ')
        curr_col_let = chr(ord(curr_col_let) + 1)
    print()

    
