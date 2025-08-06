def even_parameters(func):
    def wrapper(*args, **kwargs):
        all_args = list(args) + list(kwargs.values())

        if all(isinstance(x, int) and x % 2 == 0 for x in all_args):
            return func(*args, **kwargs)
        return "Please use only even numbers!"
    return wrapper
