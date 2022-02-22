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
    
    def __lt__(self, other) -> bool:
        if isinstance(other, Time):
            return int_to_time(self) < int_to_time(other)
        else:
            raise TypeError("Other is not a Time object.")

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


def int_to_time(s: int) -> Time:
    """Gets an int and tranforms it into a Time object"""

    t = Time()

    minutes, t.second = divmod(s, 60)
    t.hour, t.minute = divmod(minutes, 60)

    return t
