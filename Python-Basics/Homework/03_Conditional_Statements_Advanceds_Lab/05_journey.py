BUDGET_BG_LIMIT = 100
BUDGET_BALKAN_LIMIT = 1000

BG_SUMMER_PERCENTAGE = 0.30
BG_WINTER_PERCENTAGE = 0.70
BALKAN_SUMMER_PERCENTAGE = 0.40
BALKAN_WINTER_PERCENTAGE = 0.80

EUROPE_PERCENT = 0.90


budget = float(input())
season = input()

destination = ''
type_of_journey = ''
spent_sum = 0

if season == 'summer':
    if budget <= BUDGET_BG_LIMIT:
        spent_sum = budget * BG_SUMMER_PERCENTAGE
        type_of_journey = 'Camp'
        destination = 'Bulgaria'
    elif BUDGET_BG_LIMIT < budget <= BUDGET_BALKAN_LIMIT:
        spent_sum = budget * BALKAN_SUMMER_PERCENTAGE
        type_of_journey = 'Camp'
        destination = 'Balkans'
    else:
        spent_sum = budget * EUROPE_PERCENT
        type_of_journey = 'Hotel'
        destination = 'Europe'

elif season == 'winter':
    if budget <= BUDGET_BG_LIMIT:
        spent_sum = budget * BG_WINTER_PERCENTAGE
        type_of_journey = 'Hotel'
        destination = 'Bulgaria'
    elif BUDGET_BG_LIMIT < budget <= BUDGET_BALKAN_LIMIT:
        spent_sum = budget * BALKAN_WINTER_PERCENTAGE
        type_of_journey = 'Hotel'
        destination = 'Balkans'
    else:
        spent_sum = budget * EUROPE_PERCENT
        type_of_journey = 'Hotel'
        destination = 'Europe'

print(f'Somewhere in {destination}')
print(f'{type_of_journey} - {spent_sum:.2f}')