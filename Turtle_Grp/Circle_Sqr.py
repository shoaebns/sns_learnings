import turtle

# avoid magic numbers
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
SKIP_DISTANCE = 40
SIDE_LENGTH = 60
NINETY_DEGREE = 90
REVERSE_DEGREE = 180
RADIUS = 70

screen = turtle.Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

# create a turtle
t = turtle.Turtle()

# move to right without drawing
t.penup()
t.forward(SKIP_DISTANCE)
t.pendown()

# reverse and draw a green circle
t.right(REVERSE_DEGREE)
t.color("green")
t.circle(RADIUS)

# reverse and draw a blue square
t.right(REVERSE_DEGREE)
t.color("blue")
t.forward(SIDE_LENGTH)
t.left(NINETY_DEGREE)
t.forward(SIDE_LENGTH)
t.left(NINETY_DEGREE)
t.forward(SIDE_LENGTH)
t.left(NINETY_DEGREE)
t.forward(SIDE_LENGTH)

t.screen.mainloop()