input_string = list(map(int, input().split(", ")))

zeros = input_string.count("0")
for i in range(zeros):
    input_string.remove("0")
    input_string.append("0")

for i in range(len(input_string)):
    input_string[i] = int(input_string[i])
    
print(input_string) 