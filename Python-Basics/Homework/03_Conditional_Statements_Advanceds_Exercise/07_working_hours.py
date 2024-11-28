hours = int(input())
days_of_week = input()

if (days_of_week == "Monday" or days_of_week == "Tuesday" or days_of_week == "Wednesday" or days_of_week == "Thursday" or days_of_week == "Friday" or days_of_week == "Saturday"):
    if (hours >= 10 and hours <= 18):
        print("open")
    else:
        print("closed")
else:
    print("closed")