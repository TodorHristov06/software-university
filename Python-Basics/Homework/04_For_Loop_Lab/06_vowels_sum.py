a = 1
e = 2
i = 3
o = 4
u = 5

input_text = input()
vowels_sum = 0

for letter in input_text:
    if letter == "a":
        vowels_sum += a
    elif letter == "e":
        vowels_sum += e
    elif letter == "i":
        vowels_sum += i
    elif letter == "o":
        vowels_sum += o
    elif letter == "u":
        vowels_sum += u

print(vowels_sum)