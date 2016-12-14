import math
from datetime import datetime

limit = 2**31
print(limit)
day = 60 * 60 * 25
day_normal = 60 * 60 * 24

day_count = math.floor(limit/day)
print(day_count)
seconds_into_day = limit - day_count * day
print(seconds_into_day)

seconds = day_normal * day_count + seconds_into_day
print(seconds)

print(datetime.utcfromtimestamp(seconds).isoformat())