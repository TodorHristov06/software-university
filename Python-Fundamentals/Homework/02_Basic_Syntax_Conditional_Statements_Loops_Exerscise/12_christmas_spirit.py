ORNAMENT_SET_PRICE = 2
TREE_SKIRT_PRICE = 5
TREE_GARLAND_PRICE = 3
TREE_LIGHTS_PRICE = 15

ORNAMENT_SET_POINTS = 5
TREE_SKIRT_POINTS = 3
TREE_GARLAND_POINTS = 10
TREE_LIGHTS_POINTS = 17

quantity_of_decorations = int(input())
days_until_christmas = int(input())

total_cost = 0
total_spirit = 0

for current_day in range(1, days_until_christmas + 1):
    if current_day % 11 == 0:
        quantity_of_decorations += 2
    if current_day % 2 == 0:
        total_cost += quantity_of_decorations * ORNAMENT_SET_PRICE
        total_spirit += ORNAMENT_SET_POINTS
    if current_day % 3 == 0:
        total_cost += quantity_of_decorations * (TREE_SKIRT_PRICE + TREE_GARLAND_PRICE)
        total_spirit += TREE_SKIRT_POINTS + TREE_GARLAND_POINTS
    if current_day % 5 == 0:
        total_cost += quantity_of_decorations * TREE_LIGHTS_PRICE
        total_spirit += TREE_LIGHTS_POINTS
        if current_day % 3 == 0:
            total_spirit += 30
    if current_day % 10 == 0:
        total_spirit -= 20
        total_cost += TREE_SKIRT_PRICE + TREE_GARLAND_PRICE + TREE_LIGHTS_PRICE
if days_until_christmas % 10 == 0:
    total_spirit -= 30

print(f"Total cost: {total_cost}")
print(f"Total spirit: {total_spirit}")
    