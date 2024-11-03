PRICE_PACKAGE_PENS = 5.80
PRICE_PACKAGE_MARKERS = 7.20
PRICE_PER_LITER_PREPARATION = 1.20

pens_count = int(input())
markers_count = int(input())
liters_of_preparation = float(input())
percentage_discount = int(input()) / 100

total_sum = pens_count * PRICE_PACKAGE_PENS + markers_count * PRICE_PACKAGE_MARKERS + liters_of_preparation * PRICE_PER_LITER_PREPARATION
total_sum -= total_sum * percentage_discount 

print(total_sum)