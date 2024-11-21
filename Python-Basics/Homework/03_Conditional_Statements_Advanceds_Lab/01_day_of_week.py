number = int(input())

day_of_week = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}

if number < 1 or number > 7:
    print("Error")
print(day_of_week[number])
