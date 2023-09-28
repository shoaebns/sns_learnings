# TODO: Write recursive print_num_pattern() function
def print_num_pattern(num1, num2):
    t= num1
    print(t, end=" ")
    while t>=0:
        print(t-num2, end= " ")
        t-=num2
    while t<num1:
        print(t+num2, end= " ")
        t+=num2
if __name__ == "__main__":
    num1 = int(input())
    num2 = int(input())
    print_num_pattern(num1, num2)