number = int(input())
searched_word = input()
string = []
for _ in range(number):
    data = input()
    string.append(data)

print(string)
    
for i in range(len(string) - 1, -1, -1):
    if searched_word not in string[i]:
        string.pop(i)

print(string)
