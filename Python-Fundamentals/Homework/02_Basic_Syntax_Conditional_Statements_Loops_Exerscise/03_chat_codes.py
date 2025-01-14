number = int(input())

for i in range(number):
    input_number = int(input())

    if input_number == 88:
        print("Hello")
    elif input_number == 86:
        print("How are you?")
    elif input_number != 88 and input_number != 86 and input_number < 88:
        print("GREAT!")
    else:
        print("Bye.")