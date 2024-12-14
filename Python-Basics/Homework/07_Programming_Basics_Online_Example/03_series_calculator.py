Winter = {
    "Dubai": 45000,
    "Sofia": 17000,
    "London": 24000
}

Summer = {
    "Dubai": 40000,
    "Sofia": 12500,
    "London": 20250
}

film_budget = float(input())
destination = input()  
season = input()
days = int(input())

if season == "Winter":
    total_sum = Winter[destination] * days
elif season == "Summer":
    total_sum = Summer[destination] * days


if destination == "Dubai":
    total_sum -= total_sum * 0.30  
elif destination == "Sofia":
    total_sum += total_sum * 0.25  
    
difference = abs(film_budget - total_sum)

if film_budget >= total_sum:
    print(f"The budget for the movie is enough! We have {difference:.2f} leva left!")
else:
    print(f"The director needs {difference:.2f} leva more!")
