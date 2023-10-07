def draw_triangle(n):
    spaces = 9 - n // 2  # Ensures correct spacing for each line
    if n == 1:
        print(spaces * ' ' + '*')
    else:
        draw_triangle(n-2)
        print(spaces * ' ' + n * '*')

user_input = int(input())

draw_triangle(user_input)