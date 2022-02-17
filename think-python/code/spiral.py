import turtle
import math

def spiral(t, r):
    """Draws a spiral with the given radius.
    
    t: Turtle
    r: radius
    """

    for i in range(r):
        t.fd(5 + i)
        t.rt(15)

bob = turtle.Turtle()

spiral(bob, 5)

turtle.mainloop()