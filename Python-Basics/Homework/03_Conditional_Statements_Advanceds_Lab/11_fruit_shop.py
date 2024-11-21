fruits_prices_workday = {
    "banana": 2.50,
    "apple": 1.20,
    "orange": 0.85,
    "grapefruit": 1.45,
    "kiwi": 2.70,
    "pineapple": 5.50,
    "grapes": 3.85
}

fruit_prices_weekend = {
    "banana": 2.70,
    "apple": 1.25,
    "orange": 0.90,
    "grapefruit": 1.60,
    "kiwi": 3.00,
    "pineapple": 5.60,
    "grapes": 4.20
}

fruit = input()
day = input()
quantity = float(input())

if day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:
    price = fruits_prices_workday.get(fruit)
elif day in ["Saturday", "Sunday"]:
    price = fruit_prices_weekend.get(fruit)
else:
    print("error")
    exit()  

if price is None:
    print("error")
else:
    total_price = round(price * quantity, 2)
    print(f"{total_price:.2f}")
