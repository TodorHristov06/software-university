temperature = int(input())
time_of_day = input()

outfit = ""
shoes = ""

if time_of_day == "Morning":
    if 10 <= temperature <= 18:
        outfit, shoes = "Sweatshirt", "Sneakers"
    elif 18 < temperature <= 24:
        outfit, shoes = "Shirt", "Moccasins"
    elif temperature >= 25:
        outfit, shoes = "T-Shirt", "Sandals"
elif time_of_day == "Afternoon":
    if 10 <= temperature <= 18:
        outfit, shoes = "Shirt", "Moccasins"
    elif 18 < temperature <= 24:
        outfit, shoes = "T-Shirt", "Sandals"
    elif temperature >= 25:
        outfit, shoes = "Swim Suit", "Barefoot"
elif time_of_day == "Evening":
    outfit, shoes = "Shirt", "Moccasins"
        
print(f"It's {temperature} degrees, get your {outfit} and {shoes}.")