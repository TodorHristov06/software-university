page_count = int(input())
page_per_hour = int(input())
days = int(input())

total_hours_per_day = (page_count / page_per_hour) / days

print(int(total_hours_per_day))