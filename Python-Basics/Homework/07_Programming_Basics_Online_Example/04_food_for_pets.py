days = int(input())
total_food_quantity = float(input())

total_cookies = 0
total_food_eaten = 0
total_dog_food_eaten = 0
total_cat_food_eaten = 0

for day in range(1, days + 1):
    dog_food = int(input())
    cat_food = int(input())
    
    total_food_eaten += dog_food + cat_food
    
    if day % 3 == 0:
        total_cookies += (dog_food + cat_food) * 0.1
    
    total_dog_food_eaten += dog_food
    total_cat_food_eaten += cat_food

percent_cookies = round(total_cookies)
percent_food_eaten = (total_food_eaten / total_food_quantity) * 100
percent_food_eaten_dog = (total_dog_food_eaten / total_food_eaten) * 100
percent_food_eaten_cat = (total_cat_food_eaten / total_food_eaten) * 100

print(f"Total eaten biscuits: {percent_cookies}gr.")
print(f"{percent_food_eaten:.2f}% of the food has been eaten.")
print(f"{percent_food_eaten_dog:.2f}% eaten from the dog.")