def print_max(number):
    return max(number)

def print_min(number):
    return min(number)

def print_sum(number):
   return sum(number)

number = list(map(int, input().split()))

print(f"The minimum number is {print_min(number)}")
print(f"The maximum number is {print_max(number)}")
print(f"The sum number is: {print_sum(number)}")