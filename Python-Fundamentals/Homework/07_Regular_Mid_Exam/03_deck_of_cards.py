list_of_cards = input().split(", ")
number_of_commands = int(input())

for _ in range(number_of_commands):
    command = input().split(", ")

    if command[0] == "Add":
        card = command[1]
        if card not in list_of_cards:
            list_of_cards.append(card)
            print("Card successfully added")
        else:
            print("Card is already in the deck")

    elif command[0] == "Remove":
        card = command[1]   
        if card in list_of_cards:
            list_of_cards.remove(card)
            print("Card successfully removed")
        else:
            print("Card not found")

    elif command[0] == "Remove At":
        index = int(command[1])
        if 0 <= index < len(list_of_cards):
            list_of_cards.pop(index)
            print("Card successfully removed")
        else:
            print("Index out of range")

    elif command[0] == "Insert":
        index = int(command[1])
        card = command[2]
        if 0 <= index < len(list_of_cards):
            if card not in list_of_cards:
                list_of_cards.insert(index, card)
                print("Card successfully added")
            else:
                print("Card is already added")
        else:
            print("Index out of range")

print(", ".join(list_of_cards))