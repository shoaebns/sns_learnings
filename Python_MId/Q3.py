import random
import turtle
import math

SCREEN_WIDTH = 2000 
SCREEN_HEIGHT = 1200

SPEED = 0  
EAST = 0  
NORTH = 90  
SOUTH = 270  
WEST = 180  



def init():
    random.seed(2023)
    screen = turtle.Screen()
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)


def draw_axis(turtle):
    turtle.hideturtle()
    turtle.speed(SPEED)
    turtle.goto(-500,0)
    turtle.forward(1000)
    turtle.up()
    turtle.goto(0,-500)
    turtle.down()
    turtle.setheading(NORTH)
    turtle.forward(1000)
    turtle.up()

def draw_circles(turtle):
    COLORS = ["beige", "coral", "gold", "blue", "green"]
    x_pos = 50
    y_pos = 0
    rad = 50
    for circle in range(30):
       
        color_type = random.randint(0, len(COLORS) - 1)

        turtle.up()
        turtle.goto(x_pos, y_pos)  
        turtle.down()
        turtle.pencolor(COLORS[color_type])
        turtle.circle(rad)  
        
        rad += 10  
        x_pos += 10

def draw_sqr(turtle):
    turtle.up()
    turtle.goto(340, -340)  
    turtle.down()
    turtle.pencolor("red")

    for line in range(4):
        turtle.forward(680)  
        turtle.left(90)


def main():
    exam = turtle.Turtle()
    init()
    draw_axis(exam)
    draw_circles(exam)
    draw_sqr(exam)

    exam.screen.mainloop()


main()

    






