strawberries_price = float(input())  
bananas_quantity = float(input())  
oranges_quantity = float(input()) 
raspberries_quantity = float(input())  
strawberries_quantity = float(input()) 

raspberries_price = strawberries_price / 2
oranges_price = raspberries_price - (raspberries_price * 0.4)
bananas_price = raspberries_price - (raspberries_price * 0.8)

strawberries_total = strawberries_price * strawberries_quantity
bananas_total = bananas_price * bananas_quantity
oranges_total = oranges_price * oranges_quantity
raspberries_total = raspberries_price * raspberries_quantity

total_cost = strawberries_total + bananas_total + oranges_total + raspberries_total

print(f"{total_cost:.2f}")
