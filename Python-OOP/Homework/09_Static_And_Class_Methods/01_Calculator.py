class Calculator:

    @staticmethod
    def add(*args):
        return sum(args)

    @staticmethod
    def multiply(*args):
        result = 1
        for num in args:
            result *= num
        return result

    @staticmethod
    def divide(*args):
        if not args:
            return 0
        result = args[0]
        for num in args[1:]:
            if num == 0:
                raise ValueError("Cannot divide by zero.")
            result /= num
        return result

    @staticmethod
    def subtract(*args):
        if not args:
            return 0
        result = args[0]
        for num in args[1:]:
            result -= num
        return result
    
print(Calculator.add(1, 2, 3))         # 6
print(Calculator.multiply(2, 3, 4))    # 24
print(Calculator.divide(100, 2, 5))    # 10.0
print(Calculator.subtract(20, 5, 3))   # 12
