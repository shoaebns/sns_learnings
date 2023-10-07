par_allowed = (3, 4, 5)
par = int(input())
strokes = int(input())

if par in par_allowed:
    if par == strokes:
        print('Par')
    elif par - 2 == strokes:
        print('Eagle')
    elif par -1 == strokes:
        print('Birdie')
    elif par + 1 == strokes:
        print('Bogey')
else:
    print('Error')