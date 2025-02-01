def even_numbers(number):
    return list(filter(lambda x: x % 2 == 0, number))

number = list(map(int, input().split()))

print(even_numbers(number))