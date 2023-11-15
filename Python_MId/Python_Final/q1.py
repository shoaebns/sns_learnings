def signature(firstname_lastname):
    sum = 0
    for char in firstname_lastname :
            sum += ord(char)
    start_line = 7 + sum % 17
    return (start_line, start_line + 30, start_line + 60)

signature('Shoaeb_Shaik')
