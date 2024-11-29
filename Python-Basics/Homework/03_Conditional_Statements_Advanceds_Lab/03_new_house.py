ROSES_PRICE = 5
DAHLIAS_PRICE = 3.80
TULIPS_PRICE = 2.80
NARCISSUS_PRICE = 3
GLADIOLUS_PRICE = 2.50

ROSES_DISCOUNT = 0.1
DAHLIAS_DISCOUNT = 0.15
TULIPS_DISCOUNT = 0.15
NARCISSUS_DISCOUNT = 0.15
GLADIOLUS_DISCOUNT = 0.20

flower_type = input()
number_of_flowers = int(input())
budget = int(input())

price = 0

if flower_type == "Roses":
    price = ROSES_PRICE * number_of_flowers
    if number_of_flowers > 80:
        price -= price * ROSES_DISCOUNT
elif flower_type == "Dahlias":
    price = DAHLIAS_PRICE * number_of_flowers
    if number_of_flowers > 90:
        price -= price * DAHLIAS_DISCOUNT
elif flower_type == "Tulips":
    price = TULIPS_PRICE * number_of_flowers
    if number_of_flowers > 80:
        price -= price * TULIPS_DISCOUNT
elif flower_type == "Narcissus":
    price = NARCISSUS_PRICE * number_of_flowers
    if number_of_flowers < 120: 
        price += price * NARCISSUS_DISCOUNT
elif flower_type == "Gladiolus":
    price = GLADIOLUS_PRICE * number_of_flowers
    if number_of_flowers < 80:
        price += price * GLADIOLUS_DISCOUNT

difference = abs(budget - price)

if budget >= price:
    print(f"Hey, you have a great garden with {number_of_flowers} {flower_type} and {difference:.2f} leva left.")
else:
    print(f"Not enough money, you need {difference:.2f} leva more.")