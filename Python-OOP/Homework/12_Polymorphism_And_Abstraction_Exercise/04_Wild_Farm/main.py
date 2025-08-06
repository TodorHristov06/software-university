from project.animals.animal import Bird
from project.animals.animal import Mammal
from project.animals.birds import Owl, Hen
from project.animals.mammals import Mouse, Dog, Cat, Tiger
from project.food import Vegetable, Fruit, Meat, Seed

owl = Owl("Owly", 2.5, 1.0)
print(owl.make_sound())  # Hoot Hoot
print(owl.feed(Meat(5))) # None (успешно)
print(owl.feed(Vegetable(3))) # Owl does not eat Vegetable!
print(owl)  # Owl [Owly, 1.0, weight_updated, food_eaten]

hen = Hen("Henrietta", 1.0, 0.5)
print(hen.feed(Seed(10)))  # Hen яде всичко
print(hen)

dog = Dog("Rex", 20, "Backyard")
print(dog.feed(Meat(3)))
print(dog.feed(Fruit(2))) # Dog does not eat Fruit!
print(dog)
