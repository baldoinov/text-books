"""
Write a definition for a class named Circle with attributes center and radius, where center is a 
Point object and radius is a number. 

Instantiate a Circle object that represents a circle with its center at (150, 100) and radius 75.

Write a function named point_in_circle that takes a Circle and a Point and returns True if the 
Point lies in or on the boundary ofthe circle.

Write a function named rect_in_circle that takes a Circle and a Rectangle and returns True if 
the Rectangle lies entirely in or on the boundary ofthe circle.

Write a function named rect_circle_overlap that takes a Circle and a Rectangle and returns True 
if any of the corners of the Rectangle fall inside the circle. Or as a more challenging version, 
return True if any part of the Rectangle falls inside the circle.
"""

from chapter_15 import distance_between_points

class Point:
    """Represents a point in 2-D space.
    
    attributes: x, y
    """

class Rectangle:
    """Represents a rectangle.
    
    attributes: width, height, corner.

    obs: corner is a Point object that specifies the lower-left corner
    """

class Circle:
    """Represents a circle.
    
    attributes: center (Point object), radius    
    """


def point_in_circle(c: Circle, p: Point) -> bool:
    """Takes a Circle and a Point and returns True if the Point lies in or
    on the boundary of the circle.
    """

    distance = distance_between_points(c.center, p)

    if distance <= c.radius:
        return True
    else:
        return False


def rect_in_circle(c: Circle, r: Rectangle) -> bool:
    """Takes a circle and a rectangles and returns True if the rectangle lies
    entirely in or on the boundary of the circle.
    """
    diagonal = rect_diagonal(r)

    if (diagonal / 2) > c.radius:
        return False
    
    upper_right = Point()
    upper_right.x, upper_right.y = (r.corner.x, r.corner.y + r.height)

    upper_left = Point()
    upper_left.x, upper_left.y = (r.corner.x + r.width, r.corner.y + r.height)

    lower_right = Point()
    lower_right.x, lower_right.y = (r.corner.x + r.width, r.corner.y)

    corners = [upper_right, upper_left, lower_right, r.corner]
    
    for i in corners:

        if point_in_circle(c, i) == False:
            return False
    
    return True


def rect_diagonal(r: Rectangle) -> float:
    """Takes a rectangle and calculates its diagonal."""

    sum_squares = (r.width ** 2) + (r.height ** 2)
    diag = sum_squares ** (1/2)

    return diag


def rect_circle_overlap(c: Circle, r: Rectangle) -> bool:
    """Takes a rectangle and a circle and checks if any corner of the Rectangle 
    falls inside the circle."""
    
    upper_right = Point()
    upper_right.x, upper_right.y = (r.corner.x, r.corner.y + r.height)

    upper_left = Point()
    upper_left.x, upper_left.y = (r.corner.x + r.width, r.corner.y + r.height)

    lower_right = Point()
    lower_right.x, lower_right.y = (r.corner.x + r.width, r.corner.y)

    corners = [upper_right, upper_left, lower_right, r.corner]
    
    for i in corners:

        if point_in_circle(c, i):
            return True
    
    return False


if __name__ == '__main__':
    
    circle = Circle()
    circle.radius, circle.center = 75, Point()
    circle.center.x, circle.center.y = 150, 100

    point = Point()
    point.x, point.y = 125, 125

    print(f"O ponto está dentro do circulo? {point_in_circle(circle, point)}")

    ###

    rect = Rectangle()
    rect.width, rect.height, rect.corner = 14, 10, Point()
    rect.corner.x, rect.corner.y = 100, 80

    print(f"O retângulo está dentro do circulo? {rect_in_circle(circle, rect)}")

