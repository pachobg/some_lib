import turtle

dist = 1
flag = 600

spiral = turtle.Turtle()

spiral.speed(20)

while flag:
    spiral.forward(dist)

    spiral.right(90)
    spiral.right(1)
    dist += 1
    flag -= 1

turtle.done()