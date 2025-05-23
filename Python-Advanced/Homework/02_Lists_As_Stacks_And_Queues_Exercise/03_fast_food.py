from collections import deque

food_quantity = int(input())
food_orders = deque(map(int, input().split()))

print(max(food_orders))

while food_orders and food_orders[0] <= food_quantity:
    food_quantity -= food_orders.popleft()

if food_orders:
    print("Orders left:", *food_orders)
else:
    print("Orders complete")