def is_palindrome(number: list) -> bool:
    for num in number:
        if str(num) == str(num)[::-1]:
            print("True")
        else:
            print("False")

number = list(map(int, input().split(', ')))

is_palindrome(number)