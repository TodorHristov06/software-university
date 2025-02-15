def positive_numbers(list_of_numbers: str) -> str:
    return ", ".join([number for number in list_of_numbers if int(number) >= 0])
def negative_numbers(list_of_numbers: str) -> str:
    return ", ".join([number for number in list_of_numbers if int(number) < 0])
def even_numbers(list_of_numbers: str) -> str:
    return ", ".join([number for number in list_of_numbers if int(number) % 2 == 0])
def odd_numbers(list_of_numbers: str) -> str:
    return ", ".join([number for number in list_of_numbers if int(number) % 2 != 0])

numbers = input().split(", ")
print(f"Positive: {positive_numbers(numbers)}")
print(f"Negative: {negative_numbers(numbers)}")
print(f"Even: {even_numbers(numbers)}")
print(f"Odd: {odd_numbers(numbers)}")


# numbers = [int(x) for x in input().split(", ")]
# print(f"Positive: {', '.join([str(positive) for positive in numbers if positive >= 0])}")
# print(f"Negative: {', '.join([str(negative) for negative in numbers if negative < 0])}")
# print(f"Even: {', '.join([str(even) for even in numbers if even % 2 == 0])}")
# print(f"Odd: {', '.join([str(odd) for odd in numbers if odd % 2 != 0])}")