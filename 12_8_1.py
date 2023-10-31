user_num = input()
div_num = input()
test=0


try:
    print(int(user_num) // int(div_num))
except ZeroDivisionError:
    print("Zero Division Exception: integer division or modulo by zero")
except ValueError:
    user_num1 = str(user_num)
    if user_num1.isnumeric():
        test = div_num
    else:
        test = user_num
    print(f"Input Exception: invalid literal for int() with base 10: '{test}'")
   