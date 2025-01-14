number_of_orders = int(input())
total_price = 0
for i in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_count = int(input())

    if price_per_capsule < 0.01 or price_per_capsule > 1000:
        continue
    elif days < 1 or days > 31:
        continue
    elif capsules_count < 1 or capsules_count > 2000:
        continue

    price = price_per_capsule * days * capsules_count
    total_price += price
    print(f"The price for the coffee is: ${price:.2f}")
    
print(f"Total: ${total_price:.2f}")
