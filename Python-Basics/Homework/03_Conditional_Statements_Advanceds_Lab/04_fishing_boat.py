SPRING_RENT = 3000
SUMMER_RENT = 4200
AUTUMN_RENT = 4200
WINTER_RENT = 2600

SIX_DISCOUNT = 0.10
SEVEN_TO_TEN_DISCOUNT = 0.15
TWELVE_OR_MORE_DISCOUNT = 0.25

EVEN_NUMBER_OF_FISHERS_DISCOUNT = 0.05

group_budget = float(input())
season = input()
fisherman_count = int(input())

price = 0

if season == "Spring":
    price = SPRING_RENT
    if fisherman_count <= 6:
        price -= price * SIX_DISCOUNT
    elif 7 <= fisherman_count <= 11:
        price -= price * SEVEN_TO_TEN_DISCOUNT
    elif fisherman_count >= 12:
        price -= price * TWELVE_OR_MORE_DISCOUNT

elif season == "Summer":
    price = SUMMER_RENT
    if fisherman_count <= 6:
        price -= price * SIX_DISCOUNT
    elif 7 <= fisherman_count <= 11:
        price -= price * SEVEN_TO_TEN_DISCOUNT
    elif fisherman_count >= 12:
        price -= price * TWELVE_OR_MORE_DISCOUNT

elif season == "Autumn":
    price = AUTUMN_RENT
    if fisherman_count <= 6:
        price -= price * SIX_DISCOUNT
    elif 7 <= fisherman_count <= 11:
        price -= price * SEVEN_TO_TEN_DISCOUNT
    elif fisherman_count >= 12:
        price -= price * TWELVE_OR_MORE_DISCOUNT

elif season == "Winter":
    price = WINTER_RENT
    if fisherman_count <= 6:
        price -= price * SIX_DISCOUNT
    elif 7 <= fisherman_count <= 11:
        price -= price * SEVEN_TO_TEN_DISCOUNT
    elif fisherman_count >= 12:
        price -= price * TWELVE_OR_MORE_DISCOUNT
        
if fisherman_count % 2 == 0 and season != "Autumn":
    price -= price * EVEN_NUMBER_OF_FISHERS_DISCOUNT
    
difference = abs(group_budget - price)

if group_budget >= price:
    print(f"Yes! You have {difference:.2f} leva left.")
else:
    print(f"Not enough money! You need {difference:.2f} leva.")