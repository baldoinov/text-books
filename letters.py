import turtle
import math

def polyline(t, n, lenght, angle):

    for i in range(n):
        t.fd(lenght)
        t.lt(angle)


def polygon(t, lenght, n):
    
    angle = 360 / n
    polyline(t, n, lenght, angle)


def arc(t, r, angle):

    arc_lenght = (angle * math.pi * r) / 180
    n = int(arc_lenght / 3) + 1
    step_lenght = arc_lenght / n
    step_angle = angle / n

    polyline(t, n, step_lenght, step_angle)

def draw_a(t):
    
    bottom_angle = 70
    upper_angle = 180 - 2 * bottom_angle
    big_lines = 70
    small_lines = 40

    t.lt(bottom_angle)
    t.fd(big_lines)
    t.lt(upper_angle + 180)
    t.fd(small_lines)
    t.lt(bottom_angle + 180)
    t.fd(2 * math.cos(math.radians(big_lines)) * 40)
    t.lt(180)
    t.fd(2 * math.cos(math.radians(big_lines)) * 40)
    t.lt(360 - bottom_angle)
    t.fd(big_lines - small_lines)
    
def draw_b(t):

    t.fd(10)
    arc(t, r=17.5, angle=180)
    t.fd(10)
    t.lt(180)
    arc(t, r=17.5, angle=180)
    t.fd(10)
    t.lt(90)
    t.fd(70)
    

def draw_c(t):

    big_lines = 70
    radius = big_lines / 2

    t.pu()
    t.lt(90)
    t.fd(big_lines)
    t.lt(90)
    t.pd()
    arc(t, r=radius, angle=200)

def draw_d(t):

    big_lines = 70
    small_lines = 10
    radius = big_lines / 2

    t.fd(small_lines)
    arc(t, r=radius, angle=180)
    t.fd(small_lines)
    t.lt(90)
    t.fd(big_lines)
    t.lt(90)



bob = turtle.Turtle()  
draw_d(bob)
turtle.mainloop()