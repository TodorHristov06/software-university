while True:
    string = input()

    if string == "Welcome!":
        print("Welcome to Hogwarts.")
        break

    if string == "Voldemort":
        print(f"You must not speak of that name!")
        break

    if len(string) < 5:
        print(f"{string} goes to Gryffindor.")
    elif len(string) == 5:
        print(f"{string} goes to Slytherin.")
    elif len(string) == 6:
        print(f"{string} goes to Ravenclaw.")
    else:
        print(f"{string} goes to Hufflepuff.")
