items_with_prices = input().split("|")
budget = float(input())

bought_items = []
profit = 0

for item in items_with_prices:
    type_of_item, price = item.split("->")
    price = float(price)

    if type_of_item == "Clothes" and price > 50:
        continue
    elif type_of_item == "Shoes" and price > 35:
        continue
    elif type_of_item == "Accessories" and price > 20.50:
        continue

    if budget >= price:
        budget -= price
        new_price = price * 1.40
        bought_items.append(new_price)
        profit += new_price - price

budget += sum(bought_items)

print(" ".join(f"{price:.2f}" for price in bought_items))
print(f"Profit: {profit:.2f}")

if budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
