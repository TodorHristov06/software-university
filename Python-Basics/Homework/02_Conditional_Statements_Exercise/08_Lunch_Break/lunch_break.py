from math import ceil


LUNCH_TIME = 0.125
RELAX_TIME = 0.25

series_name = input()
episode_time = int(input())
rest_time = int(input())

lunch = rest_time * LUNCH_TIME
relax = rest_time * RELAX_TIME
total_time = rest_time - lunch - relax

if total_time >= episode_time:
    print(f"You have enough time to watch {series_name} and left with {ceil(total_time - episode_time)} minutes free time.")
else:
    print(f"You don't have enough time to watch {series_name}, you need {ceil(abs(episode_time - total_time))} more minutes.")