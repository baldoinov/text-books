import turtle

def koch_curve(t, lenght):
    
    if lenght < 10:
        t.fd(lenght)
        return
    
    m = lenght / 3 

    koch_curve(t, m)
    t.lt(60)
    koch_curve(t, m)
    t.rt(120)
    koch_curve(t, m)
    t.lt(60)
    koch_curve(t, m)


def snowflake(t, lenght, n):

    external_angle = 360 / n

    for i in range(n):
        koch_curve(t, lenght)
        t.rt(external_angle)



bob = turtle.Turtle()
snowflake(bob, 200, 8)
turtle.mainloop()