GRAM_PER_FAT = 9
GRAM_PER_PROTEIN = 4
GRAM_PER_CARBS = 4

fat_percent = int(input())
protein_percent = int(input())
carbs_percent = int(input())
total_calories = int(input())
water_percent = int(input())

fat_grams = (fat_percent / 100) * total_calories / GRAM_PER_FAT
protein_grams = (protein_percent / 100) * total_calories / GRAM_PER_PROTEIN
carbs_grams = (carbs_percent / 100) * total_calories / GRAM_PER_CARBS

total_food_weight = fat_grams + protein_grams + carbs_grams

calories_per_gram = total_calories / total_food_weight

remaining_calories = calories_per_gram * (100 - water_percent) / 100

print(f"{remaining_calories:.4f}")
