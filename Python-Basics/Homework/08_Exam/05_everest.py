EVEREST = 8848
CURRENT_METERS = 5364
command = input()

days_for_hiking = 1
 
while command != "END":
    meters_to_hike = int(input())
 
    if command == "Yes":
        days_for_hiking += 1
        if days_for_hiking > 5:
            print("Failed!")
            print(f"{CURRENT_METERS}")
            break
        CURRENT_METERS += meters_to_hike
    else:
        CURRENT_METERS += meters_to_hike
        
    if CURRENT_METERS >= EVEREST:
        print(f"Goal reached for {days_for_hiking} days!")
        break
 
    command = input()
 
if command == "END":
    if CURRENT_METERS >= EVEREST:
        print(f"Goal reached for {days_for_hiking} days!")
    else:
        print("Failed!")
        print(f"{CURRENT_METERS}")