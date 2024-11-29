PREMIERE_PRICE = 12.00
NORMAL_PRICE = 7.50
DISCOUNT_PRICE = 5.00

screening_type = input()
rows = int(input())
columns = int(input())

total_sum = 0

cinema_hall = rows * columns

if screening_type == "Premiere":
    total_sum = cinema_hall * PREMIERE_PRICE
elif screening_type == "Normal":
    total_sum = cinema_hall * NORMAL_PRICE
elif screening_type == "Discount":
    total_sum = cinema_hall * DISCOUNT_PRICE

print(f"{total_sum:.2f} leva")