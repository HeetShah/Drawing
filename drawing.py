import turtle
import random
turtle.colormode(255)

turtle.speed(500)


turtle.pensize(2)

for i in range(100):
    turtle.up()
    turtle.goto(0,-4*i)
    turtle.down()
    mr=random.randint(0,255)
    mg=random.randint(0,255)
    mb=random.randint(0,255)
    turtle.color(mr,mg,mb)
    turtle.circle(10+4*i)