from turtle import *
speed(11)
bgcolor("black")
for i in range(0, 601):
    if i % 2 == 0:
        pencolor("blue")
    elif i % 3 == 0:
        pencolor("red")

    else:
        pencolor("green")
    forward(i * 3)
    right(121)
done()
