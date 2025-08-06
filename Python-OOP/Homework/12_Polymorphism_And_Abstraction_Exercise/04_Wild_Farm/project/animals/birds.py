from .animal import Bird
from ..food import Vegetable, Fruit, Meat, Seed

class Owl(Bird):
    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += 0.25 * food.quantity
        self.food_eaten += food.quantity

class Hen(Bird):
    def make_sound(self):
        return "Cluck"

    def feed(self, food):
        # Hen eats everything
        self.weight += 0.35 * food.quantity
        self.food_eaten += food.quantity
