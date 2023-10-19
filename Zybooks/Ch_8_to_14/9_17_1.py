user_in = input().split(' ')
contact_details = []
for item in user_in:
    contact_details.append(item.split(','))
search_item = input()
for name in contact_details:
    for i in range(len(contact_details)):
        if name[i] == search_item:
            print(name[1])
        else:
            break
