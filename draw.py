"""
Write a function called draw_rect that takes a Turtle object and a Rectangle and uses the Turtle 
to draw the Rectangle.
Write a function called draw_circle that takes a Turtle and a Circle and draws the Circle
"""

import turtle

from polygon import d_circle, polygon
from Circle import Circle, Rectangle, Point

def draw_rect(t: turtle.Turtle, r: Rectangle) -> None:
    """Takes a Turtle and a Rectangle and draws the Rectangle."""
    
    t.pu()
    t.setposition(r.corner.x, r.corner.y)
    t.pd()

    for i in range(2):
        t.fd(r.width)
        t.lt(90)
        t.fd(r.height)
        t.lt(90)


def draw_circle(t: turtle.Turtle, c: Circle) -> None:
    """Takes a Turtle and a Circle and draws the Circle."""

    # Localizar o centro e se afastar radius dele
    # Desenhar o circulo a partir desse ponto

    t.pu()
    t.setposition(0, c.center.y + c.radius)
    t.pd()

    d_circle(t, r=c.radius)


if __name__ == '__main__':
    bob = turtle.Turtle()
    
    # rect = Rectangle()
    # rect.width, rect.height, rect.corner = 100, 200, Point()
    # rect.corner.x, rect.corner.y = 50, 0
    # draw_rect(bob, rect)

    circle = Circle()
    circle.radius, circle.center = 75, Point()
    circle.center.x, circle.center.y = 150, 100
    draw_circle(bob, circle)

    turtle.mainloop()