key = int(input())
lines = int(input())

message = ""

for _ in range(lines):
    char = input()
    message += chr(ord(char) + key)

print(message)