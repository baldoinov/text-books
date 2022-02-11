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


def polygon(t: turtle.Turtle, lenght: float, n: int) -> None:
    """Takes a turtle and draws a polygon with n side with the given lenght."""
    
    angle = 360 / n
    polyline(t, n, lenght, angle)


def d_circle(t: turtle.Turtle, r: float) -> None:
    """Takes a Turtle and a radius and draws a circle."""
    
    arc(t, r, 360)


def arc(t, r, angle):

    arc_lenght = (angle * math.pi * r) / 180
    n = int(arc_lenght / 3) + 1
    step_lenght = arc_lenght / n
    step_angle = angle / n

    polyline(t, n, step_lenght, step_angle)

if __name__ == '__main__':
    
    bob = turtle.Turtle()
    arc(bob, 50, 60)

    turtle.mainloop()