students = int(input())

group_1 = 0 #above 5
group_2 = 0 #between 4 and 4.99
group_3 = 0 #between 3 and 3.99
group_4 = 0 #lower than 3
average = 0

for i in range(students):
    grade = float(input())
    average += grade
    if grade >= 5:
        group_1 += 1
    elif 4 <= grade <= 4.99:
        group_2 += 1
    elif 3 <= grade <= 3.99:
        group_3 += 1
    else:
        group_4 += 1

print(f"Top students: {group_1 / students * 100:.2f}%")
print(f"Between 4.00 and 4.99: {group_2 / students * 100:.2f}%")
print(f"Between 3.00 and 3.99: {group_3 / students * 100:.2f}%")
print(f"Fail: {group_4 / students * 100:.2f}%")
print(f"Average: {average / students:.2f}")