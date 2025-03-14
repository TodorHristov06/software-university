n = int(input())
students = {}

for _ in range(n):
    name = input()
    grade = float(input())
    
    if name not in students:
        students[name] = []
    
    students[name].append(grade)

filtered_students = {
    name: sum(grades) / len(grades)
    for name, grades in students.items()
    if sum(grades) / len(grades) >= 4.5
}

for name, avg_grade in filtered_students.items():
    print(f"{name} -> {avg_grade:.2f}")