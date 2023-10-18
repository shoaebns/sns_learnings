# "New" means new compared to previous level
provincial_capitals = {
    'BC': 'Victoria',
    'Manitoba': 'Winnipeg',
    'Nunavut': 'Iqaluit',
    'Ontario': 'Toronto'
}

province_name = input()
while province_name != 'exit':
    if province_name in provincial_capitals:
        print(provincial_capitals[province_name])
        del provincial_capitals[province_name] # New line
    else:
        print('x')
    province_name = input()