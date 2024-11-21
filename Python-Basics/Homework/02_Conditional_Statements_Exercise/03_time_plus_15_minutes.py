MINUTES_ADDED = 15
MINUTES_IN_HOUR = 60
HOURS_IN_DAY = 24

hour = int(input())
minutes = int(input())

minutes += MINUTES_ADDED

if minutes >= MINUTES_IN_HOUR:
    hour += 1
    minutes -= MINUTES_IN_HOUR

if hour >= HOURS_IN_DAY:
    hour = 0

print(f"{hour}:{minutes:02d}")