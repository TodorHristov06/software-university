version = [int(digit) for digit in input().split(".")]
version[-1] += 1
for index in range(len(version) -1, -1, -1):
    if version[index] > 9:
        version[index] = 0
        version[index-1] += 1

print(".".join([str(digit) for digit in version]))
# version_input = input()
# n1 = int(version_input[0])
# n2 = int(version_input[2])
# n3 = int(version_input[4])

# if n3 < 9:
#     n3 += 1
# else:
#     n3 = 0
#     if n2 < 9:
#         n2 += 1
#     else:
#         n2 = 0
#         n1 += 1

# print(f"{n1}.{n2}.{n3}")