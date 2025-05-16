from collections import deque

quantity_of_water = int(input())
people = deque()

while True:
    command = input()
    if command == "Start":
        break
    people.append(command)

while True:
    command = input()

    if command == "End":
        print(f"{quantity_of_water} liters left")
        break

    if command.startswith("refill"):
        _, amount = command.split()
        quantity_of_water += int(amount)
    else:
        liters_requested = int(command)
        person = people.popleft()
        if quantity_of_water >= liters_requested:
            quantity_of_water -= liters_requested
            print(f"{person} got water")
        else:
            print(f"{person} must wait")