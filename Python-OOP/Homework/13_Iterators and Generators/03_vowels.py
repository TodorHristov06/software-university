class vowels:
    def __init__(self, text):
        self.text = text
        self.index = 0
        self.vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.text):
            current_char = self.text[self.index]
            self.index += 1
            if current_char in self.vowels:
                return current_char
        raise StopIteration()
