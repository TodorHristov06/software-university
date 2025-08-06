def type_check(expected_type):
    def decorator(func):
        def wrapper(arg):
            if isinstance(arg, expected_type):
                return func(arg)
            return "Bad Type"
        return wrapper
    return decorator