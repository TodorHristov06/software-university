class custom_range:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
        self.current = start - 1

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        if self.current <= self.end:
            return self.current
        else:
            raise StopIteration()