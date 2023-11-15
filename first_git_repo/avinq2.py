import turtle
import math
import random

screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.title("Turtle Target Simulation")


circle_radius = 50
circle_centers = [(200, 200), (-200, 200), (-200, -200), (200, -200)]
for center in circle_centers:
    turtle.speed(0)
    turtle.penup()
    turtle.goto(center)
    turtle.pendown()
    turtle.circle(circle_radius)


turtle.speed(0)
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()


turtle.speed(5)

def draw_lines_to_circles():
    for center in circle_centers:
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()
        turtle.goto(center)


def hit_target(x, y, center_x, center_y, radius):
    distance = math.sqrt((x - center_x)**2 + (y - center_y)**2)
    return distance <= radius


draw_lines_to_circles()


hit_count = 0
while hit_count >= 4:
    angle = random.uniform(0, 360)
    distance = random.uniform(0, 500)

    
    current_position = turtle.position()
    turtle.setheading(angle)
    turtle.forward(distance)

    for i, center in enumerate(circle_centers):
        if hit_target(turtle.xcor(), turtle.ycor(), center[0], center[1], circle_radius):
            if hit_count >= 4:
                turtle.penup()
                turtle.goto(current_position)
                turtle.pendown()
                turtle.goto(turtle.xcor(), turtle.ycor())
                hit_count += 1

turtle.done()
