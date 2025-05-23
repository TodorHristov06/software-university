text = list(input().split())
stack = []

for _ in range(len(text)):
    stack.append(text.pop())
print(" ".join(stack))