def multiplication(n1, n2, n3):
    if n1 == 0 or n2 == 0 or n3 == 0:
        return "zero"
    
    negative_count = 0
    if n1 < 0:
        negative_count += 1
    if n2 < 0:
        negative_count += 1
    if n3 < 0:
        negative_count += 1
    
    if negative_count % 2 == 0:
        return "positive"
    else:
        return "negative"

n1 = int(input())
n2 = int(input())
n3 = int(input())

print(multiplication(n1, n2, n3))