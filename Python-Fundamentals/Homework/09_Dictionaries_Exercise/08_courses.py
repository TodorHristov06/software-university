courses = {}

while True:
    command = input()
    if command == "end":
        break
    
    course_name, student_name = command.split(" : ")
    
    if course_name not in courses:
        courses[course_name] = []
    
    courses[course_name].append(student_name)

for course, students in courses.items():
    print(f"{course}: {len(students)}")
    for student in students:
        print(f"-- {student}")
