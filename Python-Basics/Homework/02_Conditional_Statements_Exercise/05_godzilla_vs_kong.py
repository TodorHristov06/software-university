DECORATION = 0.10
CLOTHING_DISCOUNT = 0.10

film_budget = float(input())
number_extras = int(input())
price_for_clothing_per_extra = float(input())

decor = film_budget * DECORATION
clothing_price = number_extras * price_for_clothing_per_extra

if number_extras > 150:
    clothing_price -= clothing_price * CLOTHING_DISCOUNT

total_sum = decor + clothing_price

if total_sum > film_budget:
    print("Not enough money!")
    print(f"Wingard needs {total_sum - film_budget:.2f} leva more.")
    
else:
    print("Action!")
    print(f"Wingard starts filming with {film_budget - total_sum:.2f} leva left.")