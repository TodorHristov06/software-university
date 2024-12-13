n = int(input())

total_average = 0
presentations_count = 0

while True:
    presentation_name = input()
    
    if presentation_name == "Finish":
        break
    
    current_total = 0

    for _ in range(n):
        grade = float(input())
        current_total += grade
        
    current_average = current_total / n
    print(f"{presentation_name} - {current_average:.2f}.")
    

    total_average += current_average
    presentations_count += 1


final_assessment = total_average / presentations_count
print(f"Student's final assessment is {final_assessment:.2f}.")
