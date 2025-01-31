def get_absolute_values(numbers):
    return [abs(float(num)) for num in numbers]

number = input().split()
absolute_values = get_absolute_values(number)
print(absolute_values)
