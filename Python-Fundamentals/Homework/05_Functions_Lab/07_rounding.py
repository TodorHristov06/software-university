def rounded(number):
    return list(map(lambda num: round(float(num)), number))

number = input().split()
print(rounded(number))