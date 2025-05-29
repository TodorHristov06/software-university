odd_set = set()
even_set = set()

for i in range(1, int(input()) + 1):
    curr_num = sum(ord(ch) for ch in input()) // i
    if curr_num % 2 == 0:
        even_set.add(curr_num)
    else:
        odd_set.add(curr_num)

if sum(odd_set) == sum(even_set):
    print(*odd_set.union(even_set), sep=", ")
elif sum(odd_set) > sum(even_set):
    print(*odd_set.difference(even_set), sep=", ")
else:
    print(*odd_set.symmetric_difference(even_set), sep=", ")