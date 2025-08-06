class sequence_repeat:
    def __init__(self, sequence, length):
        self.sequence = sequence
        self.length = length
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= self.length:
            raise StopIteration()
        result = self.sequence[self.index % len(self.sequence)]
        self.index += 1
        return result