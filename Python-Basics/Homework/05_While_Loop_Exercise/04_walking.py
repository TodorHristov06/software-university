GOAL = 10000  

steps = 0

while True:
    command = input()

    if command == "Going home":
        steps_to_home = int(input())
        steps += steps_to_home
        break

    steps += int(command)
    if steps >= GOAL:
        print(f"Goal reached! Good job!\n{steps - GOAL} steps over the goal!")
        break

if steps < GOAL:
    print(f"{GOAL - steps} more steps to reach goal.")
elif steps >= GOAL and command == "Going home":
    print(f"Goal reached! Good job!\n{steps - GOAL} steps over the goal!")
