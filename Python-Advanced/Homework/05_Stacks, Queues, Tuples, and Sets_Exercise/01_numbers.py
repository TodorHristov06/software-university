first_seq = set(int(x) for x in input().split())
second_seq = set(int(x) for x in input().split())

n = int(input())

for _ in range(n):
    command = input().split()
    action = command[0]
    target = command[1]

    if action == "Add":
        numbers_to_add = set(int(x) for x in command[2:])
        if target == "First":
            first_seq.update(numbers_to_add)
        else:
            second_seq.update(numbers_to_add)

    elif action == "Remove":
        numbers_to_remove = set(int(x) for x in command[2:])
        if target == "First":
            first_seq.difference_update(numbers_to_remove)
        else:
            second_seq.difference_update(numbers_to_remove)

    elif action == "Check" and target == "Subset":
        if first_seq.issubset(second_seq) or second_seq.issubset(first_seq):
            print("True")
        else:
            print("False")

print(", ".join(str(x) for x in sorted(first_seq)))
print(", ".join(str(x) for x in sorted(second_seq)))
