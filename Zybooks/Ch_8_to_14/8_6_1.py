while 1 :
    user_text = input().split()
    word = (user_text[0])
    number = (user_text[1])
    if word =='quit':
        break
    else:
        print(f'Eating {number} {word} a day keeps you happy and healthy.')
    


