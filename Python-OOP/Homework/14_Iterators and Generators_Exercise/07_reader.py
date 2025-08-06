def read_next(*args):
    for iterable in args:
        for element in iterable:
            yield element
