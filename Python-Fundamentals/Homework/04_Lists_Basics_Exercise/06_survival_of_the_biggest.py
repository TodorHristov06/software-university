string_input = input().split()
number_of_elements_to_remove = int(input())

list_of_numbers = []
sorted_list = []
for number in string_input:
    list_of_numbers.append(int(number))
    sorted_list.append(int(number))

sorted_list.sort(reverse=True)

for _ in range(number_of_elements_to_remove):
    sorted_list.pop()

final_answer = []
for number in list_of_numbers:
    if number in sorted_list:
        final_answer.append(str(number))

print(", ".join(final_answer))