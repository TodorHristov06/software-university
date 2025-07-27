from project.lion import Lion
from project.tiger import Tiger
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.caretaker import Caretaker
from project.vet import Vet

class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price: int):
        if len(self.animals) >= self.__animal_capacity:
            return "Not enough space for animal"
        if self.__budget < price:
            return "Not enough budget"
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        if len(self.workers) >= self.__workers_capacity:
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name: str):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salaries = sum(w.salary for w in self.workers)
        if self.__budget >= total_salaries:
            self.__budget -= total_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_care_cost = sum(a.get_needs() for a in self.animals)
        if self.__budget >= total_care_cost:
            self.__budget -= total_care_cost
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int):
        self.__budget += amount

    def animals_status(self):
        lions = [a for a in self.animals if isinstance(a, Lion)]
        tigers = [a for a in self.animals if isinstance(a, Tiger)]
        cheetahs = [a for a in self.animals if isinstance(a, Cheetah)]

        result = [
            f"You have {len(self.animals)} animals",
            f"----- {len(lions)} Lions:",
            *[repr(l) for l in lions],
            f"----- {len(tigers)} Tigers:",
            *[repr(t) for t in tigers],
            f"----- {len(cheetahs)} Cheetahs:",
            *[repr(c) for c in cheetahs],
        ]
        return '\n'.join(result)

    def workers_status(self):
        keepers = [w for w in self.workers if isinstance(w, Keeper)]
        caretakers = [w for w in self.workers if isinstance(w, Caretaker)]
        vets = [w for w in self.workers if isinstance(w, Vet)]

        result = [
            f"You have {len(self.workers)} workers",
            f"----- {len(keepers)} Keepers:",
            *[repr(k) for k in keepers],
            f"----- {len(caretakers)} Caretakers:",
            *[repr(c) for c in caretakers],
            f"----- {len(vets)} Vets:",
            *[repr(v) for v in vets],
        ]
        return '\n'.join(result)
