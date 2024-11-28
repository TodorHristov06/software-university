prices = {
    "Monday": 12,
    "Tuesday": 12,
    "Wednesday": 14,
    "Thursday": 14,
    "Friday": 12,
    "Saturday": 16,
    "Sunday": 16
}

day_of_week = input()

print(prices.get(day_of_week, "Invalid day"))
    

