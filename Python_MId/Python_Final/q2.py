import math
import random
import turtle

SCREEN_WIDTH = 800  # Screen width
SCREEN_HEIGHT = 800  # Screen height
MAX_DISTANCE = math.ceil(math.sqrt(SCREEN_HEIGHT**2 + SCREEN_HEIGHT**2) / 2)

SPEED = 0

def init():
    random.seed(2023)
    screen = turtle.Screen()
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

def draw_target(ttl):
    ttl.hideturtle()
    ttl.speed(SPEED)
    ttl.up()
    ttl.goto(200, 200)
    ttl.down()
    ttl.circle(50)
    ttl.up()
    ttl.goto(-200, 200)
    ttl.down()
    ttl.circle(50)
    ttl.up()
    ttl.goto(200, -200)
    ttl.down()
    ttl.circle(50)
    ttl.up()
    ttl.goto(-200, -200)
    ttl.down()
    ttl.circle(50)
    ttl.up()

def launch_test(ttl):
    is_hit = False
    while not is_hit:
        ttl.home()
        ttl.showturtle()
        ttl.speed(SPEED)
        angle = random.randint(0, 360)
        distance = random.randint(0, MAX_DISTANCE + 1)
        ttl.setheading(angle)
        ttl.down()
        ttl.forward(distance)

        is_hit = check_hit(ttl)
        





def check_hit(ttl):
    xcor = ttl.xcor()
    ycor = ttl.ycor()
    dist_circle1 = math.sqrt((xcor - 200) ** 2 + (ycor - 200) ** 2)
    dist_circle2 = math.sqrt((xcor - (-200)) ** 2 + (ycor - 200) ** 2)
    dist_circle3 = math.sqrt((xcor - 200) ** 2 + (ycor - (-200)) ** 2)
    dist_circle4 = math.sqrt((xcor - (-200)) ** 2 + (ycor - (-200)) ** 2)

    return (dist_circle1 <= 50) and (dist_circle2 <= 50) and (dist_circle3 <= 50) and (dist_circle4 <= 50)

    



def main():
    init()
    my_turtle = turtle.Turtle()
    draw_target(my_turtle)
    launch_test(my_turtle)

    my_turtle.screen.mainloop()

main()