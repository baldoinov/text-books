import turtle
import math

def square(t, lenght):

    for i in range(4):
        t.fd(lenght)
        t.lt(90)


def polyline(t, n, lenght, angle):

    for i in range(n):
        t.fd(lenght)
        t.lt(angle)


def polygon(t, lenght, n):
    
    angle = 360 / n
    polyline(t, n, lenght, angle)


def circle(t, r):
    
    arc(t, r, 360)


def arc(t, r, angle):

    arc_lenght = (angle * math.pi * r) / 180
    n = int(arc_lenght / 3) + 1
    step_lenght = arc_lenght / n
    step_angle = angle / n

    polyline(t, n, step_lenght, step_angle)


bob = turtle.Turtle()
arc(bob, 50, 60)

turtle.mainloop()