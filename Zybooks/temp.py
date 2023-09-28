def int_to_reverse_binary(x):
    str= ""
    while(x!=0):
        if(x%2 == 0):
            str += "0"
        else:
            str += "1"
        x= x>>1
    return string_reverse(str)
def string_reverse(input_string):
    return input_string[::-1]
if __name__ == '__main__':
    user_input = int(input())
    print(int_to_reverse_binary(user_input))