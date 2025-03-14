products = {}

while True:
    command = input()
    if command == "buy":
        break
    
    name, price, quantity = command.split()
    price, quantity = float(price), int(quantity)
    
    if name in products:
        products[name]["quantity"] += quantity
        products[name]["price"] = price
    else:
        products[name] = {"price": price, "quantity": quantity}

for name, data in products.items():
    total_price = data["price"] * data["quantity"]
    print(f"{name} -> {total_price:.2f}")
