number = int(input())

if number < 2:
    print("False")
else:
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
    print(is_prime)