PROTECTIVE_NYLON_PER_SQUARE_METER = 1.50
PAINT_PER_LITER = 14.50
THINNER_PER_LITER = 5.00
ADDITIONAL_NYLON_PER_SQUARE_METER = 2
ADDITIONAL_PAINT_PER_LITER = 0.10
BAGS = 0.40
PERCENT_WORKERS = 0.30

nylon_quantity = float(input()) 
paint_quantity = float(input()) 
thinner_quantity = float(input())
hours = int(input())

nylon_quantity += ADDITIONAL_NYLON_PER_SQUARE_METER
paint_quantity += paint_quantity * ADDITIONAL_PAINT_PER_LITER

MATERIAL_COST = (nylon_quantity * PROTECTIVE_NYLON_PER_SQUARE_METER + paint_quantity * PAINT_PER_LITER + thinner_quantity * THINNER_PER_LITER) + BAGS
WORKER_COST = hours * (MATERIAL_COST * PERCENT_WORKERS)

print(f"{MATERIAL_COST + WORKER_COST:.2f}")