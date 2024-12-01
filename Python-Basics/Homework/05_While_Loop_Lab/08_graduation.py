student_name = input()
grades_total = 0
years_counter = 0
failed_grades = 0

while years_counter < 12:
    annual_grade = float(input())
    if annual_grade < 4:
        failed_grades += 1
        if failed_grades == 2:
            print(f"{student_name} has been excluded at {years_counter + 1} grade")
            break
    else:
        years_counter += 1
        grades_total += annual_grade

if years_counter == 12:
    average = grades_total / 12
    print(f"{student_name} graduated. Average grade: {average:.2f}")