WIN_POINTS = 2000
FINAL_POINTS = 1200
SEMI_FINAL_POINTS = 720

tournaments_count = int(input())
start_points = int(input())

points = 0
win_count = 0

for _ in range(tournaments_count):
    result = input()

    if result == "W":
        win_count += 1
        points += WIN_POINTS
        
    elif result == "F":
        points += FINAL_POINTS
        
    elif result == "SF":
        points += SEMI_FINAL_POINTS

print(f"Final points: {points + start_points}")
print(f"Average points: {points // tournaments_count}")
print(f"{win_count / tournaments_count:.2%}")