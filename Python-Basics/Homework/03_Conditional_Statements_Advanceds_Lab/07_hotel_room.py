STUDIO_DISCOUNT_OVER_7_IN_MAY_AND_OCTOBER = 0.05
STUDIO_DISCOUNT_OVER_14_IN_MAY_AND_OCTOBER = 0.30
STUDIO_DISCOUNT_OVER_14_IN_JUNE_AND_SEPTEMBER = 0.20
APARTMENT_DISCOUNT_OVER_14 = 0.10

month = input()
nights = int(input())

price_for_studio = 0
price_for_apartment = 0

if month == "May" or month == "October":
    price_for_studio = 50 * nights
    price_for_apartment = 65 * nights
    if nights > 14:
        price_for_studio -= price_for_studio * STUDIO_DISCOUNT_OVER_14_IN_MAY_AND_OCTOBER
        price_for_apartment -= price_for_apartment * APARTMENT_DISCOUNT_OVER_14
    elif nights > 7:
        price_for_studio -= price_for_studio * STUDIO_DISCOUNT_OVER_7_IN_MAY_AND_OCTOBER

elif month == "June" or month == "September":
    price_for_studio = 75.20 * nights
    price_for_apartment = 68.70 * nights
    if nights > 14:
        price_for_studio -= price_for_studio * STUDIO_DISCOUNT_OVER_14_IN_JUNE_AND_SEPTEMBER
        price_for_apartment -= price_for_apartment * APARTMENT_DISCOUNT_OVER_14

elif month == "July" or month == "August":
    price_for_studio = 76 * nights
    price_for_apartment = 77 * nights
    if nights > 14:
        price_for_apartment -= price_for_apartment * APARTMENT_DISCOUNT_OVER_14

print(f"Apartment: {price_for_apartment:.2f} lv.")
print(f"Studio: {price_for_studio:.2f} lv.")
