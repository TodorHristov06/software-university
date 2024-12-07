allowed_bad_grades = int(input())

sum_grades = 0
number_solve_problems = 0
number_bad_grades = 0
last_task = ""
result = ""

while allowed_bad_grades > number_bad_grades:
    task_name = input()
    
    if task_name == "Enough":
        result = (f"Average score: {sum_grades / number_solve_problems:.2f}\n"
                  f"Number of problems: {number_solve_problems}\n"
                  f"Last problem: {last_task}")
        break
    
    grade = int(input())
    
    if grade <= 4:
        number_bad_grades += 1
    
    sum_grades += grade
    number_solve_problems += 1
    last_task = task_name
else:
    result = f"You need a break, {number_bad_grades} poor grades."

print(result)