card_input = input().split()
shuffles = int(input())

half = len(card_input) // 2

for _ in range(shuffles):
    first_half = card_input[:half]
    second_half = card_input[half:]
    card_input = []

    for index in range(len(first_half)):
        card_input.append(first_half[index])
        card_input.append(second_half[index])

print(card_input)