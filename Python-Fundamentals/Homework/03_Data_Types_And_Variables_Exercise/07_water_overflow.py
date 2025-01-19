WATER_TANK_CAPACITY = 255

number_of_lines = int(input())
total_liters = 0

for _ in range(number_of_lines):
    liters = int(input())
    if total_liters + liters > WATER_TANK_CAPACITY:
        print("Insufficient capacity!")
    else:
        total_liters += liters
print(total_liters)