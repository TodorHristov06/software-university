input_string = input()

indices = []

for i in range(len(input_string)):
    if input_string[i].isupper():
        indices.append(i)

print(indices)