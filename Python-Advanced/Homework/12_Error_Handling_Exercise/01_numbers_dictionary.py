numbers_dictionary = {}

line = input()
while line != "Search":
    number_as_string = line
    try:
        number = int(input())
        numbers_dictionary[number_as_string] = number
    except ValueError:
        print("The variable number must be an integer")
    line = input()

line = input()
while line != "Remove":
    searched = line
    if searched in numbers_dictionary:
        print(numbers_dictionary[searched])
    else:
        print("Number does not exist in dictionary")
    line = input()

line = input()
while line != "End":
    searched = line
    if searched in numbers_dictionary:
        del numbers_dictionary[searched]
    else:
        print("Number does not exist in dictionary")
    line = input()

print(numbers_dictionary)
