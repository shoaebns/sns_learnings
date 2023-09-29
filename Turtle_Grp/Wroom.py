import turtle
import math
import random
import Hit_Target as ht

SCREEN_WIDTH = 600  # Screen width
SCREEN_HEIGHT = 600  # Screen height
MAX_DISTANCE = math.ceil(math.sqrt(SCREEN_HEIGHT**2 + SCREEN_HEIGHT**2) / 2)

TARGET_LOWER_LEFT_X = 100  # Target's lower-left X
TARGET_LOWER_LEFT_Y = 100  # Target's lower-left Y
TARGET_WIDTH = 100  # Width of the target

SPEED = 0  # Projectile's animation speed

EAST = 0  # Angle of east direction
NORTH = 90  # Angle of north direction
SOUTH = 270  # Angle of south direction
WEST = 180  # Angle of west direction

ht.initialize()

def start_test():
    turtle.home()
    turtle.showturtle()
    turtle.speed(SPEED)
    for r in range(100):
        angle = random.randint(0, 360)
        distance = random.randint(0, MAX_DISTANCE + 1)
        turtle.setheading(angle)
        turtle.down()
        turtle.forward(distance)
        r += 1
        
        start_test()

