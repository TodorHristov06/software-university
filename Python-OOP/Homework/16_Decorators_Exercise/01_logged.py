def logged(func):
    def wrapper(*args, **kwargs):
        args_list = [repr(arg) for arg in args]
        kwargs_list = [f"{k}={v!r}" for k, v in kwargs.items()]
        all_args = ", ".join(args_list + kwargs_list)

        result = func(*args, **kwargs)
        log = f"you called {func.__name__}({all_args})\nit returned {result}"
        return log
    return wrapper
