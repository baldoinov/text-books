"""
Write a function called mul_time that takes a Time object and a number and returns a new Time 
object that contains the product of the original Time and the number.

Then use mul_time to write a function that takes a Time object that represents the finishing 
time in a race, and a number that represents the distance, and returns a Time object that 
represents the average pace (time per mile).
"""

from chapter_16 import Time, time_to_int, int_to_time

def mul_time(t: Time, i: int):
    """Takes a Time object and an int and returns a new Time object that contains
    the product of the orginal and the number.
    """
    
    time_as_int = time_to_int(t) * i
    new_t = int_to_time(time_as_int)
    return new_t

def pace_calc(finish_t: Time, dist: float) -> float:
    """Takes a Time object representing the finishing time of a race and its 
    distance and returns the average pace.
    """

    pace = mul_time(finish_t, (1 / dist))
    return pace

if __name__ == '__main__':

    race = Time()
    race.hour, race.minute, race.second = 2, 0, 0

    race_dist = 2

    # print(pace_calc(race, race_dist))