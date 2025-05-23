stack = []
number = int(input())

functions = {
    "1": lambda x: stack.append(int(x)),
    "2": lambda: stack.pop() if stack else None,
    "3": lambda: print(max(stack)) if stack else None,
    "4": lambda: print(min(stack)) if stack else None,
}

for _ in range(number):
   query = input().split()
   functions[query[0]](*query[1:])

    

print(", ".join(map(str, reversed(stack))))




# stack = []
# number = int(input())

# for _ in range(number):
#     command = input().split()

#     if command[0] == '1':
#         stack.append(int(command[1]))
#     elif command[0] == '2' and stack:
#         stack.pop()
#     elif command[0] == '3' and stack:
#         print(max(stack))
#     elif command[0] == '4' and stack:
#         print(min(stack))

# print(", ".join(map(str, reversed(stack))))