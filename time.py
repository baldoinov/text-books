import time


t = time.time()


minutes_epoch = int(t // 60)
hours_epoch = int(minutes_epoch // 60)
days = int(hours_epoch // 24)


today_midnight = days * 24 * 60 * 60
seconds_of_this_day = t - today_midnight
remaing_hours = int(seconds_of_this_day // 3600)
remaing_minutes = int((seconds_of_this_day - (remaing_hours * 3600)) // 60)
remaing_seconds = int((seconds_of_this_day - (remaing_hours * 3600 + remaing_minutes * 60)) // 60)


print(f'The number of days since the epoch is: {days}\n'
      f'The number of hours is: {hours_epoch}\n'
      f'The number os minutes is: {minutes_epoch}\n')


print(f'It is {remaing_hours}:{remaing_minutes}:{remaing_seconds} on {days} from epoch.')
