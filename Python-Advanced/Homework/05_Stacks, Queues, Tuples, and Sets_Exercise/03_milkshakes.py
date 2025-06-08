from collections import deque

def make_milkshakes(chocolates, milk_cups):
    chocolates = list(chocolates)
    milk_cups = deque(milk_cups)
    milkshakes = 0

    while chocolates and milk_cups and milkshakes < 5:
        while chocolates and chocolates[-1] <= 0:
            chocolates.pop()
        while milk_cups and milk_cups[0] <= 0:
            milk_cups.popleft()

        if not chocolates or not milk_cups:
            break

        current_chocolate = chocolates[-1]
        current_milk = milk_cups[0]

        if current_chocolate == current_milk:
            chocolates.pop()
            milk_cups.popleft()
            milkshakes += 1
        else:
            milk_cups.append(milk_cups.popleft())
            chocolates[-1] -= 5

    if milkshakes == 5:
        print("Great! You made all the chocolate milkshakes needed!")
    else:
        print("Not enough milkshakes.")

    if chocolates:
        print("Chocolate:", ", ".join(map(str, chocolates)))
    else:
        print("Chocolate: empty")

    if milk_cups:
        print("Milk:", ", ".join(map(str, milk_cups)))
    else:
        print("Milk: empty")

chocolates_input = input().split(", ")
milk_input = input().split(", ")

chocolates = list(map(int, chocolates_input))
milk = list(map(int, milk_input))

make_milkshakes(chocolates, milk)
