class Person:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"{self.name} {self.surname}"

    def __add__(self, other):
        return Person(self.name, other.surname)

class Group:
    def __init__(self, name, people):
        self.name = name
        self.people = people

    def __len__(self):
        return len(self.people)

    def __add__(self, other):
        new_name = f"{self.name} {other.name}"
        new_people = self.people + other.people
        return Group(new_name, new_people)

    def __str__(self):
        members = ", ".join(str(p) for p in self.people)
        return f"Group {self.name} with members {members}"

    def __getitem__(self, index):
        person = self.people[index]
        return f"Person {index}: {person}"



p1 = Person("John", "Smith")
p2 = Person("Lisa", "Taylor")
p3 = p1 + p2

print(p3)

group1 = Group("Alpha", [p1, p2])
group2 = Group("Beta", [p3])

print(len(group1))
print(group1)       

combined = group1 + group2
print(combined)
