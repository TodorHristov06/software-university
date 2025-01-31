current_year = int(input())

next_year = current_year + 1
while True:
    year_str = str(next_year)
    
    if len(year_str) == len(set(year_str)):
        break 

    next_year += 1

print(next_year)