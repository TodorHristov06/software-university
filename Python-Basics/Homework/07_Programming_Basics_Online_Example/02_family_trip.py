DISCOUNT_OVER_SEVEN_NIGHTS = 0.05

budget = float(input())
nights = int(input())
price_per_night = float(input())
percent_additional_expenses = float(input()) / 100

if nights > 7:
    price_per_night -= price_per_night * DISCOUNT_OVER_SEVEN_NIGHTS
    
total_nights_cost = nights * price_per_night
additional_expenses = budget * percent_additional_expenses
total_cost = total_nights_cost + additional_expenses

if total_cost > budget:
    print(f"{total_cost - budget:.2f} leva needed.")
else:
    print(f"Ivanovi will be left with {budget - total_cost:.2f} leva after vacation.")