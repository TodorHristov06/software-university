CHICKEN_MENU_PRICE = 10.35
FISH_MENU_PRICE = 12.40
VEGETARIAN_MENU_PRICE = 8.15
DELIVERY_PRICE = 2.50

chicken_menu_count = int(input())
fish_menu_count = int(input())
vegetarian_menu_count = int(input())

total_sum = (chicken_menu_count * CHICKEN_MENU_PRICE) + (fish_menu_count * FISH_MENU_PRICE) + (vegetarian_menu_count * VEGETARIAN_MENU_PRICE)
desert_price = total_sum * 0.20

total_sum += desert_price + DELIVERY_PRICE

print(f"{total_sum:.2f}")

