DISCOUNT_CARD = 0.85

shirt_price = float(input())
target_sum = float(input())

shorts_price = shirt_price * 0.75
socks_price = shorts_price * 0.20   
shoes_price = (shirt_price + shorts_price) * 2

total_sum = (shirt_price + shorts_price + socks_price + shoes_price) * DISCOUNT_CARD

if total_sum >= target_sum:
    print(f"Yes, he will earn the world-cup replica ball!\nHis sum is {total_sum:.2f} lv.")
    
else:
    print(f"No, he will not earn the world-cup replica ball.\nHe needs {target_sum - total_sum:.2f} lv. more.")