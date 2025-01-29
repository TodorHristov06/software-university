events = input().split("|")

energy = 100
coins = 100

for event in events:
    event_name, value = event.split("-")
    value = int(value)

    if event_name == "rest":
        gained_energy = min(value, 100 - energy)
        energy += gained_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")
    
    elif event_name == "order":
        if energy >= 30:
            energy -= 30
            coins += value
            print(f"You earned {value} coins.")
        else:
            energy += 50
            print("You had to rest!")
    
    else:
        if coins >= value:
            coins -= value
            print(f"You bought {event_name}.")
        else:
            print(f"Closed! Cannot afford {event_name}.")
            break
else:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")