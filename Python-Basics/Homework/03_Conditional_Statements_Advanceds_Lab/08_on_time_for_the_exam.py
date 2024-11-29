hour_of_exam = int(input())
minute_of_exam = int(input())
hour_of_arrival = int(input())
minutes_of_arrival = int(input())

minute_of_exam = minute_of_exam + hour_of_exam * 60
minute_of_arrival = hour_of_arrival * 60 + minutes_of_arrival

time_diff = minute_of_exam - minute_of_arrival

if time_diff > 30:
    print("Early")
elif time_diff < 0:
    print("Late")
else:
    print("On time")
    
hours = abs(time_diff) // 60
minutes = abs(time_diff) % 60

result = ""

if hours > 0: 
    result += f"{hours}:{minutes:02d} hours"
elif minutes > 0:
    result += f"{minutes} minutes"
    
if time_diff > 0:
    result += " before the start"
else:
    result += " after the start"
    
print(result)


