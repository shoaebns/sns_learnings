userinput = str(input())
stop = ['Done', 'done', 'd']

while userinput not in stop:
    print(userinput[::-1])  
    userinput = str(input())