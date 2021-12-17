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


def diagonal(t, lenght, angle):
    """ Draws a diagonal with a given lenght and forming a given angle
    with a bottom part of an imaginary square.
    """

    t.lt(angle)
    t.fd(lenght)
    t.lt((2 * (180 - angle) + angle))


def diagonal_back_in_place(t, lenght, angle):
    """ Draws a diagonal with a given lenght and forming a given angle
    with a bottom part of an imaginary square.
    """

    t.lt(angle)
    t.fd(lenght)
    t.lt(180)
    t.fd(lenght)
    if (angle >= 0) and (angle <= 180):
        t.lt((2 * (180 - angle) + angle))
    elif (angle > 180):
        t.rt(angle - 180)
    else:
        t.lt(180 - angle)
    


def forward_and_back(t, lenght):
    """Draws a line segment with the give lenght and leaves the turtle
    back where it started.
    """
    t.fd(lenght)
    t.pu()
    t.lt(180)
    t.fd(lenght)
    t.pd()
    t.lt(180)


def leave_at_origin(t):
    """Leaves the turtle back where it started.

    t: Turtle.
    lenght: size of line segment to get back to the origin.
    """

    t.pu()
    t.goto(0, 0)
    t.pd()

def draw_a(t, lenght):
    
    bottom_angle = 70
    upper_angle = 180 - 2 * bottom_angle
    small_lines = lenght - 30

    diagonal(t, small_lines, bottom_angle)
    forward_and_back(t, (2 * math.cos(math.radians(lenght)) * small_lines))
    diagonal(t, 30, bottom_angle)
    diagonal(t, lenght, (upper_angle + bottom_angle + 180))
    leave_at_origin(t, (2 * math.sin(math.radians(upper_angle / 2)) * lenght))

    
def draw_b(t):

    t.fd(10)
    arc(t, r=17.5, angle=180)
    t.fd(10)
    t.lt(180)
    arc(t, r=17.5, angle=180)
    t.fd(10)
    t.lt(90)
    t.fd(70)
    t.lt(90)
    leave_at_origin(t)


def draw_c(t):

    big_lines = 70
    radius = big_lines / 2

    t.pu()
    t.lt(90)
    t.fd(big_lines)
    t.lt(90)
    t.pd()
    arc(t, r=radius, angle=200)
    leave_at_origin(t)


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
    leave_at_origin(t)


def draw_e(t):

    big_lines = 70
    small_lines = 70 / 3
    
    def spin_and_relocate(tur, lenght):
        tur.lt(270)
        tur.fd(lenght)
        tur.lt(90)

    forward_and_back(t, small_lines)
    t.lt(90)
    t.fd(big_lines)
    t.lt(270)
    forward_and_back(t, small_lines)
    spin_and_relocate(t, 35)
    forward_and_back(t, small_lines)
    leave_at_origin(t)

def draw_f(t):

    big_lines = 70
    small_lines = big_lines / 3

    t.lt(90)
    t.fd(big_lines - 30)
    t.lt(270)
    forward_and_back(t, small_lines)
    t.lt(90)
    t.fd(30)
    t.lt(270)
    forward_and_back(t, (big_lines / 2))
    t.lt(90)
    leave_at_origin(t, big_lines)
    t.lt(270)


def draw_g(t):

    big_lines = 70
    radius = big_lines / 2

    t.pu()
    t.lt(90)
    t.fd(big_lines)
    t.lt(90)
    t.pd()
    arc(t, r=radius, angle=270)
    t.lt(90)
    forward_and_back(t, radius)


def draw_h(t):
    
    big_line = 70
    small_line = big_line / 2

    t.lt(90)
    forward_and_back(t, big_line)
    t.fd(small_line)
    t.lt(270)
    t.fd(small_line)
    t.lt(90)
    forward_and_back(t, small_line)
    t.lt(180)
    t.fd(small_line)
    leave_at_origin(t)


def draw_i(t):
    
    t.fd(15)
    t.lt(90)
    t.fd(70)
    t.lt(270)
    forward_and_back(t, 15)
    t.lt(180)
    forward_and_back(t, 15)
    t.lt(90)
    t.fd(70)
    t.lt(90)
    t.fd(15)
    leave_at_origin(t)


def draw_j(t):
    
    
    t.lt(270)
    arc(t, 15, 180)
    t.fd(55)
    t.lt(90)
    forward_and_back(t, 15)
    t.lt(180)
    forward_and_back(t, 15)
    leave_at_origin(t)


def draw_k(t):
    
    big_line = 70
    small_line = big_line / 2

    t.lt(90)
    t.fd(small_line)
    t.rt(90)
    diagonal_back_in_place(t, ( small_line/ (math.cos(math.radians(30)))), 300)
    diagonal_back_in_place(t, (small_line / (math.cos(math.radians(30)))), 60)
    t.lt(270)
    t.fd(small_line)
    t.lt(270)
    leave_at_origin(t)

def draw_l(t):

    forward_and_back(t, 50)
    t.lt(90)
    forward_and_back(t, 70)
    t.lt(270)

def draw_m(t):

    t.lt(90)
    t.fd(70)
    t.lt(270)
    diagonal(t, (30 / (math.cos(math.radians(30)))), 315)
    diagonal(t, (30 / (math.cos(math.radians(30)))), 45)
    t.lt(270)
    t.fd(70)
    t.lt(90)
    leave_at_origin(t)

bob = turtle.Turtle()  

draw_m(bob)
turtle.mainloop()