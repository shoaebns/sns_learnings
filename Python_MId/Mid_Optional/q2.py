import random
import turtle
import math
SCREEN_WIDTH = 2000 
SCREEN_HEIGHT = 1200
def init():
    random.seed(2023)
    screen = turtle.Screen()
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    


def draw_sqrs_circle(turtle):
    turtle.hideturtle()
    COLORS = ["red", "green", "blue"]
    x_pos = -50
    y_pos = -50
    gap = 100
    turtle.speed(0)
    for square in range(20):
        turtle.up()
        turtle.goto(x_pos,y_pos)
        turtle.down()
        turtle.pencolor(random.choice(COLORS))
        for turn in range(4):
            turtle.forward(gap)
            turtle.left(90)
        x_pos -= 10
        y_pos -= 10
        gap += 20
    
    turtle.pencolor(random.choice(COLORS))
    turtle.penup()
    turtle.goto(0,(x_pos + 10)*math.sqrt(2))
    turtle.setheading(180)
    turtle.pendown()
    turtle.circle((x_pos + 10)*math.sqrt(2))



def main():
    exam = turtle.Turtle()
    init()
    draw_sqrs_circle(exam)

  

    exam.screen.mainloop()


main()
