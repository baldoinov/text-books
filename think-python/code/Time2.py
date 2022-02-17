"""
Change the attributes of Time to be a single integer representing seconds since midnight. Then modify 
the methods (and the function int_to_time) to work with the new implementation. You should not have 
to modify the test code in main. When you are done, the output should be the same as before.
"""

class Time:
    """Represents the time of day.
    
    attributes: hour, minute, second 
    """

    def __init__(self, hour: int = 0, minute: int = 0, second: int = 0):

        self.second = second + (minute * 60) + (hour * 3600)

    def __str__(self) -> None:
        representation = int_to_time(self.second)
        return f"{representation.hour:02d}:{representation.minute:02d}:{representation.second:02d}"
    
    def __add__(self, other):
        if isinstance(other, Time):
            return self.add_time
        else:
            return self.increment(other)
    
    def __radd__(self, other):
        return self.__add__(other)

    def increment(self, seconds: int):
        seconds += self.second
        return int_to_time(seconds)

    def add_time(self, other):
        seconds = self.second + other.second
        return int_to_time(seconds)
    
    def time_to_int(self) -> int:
        """Transforms a Time object into a int."""
        seconds = (self.hour * 3600) + (self.minute * 60) + self.second
        return seconds

    def is_after(self, other) -> bool:
        """Takes two Time objects and returns True if t1 follows t2 chronologically."""
        return self.second > other.second


def int_to_time(s: int) -> Time:
    """Gets an int and tranforms it into a Time object"""

    t = Time()

    minutes, t.second = divmod(s, 60)
    t.hour, t.minute = divmod(minutes, 60)

    return t

if __name__ == '__main__':

    now = Time(9, 35, 45)
    print(now)  

    before = Time(8, 35, 45)
    print(before)

    print(now.is_after(before))
    
    print(before.increment(20)) #TODO: is not working
