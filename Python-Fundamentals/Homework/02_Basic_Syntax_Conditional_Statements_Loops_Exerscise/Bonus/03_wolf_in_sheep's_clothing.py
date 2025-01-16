animal_input = input().split(", ")

for i in range(len(animal_input)):
    if animal_input[i] == "wolf":
        if i == len(animal_input) - 1:
            print("Please go away and stop eating my sheep")
        else:
            print(f"Oi! Sheep number {len(animal_input) - i - 1}! You are about to be eaten by a wolf!")
        break