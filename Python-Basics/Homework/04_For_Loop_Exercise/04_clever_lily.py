age = int(input())
price_for_washing_machine = float(input())
price_for_toy = int(input())

money_saved = 0  
toys_count = 0  
money_gift = 10

for birthday in range(1, age + 1):
    if birthday % 2 == 0:
        money_saved += money_gift
        money_gift += 10
        money_saved -= 1
    else:
        toys_count += 1

money_saved += toys_count * price_for_toy

if money_saved >= price_for_washing_machine:
    print(f"Yes! {money_saved - price_for_washing_machine:.2f}")
else:
    print(f"No! {price_for_washing_machine - money_saved:.2f}")