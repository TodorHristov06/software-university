rooms = int(input())
total_free_chairs = 0
game_on = True

for room in range(1, rooms + 1):
    chairs_data = input().split()
    available_chairs = len(chairs_data[0])
    visitors = int(chairs_data[1])

    if available_chairs < visitors:
        needed_chairs = visitors - available_chairs
        print(f"{needed_chairs} more chairs needed in room {room}")
        game_on = False
    else:
        total_free_chairs += available_chairs - visitors

if game_on:
    print(f"Game On, {total_free_chairs} free chairs left")