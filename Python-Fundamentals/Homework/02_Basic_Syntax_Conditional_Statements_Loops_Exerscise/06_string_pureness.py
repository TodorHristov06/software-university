COMMA = ','
PERIOD = '.'
UNDERSCORE = '_'

number = int(input())

for _ in range(number):
    string = input()

    if COMMA in string or PERIOD in string or UNDERSCORE in string:
        print(f"{string} is not pure!")
    else:
        print(f"{string} is pure.")