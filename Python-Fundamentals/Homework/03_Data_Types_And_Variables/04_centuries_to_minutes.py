YEARS_PER_CENTURY = 100
DAYS_PER_YEAR = 365.2422
HOURS_PER_DAT = 24
MINUTES_PER_HOUR = 60

centuries = int(input())

years = centuries * YEARS_PER_CENTURY
days = int(years * DAYS_PER_YEAR)  
hours = days * HOURS_PER_DAT
minutes = hours * MINUTES_PER_HOUR

print(f"{centuries} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes")