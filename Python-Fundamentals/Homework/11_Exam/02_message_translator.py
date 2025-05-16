import re

number_input = int(input())
for _ in range(number_input):
    message = input().strip()
    pattern = r'^!([A-Z][a-z]{2,})!:\[([A-Za-z]{8,})\]$'
    matches = re.fullmatch(pattern, message)
    if matches:
        command = matches.group(1)
        text = matches.group(2)
        ascii_values = [str(ord(char)) for char in text]
        print(f"{command}: {' '.join(ascii_values)}")
    else:
        print("The message is invalid")