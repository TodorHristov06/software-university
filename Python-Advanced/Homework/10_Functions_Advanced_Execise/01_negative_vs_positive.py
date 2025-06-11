def calculate_sums(numbers):
    positive_sum = sum(n for n in numbers if n > 0)
    negative_sum = sum(n for n in numbers if n < 0)
    return positive_sum, negative_sum

def print_results(positive_sum, negative_sum):
    print(negative_sum)
    print(positive_sum)
    if abs(negative_sum) > positive_sum:
        print("The negatives are stronger than the positives")
    else:
        print("The positives are stronger than the negatives")


numbers = list(map(int, input().split()))
positive_sum, negative_sum = calculate_sums(numbers)
print_results(positive_sum, negative_sum)