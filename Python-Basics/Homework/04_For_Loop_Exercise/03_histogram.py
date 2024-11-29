number = int(input())

p1 = 0 #<200
p2 = 0 #200-399
p3 = 0 #400-599
p4 = 0 #600-799
p5 = 0 #>800

for _ in range(number):
    input_number = input()
    
    if int(input_number) < 200:
        p1 += 1
    elif 200 <= int(input_number) < 400:
        p2 += 1
    elif 400 <= int(input_number) < 600:
        p3 += 1
    elif 600 <= int(input_number) < 800:
        p4 += 1
    else:
        p5 += 1

print(f"{p1 / number:.2%}")
print(f"{p2 / number:.2%}")
print(f"{p3 / number:.2%}")
print(f"{p4 / number:.2%}")
print(f"{p5 / number:.2%}")