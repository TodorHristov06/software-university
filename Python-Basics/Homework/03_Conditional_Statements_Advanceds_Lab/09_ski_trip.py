ROOM_FOR_ONE_PERSON_PRICE = 18
APARTMENT_PRICE = 25
PRESIDENT_APARTMENT_PRICE = 35

APARTMENT_DISCOUNT_LESS_THAN_10 = 0.30
APARTMENT_DISCOUNT_10_15 = 0.35
APARTMENT_DISCOUNT_MORE_THAN_15 = 0.50

PRESIDENT_APARTMENT_DISCOUNT_LESS_THAN_10 = 0.10
PRESIDENT_APARTMENT_DISCOUNT_10_15 = 0.15
PRESIDENT_APARTMENT_DISCOUNT_MORE_THAN_15 = 0.20

POSITIVE_REVIEW_ADD = 0.25
NEGATIVE_REVIEW_SUB = 0.10

number_of_days = int(input())
type_of_room = input()
rating = input()

nights = number_of_days - 1 
price = 0

if type_of_room == "room for one person":
    price = nights * ROOM_FOR_ONE_PERSON_PRICE

elif type_of_room == "apartment":
    price = nights * APARTMENT_PRICE

    if nights < 10:
        price -= price * APARTMENT_DISCOUNT_LESS_THAN_10
    elif 10 <= nights <= 15:
        price -= price * APARTMENT_DISCOUNT_10_15
    elif nights > 15:
        price -= price * APARTMENT_DISCOUNT_MORE_THAN_15

elif type_of_room == "president apartment":
    price = nights * PRESIDENT_APARTMENT_PRICE

    if nights < 10:
        price -= price * PRESIDENT_APARTMENT_DISCOUNT_LESS_THAN_10
    elif 10 <= nights <= 15:
        price -= price * PRESIDENT_APARTMENT_DISCOUNT_10_15
    elif nights > 15:
        price -= price * PRESIDENT_APARTMENT_DISCOUNT_MORE_THAN_15

if rating == "positive":
    price += price * POSITIVE_REVIEW_ADD
elif rating == "negative":
    price -= price * NEGATIVE_REVIEW_SUB

print(f"{price:.2f}")
