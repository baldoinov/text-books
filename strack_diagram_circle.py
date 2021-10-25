import turtle
import math


def polyline(t, n, lenght, angle):
    """Draws n line segments.

    t: Turtle object
    n: number of segments
    lenght: size of each segments
    angle: degrees between segments
    """

    stack_diagram("POLYLINE")
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

    stack_diagram("ARC")
    polyline(t, n, lenght=step_lenght, angle=step_angle)


def circle(t, r):
    """Draws a circle with the given radius.

    t: Turtle object
    r: radius
    """
    stack_diagram("CIRCLE")
    arc(t, r, 360)


def stack_diagram(text):

    print("- " * (len(text)))
    print(f"- {text} -")
    print("- " * (len(text)))

stack_diagram("MAIN")
bob = turtle.Turtle()
circle(bob, 25)