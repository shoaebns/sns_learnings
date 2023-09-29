import turtle
import math
import random



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
angle_list = []
zero_list = []
frequency = []
max = 0
ans = -1
for j in range(360):
    frequency.insert(j,0)
def initialize():
    # for repeatable experiments
    random.seed(2023)

    # Setup the window.
    screen = turtle.Screen()
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)


def start_test():
    for r in range(100):
        turtle.home()
        turtle.showturtle()
        turtle.speed(SPEED)
    
        angle = random.randint(0, 360)
        distance = random.randint(0, MAX_DISTANCE + 1)
        angle_list.append(angle)
        turtle.setheading(angle)
        turtle.down()
        turtle.forward(distance)
        r += 1


    

    for j in range(360):
        frequency.insert(angle,frequency[angle]+1)
        if max< frequency[angle]:
            max = frequency[angle]
            ans = angle
        
        print(ans,max)
    
        



initialize()       
start_test()


turtle.mainloop()

