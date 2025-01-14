LOWER_CASE_EVENTS = ["coding", "dog", "cat", "movie"]
UPPER_CASE_EVENTS = ["CODING", "DOG", "CAT", "MOVIE"]
coffee_counter = 0

while True:
    current_string = input()
    if current_string == "END":
        break
    if current_string in LOWER_CASE_EVENTS:
        coffee_counter += 1
    elif current_string in UPPER_CASE_EVENTS:
        coffee_counter += 2
    
    if coffee_counter > 5:
        print("You need extra sleep")
        break

if coffee_counter <= 5:
    print(coffee_counter)