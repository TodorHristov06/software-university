WATER_RESISTANCE_DISTANCE = 15
WATER_RESISTANCE_DELAY = 12.5 

world_record_seconds = float(input())
distance_meters = float(input())
seconds_for_1_meter  = float(input())

time = distance_meters * seconds_for_1_meter
slow_time = distance_meters // WATER_RESISTANCE_DISTANCE * WATER_RESISTANCE_DELAY
total_time = time + slow_time

if total_time < world_record_seconds:
    print(f" Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {abs(total_time - world_record_seconds):.2f} seconds slower.")