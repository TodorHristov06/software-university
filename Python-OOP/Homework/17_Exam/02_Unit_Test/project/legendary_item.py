class LegendaryItem:
    def __init__(self, identifier: str, power: int, durability: int, price: int):
        self.identifier = identifier
        self.power = power
        self.durability = durability
        self.price = price

    @property
    def identifier(self):
        return self.__identifier

    @identifier.setter
    def identifier(self, value):
        if not value.replace('-', '').isalnum():
            raise ValueError("Identifier can only contain letters, digits, or hyphens!")
        if len(value) < 4:
            raise ValueError("Identifier must be at least 4 characters long!")
        self.__identifier = value

    @property
    def power(self):
        return self.__power

    @power.setter
    def power(self, value):
        if value < 0:
            raise ValueError("Power must be a non-negative integer!")
        self.__power = value

    @property
    def durability(self):
        return self.__durability

    @durability.setter
    def durability(self, value):
        if not 1 <= value <= 100:
            raise ValueError("Durability must be between 1 and 100 inclusive!")
        self.__durability = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value == 0 or value % 10 != 0:
            raise ValueError("Price must be a multiple of 10 and not 0!")
        self.__price = value

    @property
    def is_precious(self) -> bool:
        return self.power >= 50

    def enhance(self) -> None:
        self.power *= 2
        self.price += 10
        self.durability = min(100, self.durability + 10)

    def evaluate(self, min_durability: int) -> str:
        if self.durability >= min_durability and self.is_precious:
            return f"{self.identifier} is eligible."
        return "Item not eligible."