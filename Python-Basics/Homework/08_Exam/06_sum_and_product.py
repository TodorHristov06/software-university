n = int(input())

for a in range(1, 10):
    for b in range(9, a - 1, -1):
        for c in range(0, 10):
            for d in range(9, c - 1, -1):
                sum_digits = a + b + c + d
                product_digits = a * b * c * d

                if sum_digits == product_digits and n % 10 == 5:
                    print(f"{a}{b}{c}{d}")
                    exit()

                if product_digits // sum_digits == 3 and n % 3 == 0:
                    print(f"{d}{c}{b}{a}")
                    exit() 

print("Nothing found")
