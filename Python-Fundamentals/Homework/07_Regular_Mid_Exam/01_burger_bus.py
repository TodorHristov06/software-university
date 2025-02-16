number_of_cities = int(input())
total_profit = 0

for city in range(1, number_of_cities + 1):
    city_name = input()
    owner_income = float(input())
    owner_expense = float(input())

    if city % 3 == 0 and city % 5 != 0:
        owner_expense *= 1.5

    if city % 5 == 0:
        owner_income *= 0.9

    profit = owner_income - owner_expense
    total_profit += profit

    print(f"In {city_name} Burger Bus earned {profit:.2f} leva.")

print(f"Burger Bus total profit: {total_profit:.2f} leva.")