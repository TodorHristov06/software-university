def operate(operator, *args):
    if operator == "+":
        result = 0
        for num in args:
            result += num
    elif operator == "-":
        result = args[0]
        for num in args[1:]:
            result -= num
    elif operator == "*":
        result = 1
        for num in args:
            result *= num
    elif operator == "/":
        result = args[0]
        for num in args[1:]:
            result /= num
    else:
        return "Invalid operator"
    return result
