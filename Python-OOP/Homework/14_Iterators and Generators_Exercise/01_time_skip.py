class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index >= self.count:
            raise StopIteration()
        result = self.current_index * self.step
        self.current_index += 1
        return result
