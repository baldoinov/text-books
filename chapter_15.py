
import copy

# 1º) As an exercise, write a function called distance_between_points that takes two 
# Points as arguments and returns the distance between them.

class Point:
    """Represents a point in 2-D space."""
    pass

def distance_between_points(a, b):

   x_square = abs(a.x - b.x) ** 2
   y_square = abs(a.y - b.y) ** 2
   distance = (x_square + y_square) ** (1/2)

   return distance

# 2º) As an exercise, write a function named move_rectangle that takes a Rectangle and two 
# numbers named dx and dy. It should change the location of the rectangle by adding dx 
# to the x coordinate of corner and adding dy to the y coordinate of corner.

class Rectangle:
    """Represents a rectangle.
    
    attributes: width, height, corner.

    obs: corner is a Point object
    """
    pass

def move_rectangle(rect, dx, dy):
    
    rect.corner.x += dx
    rect.corner.y += dy

# 3º) As an exercise, write a version of move_rectangle that creates and returns a new Rectangle 
# instead of modifying the old one.

def new_move_rectangle(rect, dx, dy):

    n_rect = copy.deepcopy(rect)
    
    rect.corner.x += dx
    rect.corner.y += dy

    return n_rect
    
if __name__ == '__main__':
    
    # 1º)
    # a = Point()
    # b = Point()
    # a.x, a.y = 4, 3
    # b.x, b.y = 8, 9
    # print(distance_between_points(a, b))

    # 2º)
    rect = Rectangle()
    rect.width, rect.height, rect.corner = 100, 200, Point()
    rect.corner.x, rect.corner.y = 0, 0
    move_rectangle(rect, dx=10, dy=20)
    print(f"The new location is {rect.corner.x, rect.corner.y}")
    


    pass