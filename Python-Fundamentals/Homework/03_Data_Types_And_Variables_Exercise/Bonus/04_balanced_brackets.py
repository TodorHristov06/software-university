number_of_lines = int(input())
is_balanced = True
last_opening = False

for _ in range(number_of_lines):
    line = input().strip()
    
    if line == "(":
        if last_opening:
            is_balanced = False
            break
        last_opening = True
    elif line == ")":
        if not last_opening:
            is_balanced = False
            break
        last_opening = False

if last_opening:
    is_balanced = False

if is_balanced:
    print("BALANCED")
else:
    print("UNBALANCED")
