def cache(func):
    log = {}

    def wrapper(n):
        if n not in log:
            log[n] = func(n)
        return log[n]

    wrapper.log = log # type: ignore
    return wrapper
