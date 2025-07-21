class Account:
    def __init__(self, id: int, balance: float, pin: int):
        self.__id = id 
        self.balance = balance
        self.__pin = pin

    def get_id(self, pin):
        if pin == self.__pin:
            return self.__id
        return "Wrong pin"

    def change_pin(self, old_pin, new_pin):
        if old_pin == self.__pin:
            self.__pin = new_pin
            return "Pin changed"
        return "Wrong pin"

acc = Account(12345, 1000.0, 4321)

print(acc.balance)        # 1000.0
print(acc.get_id(4321))   # 12345
print(acc.get_id(1111))   # Wrong pin

print(acc.change_pin(1111, 9999))  # Wrong pin
print(acc.change_pin(4321, 9999))  # Pin changed
print(acc.get_id(9999))             # 12345
