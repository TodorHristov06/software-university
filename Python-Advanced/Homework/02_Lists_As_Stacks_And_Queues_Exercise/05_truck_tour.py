from collections import deque

pumps_number = int(input())
pumps = deque()

for _ in range(pumps_number):
    curr_fuel, curr_distance = input().split()
    pumps.append({"fuel": int(curr_fuel), "distance": int(curr_distance)})

start_position = 0
stops = 0

while stops < pumps_number:
    fuel = 0
    for i in range(pumps_number):
        fuel += pumps[i]["fuel"]
        distance = pumps[i]["distance"]
        if fuel < distance:
            pumps.rotate(-1)
            start_position += 1
            stops = 0
            break
        fuel -= distance
        stops += 1

print(start_position)