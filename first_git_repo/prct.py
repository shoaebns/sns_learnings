import turtle

t = turtle.Turtle()

r = 10
  
# Loop for printing concentric circles
for i in range(50):
    t.circle(r * i)
    t.up()
    t.sety((r * i)*(-1))
    t.down()

if __name__ == "__main__":
    pass
