hour = int(input())
minutes = int(input())

minutes += 15

if minutes >= 60:
    hour += 1
    minutes -= 60

if hour >= 24:
    hour = 0

print(f"{hour}:{minutes:02d}")