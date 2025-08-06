class Equipment:
    _id_counter = 1

    def __init__(self, name: str):
        self.name = name
        self.id = Equipment._id_counter
        Equipment._id_counter += 1

    @staticmethod
    def get_next_id():
        return Equipment._id_counter

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"