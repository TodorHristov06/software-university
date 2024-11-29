number_of_groups = int(input())

musala_count = 0
monblan_count = 0
kilimanjaro_count = 0
k2_count = 0
everest_count = 0

for _ in range(number_of_groups):
    group_size = int(input())
    
    if group_size <= 5:
        musala_count += group_size
    elif 6 <= group_size <= 12:
        monblan_count += group_size
    elif 13 <= group_size <= 25:
        kilimanjaro_count += group_size
    elif 26 <= group_size <= 40:
        k2_count += group_size
    else:
        everest_count += group_size

total_count = musala_count + monblan_count + kilimanjaro_count + k2_count + everest_count

print(f"{musala_count / total_count:.2%}")
print(f"{monblan_count / total_count:.2%}")
print(f"{kilimanjaro_count / total_count:.2%}")
print(f"{k2_count / total_count:.2%}")
print(f"{everest_count / total_count:.2%}")

