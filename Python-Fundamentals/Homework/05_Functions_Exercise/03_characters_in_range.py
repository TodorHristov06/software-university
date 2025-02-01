def char_between(first: str ,last: str) -> str:
    return ' '.join(chr(char) for char in range(ord(first) + 1, ord(last)))

first = input()
last = input()

print(char_between(first, last))