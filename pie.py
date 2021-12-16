import turtle
import math


def move(t, lenght):
    """Move Turtle forward without leaving a trail.
    Leaves the pen down.
    """

    t.pu()
    t.fd(lenght)
    t.pd()


def insider_triangle(t, left_turn, inner_lenght, outer_lenght):
    """Draws a triangle tha fits inside the given figure.
    
    t: Turtle
    inside_lenght: lenght os the segment that stays within the figure.
    left_turn: angle used to make the bottom corners of the triangle.
    outer_lenght: lenght of the bottom segment of the triangle.
    """

    t.fd(inner_lenght)
    t.lt(left_turn)
    t.fd(outer_lenght)
    t.lt(left_turn)
    t.fd(inner_lenght)
    t.lt(180)


def polygon(t, n_sides, inner_lenght):
    """Draws a polygon with line segment connecting all vertices.
    
    t: Turtle
    n_sides: number of sides of the polygon
    inner_lenght: size of the segment that connect the 'center' of the polygon to the vertex."""

    top_angle = 360 / n_sides
    bottom_angle = (180 - top_angle) / 2
    lturn = 180 - bottom_angle
    outter_lenght = 2 * math.sin(math.radians(top_angle / 2)) * inner_lenght

    for i in range(n_sides):
        insider_triangle(t, lturn, inner_lenght, outter_lenght)

bob = turtle.Turtle()

move(bob, -300)
polygon(bob, 5, 50)
move(bob, 300)
polygon(bob, 6, 50)
move(bob, 300)
polygon(bob, 7, 50)


turtle.mainloop()