import copy

# 1) As an exercise, write a function called print_time that takes a Time object 
# and prints it in the form hour:minute:second.

class Time:
    """Represents the time of day.
    
    attributes: 
        hour: int 
        minute: int
        second: int 
    """

def print_time(t: Time) -> None:
    """Takes a time object and print it in the form hour:minute:second"""

    print(f"{t.hour:02d}:{t.minute:02d}:{t.second:02d}")


# 2) Write a boolean function called is_after that takes two Time objects, t1 and t2, and 
# returns True if t1 follows t2 chronologically and False otherwise. 
# Challenge: don’t use an if statement.

def is_after(t1: Time, t2: Time) -> bool:
    """Takes two Time objects and returns True if t1 follows t2 chronologically."""

    t1_sum = t1.hour + t1.minute + t1.second
    t2_sum = t2.hour + t2.minute + t2.second

    return t1_sum > t2_sum

# As an exercise, write a “pure” version of increment that creates and returns a new Time 
# object rather than modifying the parameter.

def increment(t: Time, seconds: int) -> Time:
    """Takes a Time object and increments it with the given seconds.
    
    Returns a new Time object.
    """
    
    new_t = time_to_int(t) + seconds
    new_t = int_to_time(new_t)

    return new_t

def time_to_int(t: Time) -> int:
    """Transforms a Time object into a int."""

    seconds = (t.hour * 3600) + (t.minute * 60) + t.second
    return seconds


def int_to_time(s: int) -> Time:
    """Gets an int and tranforms it into a Time object"""

    t = Time()

    minutes, t.second = divmod(s, 60)
    t.hour, t.minute = divmod(minutes, 60)

    return t


if __name__ == '__main__':

    now = Time()
    now.hour, now.minute, now.second = 9, 35, 45

    print_time(now)  

    before = Time()
    before.hour, before.minute, before.second = 8, 35, 45

    print(is_after(now, before))
    
    print_time(increment(before, 20))