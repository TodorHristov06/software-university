class Integer:
    def __init__(self, value: int):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f"Integer({self.value})"

    @classmethod
    def from_float(cls, float_value):
        if not isinstance(float_value, float):
            return "value is not a float"
        return cls(int(float_value // 1))

    @classmethod
    def from_roman(cls, value: str):
        roman_numerals = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

        result = 0
        prev_value = 0

        for char in reversed(value.upper()):
            if char not in roman_numerals:
                raise ValueError("Invalid Roman numeral")
            current = roman_numerals[char]
            if current >= prev_value:
                result += current
            else:
                result -= current
            prev_value = current

        return cls(result)

    @classmethod
    def from_string(cls, value):
        if not isinstance(value, str):
            return "wrong type"
        try:
            int_value = int(value)
        except ValueError:
            return "wrong type"
        return cls(int_value)


first_num = Integer(10)
print(first_num.value)
second_num = Integer.from_roman("IV")
print(second_num.value)
print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))