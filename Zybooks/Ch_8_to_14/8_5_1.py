full_name = input().split(' ')
if len(full_name)==3:
    print(f'{full_name[2]}, {full_name[0][0]}.{full_name[1][0]}.')
else:
    print(f'{full_name[1]}, {full_name[0][0]}.')
