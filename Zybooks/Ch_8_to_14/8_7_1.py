userEntered = input()
result = ''
for char in userEntered:
    if char.isalpha():
        result += char
print(result)