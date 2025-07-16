from project.food import Food
from project.fruit import Fruit

food = Food("2025-10-10")
fruit = Fruit("tomato", "2025-10-09")

print(fruit.name)
print(food.expiration_date)