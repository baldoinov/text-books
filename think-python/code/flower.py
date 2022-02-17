import turtle
import math


def polyline(t, n, lenght, angle):
    """Draws n line segments with an left turn.

    t: Turtle object
    n: number of segments
    lenght: size of each segments
    angle: degrees between segments
    """

    for i in range(n):
        t.fd(lenght)
        t.lt(angle)


def arc(t, r, angle):
    """Draws an arc with the given radius and angle
    
    t: Turtle object
    r: radius
    angle: angle in degrees
    """

    arc_lenght = (angle * math.pi * r) / 180
    n = int(arc_lenght / 3) + 1
    step_lenght = arc_lenght / n
    step_angle = angle / n

    polyline(t, n, step_lenght, step_angle)

def petal(t, r, angle):
    """Draws a petal using two arcs.
    """
    for i in range(2):
        arc(t, r, angle)
        t.lt(180 - angle)

def flower(t, r, angle, petals):
    """Draws a flower with the given number of petals.
    
    t: Turtle object
    r: size of the petal
    angle: shape of the petal
    petals: number of petals
    """

    for i in range(petals):
        petal(t, r, angle)
        t.lt(360 / petals)


def move(t, lenght):
    """Move Turtle without forward without leaving a trail.
    Leaves the pen down.
    """

    t.pu()
    t.fd(lenght)
    t.pd()

bob = turtle.Turtle()

move(bob, -200)
flower(bob, 60, 60, petals=7)

move(bob, 200)
flower(bob, 60, 80, petals=10)

move(bob, 200)
flower(bob, 100, 30, petals=20)

bob.hideturtle()
turtle.mainloop()