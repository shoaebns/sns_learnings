import random
import turtle
import math

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

pen = turtle.Turtle()

def init():
    random.seed(2023)

    # Setup the window.
    screen = turtle.Screen()
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)


def circle(rad):
    pen.circle(rad)


init()
circle(50)




pen.screen.mainloop()