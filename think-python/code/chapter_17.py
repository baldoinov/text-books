
from chapter_16 import int_to_time
# As an exercise, rewrite time_to_int (from Section 16.4) as a method.

class Time:
    """Represents the time of day.
    
    attributes: 
        hour: int 
        minute: int
        second: int 
    """

    def __init__(self, hour=0, minute=0, second=0):

        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self) -> None:
        return f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"
    
    def __add__(self, other):
        if isinstance(other, Time):
            return self.add_time
        else:
            return self.increment(other)
    
    def __radd__(self, other):
        return self.__add__(other)

    def increment(self, seconds: int):
        seconds += self.time_to_int()
        return int_to_time(seconds)

    def add_time(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)
    
    def time_to_int(self) -> int:
        """Transforms a Time object into a int."""
        seconds = (self.hour * 3600) + (self.minute * 60) + self.second
        return seconds

    def is_after(self, other) -> bool:
        """Takes two Time objects and returns True if t1 follows t2 chronologically."""
        return self.time_to_int(self) > self.time_to_int(other)

# As an exercise, write an init method for the Point class that takes x and y as optional parameters and assigns them to the corresponding attributes.
# As an exercise, write a str method for the Point class.
# As an exercise, write an add method for the Point class.
# As an exercise, write an add method for Points that works with either a Point object or a tuple:

class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f'({self.x}, {self.y})'

    def __add__(self, other):
        
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        else:
            return Point(self.x + other[0], self.y + other[1])
    
    def __radd__(self, other):
        return self.__add__(other)

if __name__ == '__main__':

    p = Point(2, 3)
    q = Point(3, 5)
    m = 5, 9
    
    print(p + q)
    print(type(p + q))

    print(p + m)
    print(type(p + m))