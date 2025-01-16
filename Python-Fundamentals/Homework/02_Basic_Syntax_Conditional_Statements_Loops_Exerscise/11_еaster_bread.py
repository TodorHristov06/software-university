budget = float(input())
price_per_kg_flour = float(input())

PRICE_PER_PACK_OF_EGGS = price_per_kg_flour * 0.75
PRICE_PER_LITER_MILK = price_per_kg_flour * 1.25

breads = 0
colored_eggs = 0

price_per_bread = price_per_kg_flour + PRICE_PER_PACK_OF_EGGS + PRICE_PER_LITER_MILK / 4

while budget >= price_per_bread:
    budget -= price_per_bread
    breads += 1
    colored_eggs += 3

    if breads % 3 == 0:
        colored_eggs -= breads - 2
    
print(f"You made {breads} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")