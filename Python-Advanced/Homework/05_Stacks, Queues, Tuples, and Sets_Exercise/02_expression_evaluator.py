import math

def evaluate_expression(expr):
    tokens = expr.split()
    stack = []

    for token in tokens:
        if token in '+-*/':
            result = stack[0]
            for num in stack[1:]:
                if token == '+':
                    result += num
                elif token == '-':
                    result -= num
                elif token == '*':
                    result *= num
                elif token == '/':
                    result = math.floor(result / num)
            stack = [result]
        else:
            stack.append(int(token))
    
    return stack[0]

expression = input()
print(evaluate_expression(expression))
