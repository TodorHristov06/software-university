phone_book = {}

while True:
    entry = input()
    if "-" in entry:
        name, number = entry.split("-")
        phone_book[name] = number
    else:
        n = int(entry)
        for _ in range(n):
            name = input()
            if name in phone_book:
                print(f"{name} -> {phone_book[name]}")
            else:
                print(f"Contact {name} does not exist.")
        break