class reverse_iter:
    def __init__(self, iterable):
        self.items = list(iterable)
        self.index = len(self.items)

    def __iter__(self):
        return self

    def __next__(self):
        self.index -= 1
        if self.index >= 0:
            return self.items[self.index]
        else:
            raise StopIteration()