number = int(input())
negative_numbers = []
positive_numbers = []
for _ in range(number):
    data = int(input())
    if data < 0:
        negative_numbers.append(data)
    else:
        positive_numbers.append(data)

print(f"{positive_numbers}\n{negative_numbers}\nCount of positives: {len(positive_numbers)}\nSum of negatives: {sum(negative_numbers)}")
