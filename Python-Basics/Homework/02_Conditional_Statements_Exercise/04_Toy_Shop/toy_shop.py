PUZZLE = 2.60
DOLL = 3
TEDDY_BEAR = 4.10
MINION = 8.20
TRUCK =  2.00 

DISCOUNT = 0.25
RENT = 0.10

vacation_price = float(input())
puzzle_count = int(input())
doll_count = int(input())
teddy_bear_count = int(input())
minion_count = int(input())
truck_count = int(input())

toy_count = puzzle_count + doll_count + teddy_bear_count + minion_count + truck_count
total_sum = puzzle_count * PUZZLE + doll_count * DOLL + teddy_bear_count * TEDDY_BEAR + minion_count * MINION + truck_count * TRUCK

if toy_count >= 50:
    total_sum -= total_sum * DISCOUNT

rent = total_sum * RENT
total_sum -= rent

if total_sum >= vacation_price:
    print(f"Yes! {total_sum - vacation_price:.2f} lv left.")
    
else:
    print(f"Not enough money! {vacation_price - total_sum:.2f} lv needed.")